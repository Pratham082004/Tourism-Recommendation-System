import os
import pandas as pd

class FeatureEngineer:

    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file
        self.df = None

    def load_dataset(self):
        self.df = pd.read_csv(self.input_file)
        print(f"Successfully loaded dataset from {self.input_file}")

    @staticmethod
    def get_budget_category(cost: float) -> str:
        if cost <= 25000:
            return "budget"
        if cost <= 50000:
            return "standard"
        if cost <= 100000:
            return "premium"
        return "luxury"

    @staticmethod
    def get_duration_category(days: int) -> str:
        if days <= 3:
            return "weekend"
        if days <= 6:
            return "short_trip"
        if days <= 10:
            return "vacation"
        return "long_trip"

    def create_features(self):
        self.df["budget_category"] = self.df["estimated_cost"].apply(self.get_budget_category)
        self.df["duration_category"] = self.df["duration"].apply(self.get_duration_category)

    def create_package_profile(self):
        cols_to_fill = [
            "country", 
            "activities", 
            "cities_covered",
            "package_type", 
            "best_for",
            "major_attractions", 
            "hotel_category", 
            "budget_category", 
            "duration_category", 
            "transportation", 
            "meals"
        ]
        temp_df = self.df[cols_to_fill].fillna("").astype(str)

        highest_priority = (temp_df["country"] + " ") * 4 + (temp_df["activities"] + " ") * 4
        high_priority = (temp_df["cities_covered"] + " ") * 3 + (temp_df["package_type"] + " ") * 3 + (temp_df["best_for"] + " ") * 3
        medium_priority = (temp_df["major_attractions"] + " ") * 2 + (temp_df["hotel_category"] + " ") * 2 + (temp_df["budget_category"] + " ") * 2 + (temp_df["duration_category"] + " ") * 2
        low_priority = temp_df["transportation"] + " " + temp_df["meals"]

        self.df["package_profile"] = (
            highest_priority + high_priority + medium_priority + low_priority
        ).str.strip().str.replace(r"\s+", " ", regex=True)

    def save_dataset(self):
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        self.df.to_csv(self.output_file, index=False)
        print(f"Training dataset saved to {self.output_file}")

    def process(self):
        self.load_dataset()
        self.create_features()
        self.create_package_profile()
        self.save_dataset()


if __name__ == "__main__":
    from pathlib import Path

    base_dir = Path(__file__).resolve().parent
    processed_dir = base_dir / "data"

    engineer = FeatureEngineer(
        input_file=str(processed_dir / "international_cleaned.csv"),
        output_file=str(processed_dir / "international_training.csv"),
    )
    engineer.process()
