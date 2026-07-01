import joblib
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


class DomesticRecommendationEngine:

    def __init__(self, model_path: str):
        pipeline = joblib.load(model_path)
        self.vectorizer = pipeline["vectorizer"]
        self.package_vectors = pipeline["package_vectors"]
        self.packages = pipeline["packages"]

    def build_user_profile(self, user: dict) -> str:
        """Constructs a weighted profile string matching the vectorizer's scheme."""
        profile_tokens = ([user["country"]] * 4 + user["activities"] * 4 + [user["package_type"]] * 3 + [user["best_for"]] * 3 + [user["hotel_category"]] * 2)
        return " ".join(profile_tokens).lower()

    def apply_hard_filters(self, user: dict) -> pd.DataFrame:
        """Applies initial strict constraints for country, budget, and trip duration."""
        filtered = self.packages.copy()

        if user.get("country"):
            filtered = filtered[filtered["country"].str.lower() == user["country"].lower()]

        # Hard budget ceiling (+20% leeway)
        filtered = filtered[filtered["estimated_cost_inr"] <= user["budget"] * 1.20]

        # Duration bounds (+/- 2 days tolerance)
        filtered = filtered[(filtered["duration"] - user["duration"]).abs() <= 2]

        return filtered

    def recommend(self, user: dict, top_k: int = 5) -> list:
        """Generates hybrid recommendations sorted by relevance score."""
        filtered = self.apply_hard_filters(user)
        if filtered.empty:
            return []

        # 1. Content Similarity Matrix (Cosine Distance)
        user_profile = self._build_user_profile(user)
        user_vector = self.vectorizer.transform([user_profile])
        matched_vectors = self.package_vectors[filtered.index]
        text_sims = cosine_similarity(user_vector, matched_vectors)[0]

        # 2. Vectorized Metric Calculations (Fast NumPy execution)
        costs = filtered["estimated_cost_inr"].to_numpy()
        durations = filtered["duration"].to_numpy()
        ratings = filtered["rating"].to_numpy()

        # Safely normalize difference metrics preventing division-by-zero or negative breaks
        max_cost_diff = np.max(np.abs(costs - user["budget"])) or 1.0
        max_dur_diff = np.max(np.abs(durations - user["duration"])) or 1.0

        budget_scores = 1.0 - (np.abs(costs - user["budget"]) / max_cost_diff)
        duration_scores = 1.0 - (np.abs(durations - user["duration"]) / max_dur_diff)
        rating_scores = np.nan_to_num(ratings / 5.0, nan=0.0)

        # 3. Vectorized Sub-Scores (Hotel and Activities)
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

        # 4. Final Hybrid Scoring Array Matrix
        final_scores = (
            0.55 * text_sims +
            0.15 * activity_scores +
            0.10 * budget_scores +
            0.08 * duration_scores +
            0.07 * hotel_scores +
            0.05 * rating_scores
        )

        # 5. Compile Results
        filtered = filtered.copy()
        filtered["score"] = np.round(final_scores, 4)
        
        # Sort and take top K entries
        top_packages = filtered.sort_values(by="score", ascending=False).head(top_k)

        return top_packages[[
            "package_id", 
            "package_name", 
            "country", 
            "duration", 
            "estimated_cost", 
            "rating", "score"
        ]].to_dict(orient="records")