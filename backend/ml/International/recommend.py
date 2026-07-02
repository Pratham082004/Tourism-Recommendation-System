import joblib
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


class International_Recommendation_Engine:

    def __init__(self, model_path: str):

        pipeline = joblib.load(model_path)

        self.vectorizer = pipeline["vectorizer"]
        self.package_vectors = pipeline["package_vectors"]
        self.packages = pipeline["packages"]

    @staticmethod
    def _normalize_best_for(best_for_val):
        """Map numeric/semantic family codes to dataset-like best_for text."""
        if best_for_val is None:
            return ""

        # Handle numeric inputs (1/2/4/5)
        if isinstance(best_for_val, (int, float)):
            v = int(best_for_val)
            if v == 1:
                return "students, solo travelers"
            if v == 2:
                return "couples"
            if v in (4, 5):
                return "families"

        # Handle strings
        s = str(best_for_val).strip().lower()

        if s in {"1", "solo", "solotravelers", "solo traveler", "single"}:
            return "students, solo travelers"
        if s in {"2", "couple", "couples"}:
            return "couples"
        if s in {"4", "5", "family", "families", "familise"}:
            return "families"

        return s

    @staticmethod
    def _as_text(x) -> str:
        if x is None:
            return ""
        return str(x).strip().lower()

    def build_user_profile(self, user: dict) -> str:
        """Construct a weighted profile string matching the vectorizer's scheme."""
        best_for = self._normalize_best_for(user.get("best_for"))

        country = self._as_text(user.get("country"))
        activities = self._as_text(user.get("activities"))
        package_type = self._as_text(user.get("package_type"))
        hotel_category = self._as_text(user.get("hotel_category"))

        profile_tokens = (
            [country] * 4
            + [activities] * 4
            + [package_type] * 3
            + [best_for] * 3
            + [hotel_category] * 2
        )
        return " ".join(profile_tokens).strip()

    def _get_estimated_cost_col(self) -> str:
        # Handle both possibilities depending on preprocessing/header
        for col in ("estimated_cost"):
            if col in self.packages.columns:
                return col
        # Let it fail clearly if neither exists
        return "estimated_cost"


    def apply_hard_filters(self, user: dict) -> pd.DataFrame:
        """ Applies initial strict constraints for country, budget, and trip duration. """
        filtered = self.packages.copy()

        if user.get("country"):
            filtered = filtered[filtered["country"].str.lower() == user["country"].lower()]

        cost_col = self._get_estimated_cost_col()
        filtered = filtered[filtered[cost_col] <= user["budget"] * 1.20]

        filtered = filtered[(filtered["duration"] - user["duration"]).abs() <= 2]


        return filtered

    def recommend(self, user: dict, top_k: int = 5) -> list:
        """ Generates hybrid recommendations sorted by appropirate score. """
        filtered = self.apply_hard_filters(user)
        if filtered.empty:
            return []

        user_profile = self.build_user_profile(user)
        user_vector = self.vectorizer.transform([user_profile])
        matched_vectors = self.package_vectors[filtered.index]
        text_sims = cosine_similarity(user_vector, matched_vectors)[0]

        cost_col = self._get_estimated_cost_col()
        costs = filtered[cost_col].to_numpy()
        durations = filtered["duration"].to_numpy()
        ratings = filtered["rating"].to_numpy()

        max_cost_diff = np.max(np.abs(costs - user["budget"])) or 1.0
        max_dur_diff = np.max(np.abs(durations - user["duration"])) or 1.0

        budget_scores = 1.0 - (np.abs(costs - user["budget"]) / max_cost_diff)
        duration_scores = 1.0 - (np.abs(durations - user["duration"]) / max_dur_diff)
        rating_scores = np.nan_to_num(ratings / 5.0, nan=0.0)

        hotel_stars = {"3 star": 3, "4 star": 4, "5 star": 5}
        user_star = hotel_stars.get(user["hotel_category"].lower(), 3)
        package_stars = filtered["hotel_category"].str.lower().map(hotel_stars).fillna(3).to_numpy()
        hotel_scores = 1.0 - (np.abs(user_star - package_stars) / 5.0)

        user_activities = set(act.lower() for act in user["activities"])
        
        def calculate_act_overlap(pkg_act_str):
            if not user_activities:
                return 0.0
            pkg_set = set(str(pkg_act_str).lower().split())
            return len(pkg_set.intersection(user_activities)) / len(user_activities)

        activity_scores = filtered["activities"].apply(calculate_act_overlap).to_numpy()

        text_weight = 0.55
        activity_weight = 0.15
        budget_weight = 0.10
        duration_weight = 0.88
        hotel_weight = 0.07
        rating_weight = 0.05
        
        final_scores = (
            text_weight * text_sims +
            activity_weight* activity_scores +
            budget_weight * budget_scores +
            duration_weight * duration_scores +
            hotel_weight * hotel_scores +
            rating_weight * rating_scores
        )

        filtered = filtered.copy()
        filtered["score"] = np.round(final_scores, 4)
        
        top_packages = filtered.sort_values(by="score", ascending=False).head(top_k) # Top 5 Packages

        return top_packages[[
            "package_id", 
            "package_name", 
            "country", 
            "duration", 
            "estimated_cost", 
            "package_type",
            "rating", "score"
        ]].to_dict(orient="records")

