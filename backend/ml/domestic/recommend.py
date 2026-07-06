import joblib
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity


class Domestic_Recommendation_Engine:
    """Recommend domestic tourism packages for a user profile."""

    def __init__(self, model_path: str):
        """Load the trained domestic recommendation artifacts."""
        pipeline = joblib.load(model_path)

        self.vectorizer = pipeline["vectorizer"]
        self.package_vectors = pipeline["package_vectors"]
        self.packages = pipeline["packages"]

    @staticmethod
    def _normalize_best_for(best_for_val):
        """Normalize the `best_for` field into values expected by the dataset."""

        if best_for_val is None:
            return ""

        if isinstance(best_for_val, (int, float)):
            value = int(best_for_val)

            if value == 1:
                return "students solo travelers"
            elif value == 2:
                return "couples"
            elif value in (4, 5):
                return "families"

        value = str(best_for_val).strip().lower()

        mapping = {
            "1": "students solo travelers",
            "solo": "students solo travelers",
            "solo traveler": "students solo travelers",
            "solo travelers": "students solo travelers",
            "student": "students solo travelers",
            "students": "students solo travelers",
            "2": "couples",
            "couple": "couples",
            "couples": "couples",
            "4": "families",
            "5": "families",
            "family": "families",
            "families": "families",
        }

        return mapping.get(value, value)

    @staticmethod
    def _as_text(value):
        """Convert arbitrary input to a clean, lowercased string."""
        if value is None:
            return ""
        return str(value).strip().lower()

    def build_user_profile(self, user: dict):
        """Create a weighted text profile string from user preferences.

        The recommendation model is TF-IDF based, so we convert structured fields into
        a single text string. Each component is repeated to express relative importance.
        """

        destination = self._as_text(user.get("destination"))
        activities = self._as_text(user.get("activities"))
        package_type = self._as_text(user.get("package_type"))
        hotel_category = self._as_text(user.get("hotel_category"))
        best_for = self._normalize_best_for(user.get("best_for"))

        profile = (
            [destination] * 4 +
            [activities] * 4 +
            [package_type] * 3 +
            [best_for] * 3 +
            [hotel_category] * 2
        )

        return " ".join(profile).strip()

    def apply_hard_filters(self, user: dict):
        """Filter packages before scoring."""

        filtered = self.packages.copy()

        if user.get("destination"):
            filtered = filtered[
                filtered["destination"].str.lower() == user["destination"].lower()
            ]

        filtered = filtered[
            filtered["estimated_cost"] <= user["budget"] * 1.20
        ]

        filtered = filtered[
            (filtered["duration"] - user["duration"]).abs() <= 2
        ]

        return filtered

    def recommend(self, user: dict, top_k: int = 5):
        """Generate top-K recommendations for a given user."""

        filtered = self.apply_hard_filters(user)

        if filtered.empty:
            return []

        user_profile = self.build_user_profile(user)

        user_vector = self.vectorizer.transform([user_profile])

        matched_vectors = self.package_vectors[filtered.index]

        text_similarity = cosine_similarity(
            user_vector,
            matched_vectors
        )[0]

        costs = filtered["estimated_cost"].to_numpy()
        durations = filtered["duration"].to_numpy()
        ratings = filtered["rating"].fillna(0).to_numpy()

        max_cost_diff = np.max(np.abs(costs - user["budget"])) or 1
        max_duration_diff = np.max(np.abs(durations - user["duration"])) or 1

        budget_scores = 1 - (
            np.abs(costs - user["budget"]) / max_cost_diff
        )

        duration_scores = 1 - (
            np.abs(durations - user["duration"]) / max_duration_diff
        )

        rating_scores = ratings / 5

        hotel_mapping = {
            "3 star": 3,
            "4 star": 4,
            "5 star": 5
        }

        user_star = hotel_mapping.get(
            user["hotel_category"].lower(),
            3
        )

        package_stars = (
            filtered["hotel_category"]
            .str.lower()
            .map(hotel_mapping)
            .fillna(3)
            .to_numpy()
        )

        hotel_scores = 1 - (
            np.abs(user_star - package_stars) / 5
        )

        user_activities = {
            activity.strip().lower()
            for activity in user.get("activities", [])
        }

        def activity_overlap(package_activities):
            if not user_activities:
                return 0

            package_set = {
                activity.strip().lower()
                for activity in str(package_activities).split(",")
            }

            return (
                len(package_set & user_activities)
                / len(user_activities)
            )

        activity_scores = (
            filtered["activities"]
            .apply(activity_overlap)
            .to_numpy()
        )

        final_scores = (
            0.55 * text_similarity +
            0.15 * activity_scores +
            0.10 * budget_scores +
            0.08 * duration_scores +
            0.07 * hotel_scores +
            0.05 * rating_scores
        )

        filtered = filtered.copy()

        filtered["score"] = np.round(final_scores, 4)

        recommendations = (
            filtered
            .sort_values("score", ascending=False)
            .head(top_k)
        )

        return recommendations.to_dict(orient="records")