from ml.domestic.recommend import Domestic_Recommendation_Engine

MODEL_PATH = "ml/domestic/models/domestic_model.pkl"

engine = Domestic_Recommendation_Engine(MODEL_PATH)

user = {
    "country": "India",
    "budget": 50000,
    "city": "Mumbai",
    "duration": 5,
    "hotel_category": "4 star",
    "activities": [
        "Adventure",
        "Nature"
    ],
    "package_type": "Couples",
    "best_for": "4"
}
print(engine.packages.columns.tolist())

print(engine.packages["country"].unique())

print(engine.packages["duration"].describe())

print(engine.packages["estimated_cost"].describe())

recommendations = engine.recommend(user, top_k=5)

print("=" * 80)
print("TOP 5 DOMESTIC PACKAGE RECOMMENDATIONS")
print("=" * 80)

if not recommendations:
    print("No recommendations found.")
else:
    for i, package in enumerate(recommendations, start=1):
        print(f"\nRank #{i}")
        print("-" * 60)

        print(f"Package ID     : {package['package_id']}")
        print(f"Package Name   : {package['package_name']}")
        print(f"Country        : {package['country']}")
        print(f"Duration       : {package['duration']} Days")
        print(f"Package Type   : {package['package_type']}")
        print(f"Estimated Cost : ₹{package['estimated_cost']}")
        print(f"Rating         : {package['rating']}")
        print(f"Score          : {package['score']}")