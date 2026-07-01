import os
from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


class Vectorizer:
    def __init__(self, input_file):
        self.input_file = input_file
        self.df = None
        self.vectorizer = None
        self.package_vectors = None

    def load_dataset(self):
        self.df = pd.read_csv(self.input_file)
        print(f"Successfully loaded dataset from {self.input_file}")

    def vectorize(self):
        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2),
            min_df=1,
        )

        self.package_vectors = self.vectorizer.fit_transform(self.df["package_profile"])

    def save_model(self):
        pipeline_dir = {
            "vectorizer": self.vectorizer,
            "package_vectors": self.package_vectors,
            "packages": self.df,
        }

        base_dir = Path(__file__).resolve().parent
        model_dir = base_dir / "models"
        os.makedirs(model_dir, exist_ok=True)
        model_path = str(model_dir / "domestic_model.pkl")

        joblib.dump(pipeline_dir, model_path)
        print("Domestic Model saved successfully.")

    def process(self):
        self.load_dataset()
        self.vectorize()
        self.save_model()


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    processed_dir = base_dir / "data"

    vectorizer = Vectorizer(str(processed_dir / "domestic_training.csv"))
    vectorizer.process()


    