import os
import re
import pandas as pd


class Domestic_Preprocessor:

    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.df = None

    def load_data(self): 
        self.df = pd.read_csv(self.input_file_path, encoding="ISO-8859-1")
        print(f"Dataset successfully loaded")
        return self.df
    
    def rename_columns(self):
        self.df.columns = (
            self.df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
            .str.replace("(", "", regex=False)
            .str.replace(")", "", regex=False)
            .str.replace("₹", "inr", regex=False)
            .str.replace("$", "usd", regex=False)
            .str.replace("/","_")
        )

    @staticmethod
    def clean_text(text):
        if pd.isna(text) or text == "":
            return ""
        
        text = str(text).lower()
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
        text = re.sub(r"\s+", " ", text)
        text = text.strip()

        return text
    
    def clean_text_columns(self):
        text_columns = [
            "package_name",
            "country",
            "cities_covered",
            "hotel_category",
            "meals",
            "transportation",
            "major_attractions",
            "activities",
            "package_type",
            "best_for"
        ]

        for column in text_columns:
            if column in self.df.columns:
                self.df[column] = self.df[column].apply(self.clean_text)

    def missing_values(self):
        text_columns = [
            "hotel_category",
            "meals",
            "transportation",
            "major_attractions",
            "activities",
            "package_type",
            "best_for"
        ]

        for column in text_columns:
            if column in self.df.columns:
                self.df[column] = self.df[column].fillna("not_specified")
        
        self.df["rating"] = self.df["rating"].fillna(0)

    def convert_datatypes(self):

        if "duration" in self.df.columns:

            self.df["duration"] = (
                self.df["duration"]
                .astype(str)
                .str.extract(r"(\d+)", expand=False)
            )

            self.df["duration"] = pd.to_numeric(
                self.df["duration"],
                errors="coerce"
            )

        if "rating" in self.df.columns:

            self.df["rating"] = pd.to_numeric(
                self.df["rating"],
                errors="coerce"
            )

        if "estimated_cost" in self.df.columns:

            self.df["estimated_cost"] = (
                self.df["estimated_cost"]
                .astype(str)
                .str.replace(",", "", regex=False)
                .str.replace("₹", "", regex=False)
            )

            self.df["estimated_cost"] = pd.to_numeric(
                self.df["estimated_cost"],
                errors="coerce"
            )
            
    def remove_duplicates(self):
        if "package_id" in self.df.columns:
            self.df.drop_duplicates(subset="package_id", inplace=True)

    def save_data(self):
        os.makedirs(os.path.dirname(self.output_file_path), exist_ok=True)
        self.df.to_csv(self.output_file_path, index=False)
        print(f"Preprocessed dataset saved to {self.output_file_path}")

    def process(self):
        self.load_data()
        self.rename_columns()
        self.missing_values()
        self.clean_text_columns()
        self.convert_datatypes()
        self.remove_duplicates()
        self.save_data()
        return self.df


if __name__ == "__main__":
    from pathlib import Path

    base_dir = Path(__file__).resolve().parent
    dataset_dir = base_dir / "dataset"
    processed_dir = base_dir / "data"

    input_file_path = str(dataset_dir / "International Package.csv")
    output_file_path = str(processed_dir / "international_cleaned.csv")


    preprocessor = Domestic_Preprocessor(input_file_path, output_file_path)
    preprocessor.process()


