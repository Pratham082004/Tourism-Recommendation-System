from ml.International.recommend import International_Recommendation_Engine

MODEL_PATH = "ml/International/models/international_model.pkl"

engine = International_Recommendation_Engine(MODEL_PATH)

# Test User
user = {
    "country": "Japan",
    "budget": 10000000,
    "duration": 7,
    "hotel_category": "4 star",
    "activities": [
        "Adventure",
        "Nature"
    ],
    "package_type": "Adventure",
    "best_for": "Couples"
}

# Dataset Information
print("=" * 80)
print("DATASET INFORMATION")
print("=" * 80)

print(engine.packages.columns.tolist())

print("\nAvailable Countries:")
print(engine.packages["country"].unique())

print("\nDuration Statistics:")
print(engine.packages["duration"].describe())

print("\nEstimated Cost Statistics:")
print(engine.packages["estimated_cost"].describe())

# Recommendation
recommendations = engine.recommend(user, top_k=5)

print("\n" + "=" * 80)
print("TOP 5 INTERNATIONAL PACKAGE RECOMMENDATIONS")
print("=" * 80)

if not recommendations:
    print("No recommendations found.")
else:
    for i, package in enumerate(recommendations, start=1):
        print(f"\nRank #{i}")
        print("-" * 60)
        print(f"Package ID      : {package['package_id']}")
        print(f"Package Name    : {package['package_name']}")
        print(f"Country         : {package['country']}")
        print(f"Duration        : {package['duration']} Days")
        print(f"Package Type    : {package['package_type']}")
        print(f"Estimated Cost  : ₹{package['estimated_cost']}")
        print(f"Rating          : {package['rating']}")
        print(f"Score           : {package['score']:.4f}")