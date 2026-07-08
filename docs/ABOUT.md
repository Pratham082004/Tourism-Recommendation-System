# About the Project

**ExploreX** is an intelligent, full-stack Tourism Recommendation System designed to act as your 24/7 personal travel agent. By combining a dynamic React frontend, a robust Python Flask API, and a Scikit-learn Machine Learning engine, it completely reimagines the travel planning experience.

## 1. What it does
Imagine having a personal travel agent available 24/7. With ExploreX, you simply tell the system what you're looking for whether that's a strict budget, a specific number of days, or niche activities like scuba diving or hiking. You can also specify if you're looking to explore locally (Domestic) or cross borders (International). Behind the scenes, the system sifts through a comprehensive database of travel packages, mathematically scores how well each one aligns with your unique profile, and curates a list of the top 5 absolute best fits. To help you visualize your trip, it even plots nearby attractions on a dynamic, interactive map so you can see exactly what awaits you.

## 2. Why I chose this project
Planning a trip can be incredibly overwhelming. With the sheer volume of choices, destinations, and hidden costs out there, it's easy to suffer from decision fatigue. I have personally spent countless hours bouncing between static, frustrating travel websites, desperately trying to piece together a package that perfectly fits my budget while still letting me do the activities I love. 

I built ExploreX because it is the exact tool I genuinely wished existed when I was planning my own trips. I wanted to create an intelligent, virtual travel agent that eliminates the endless scrolling and guesswork. It programmatically connects travelers directly to the right packages based on their actual constraints and desires, turning a stressful planning phase into an exciting one.

## 3. What makes it special
Most standard search bars on travel websites rely on rigid, basic database queries (like simple SQL `WHERE` clauses). If you don't type the exact right keyword, you miss out on great options. 

ExploreX takes a much smarter approach. It uses a custom-built, weighted content-based filtering algorithm powered by Machine Learning (specifically, Scikit-learn). When you input your preferences, the system actually converts your desires into a mathematical vector. It then calculates the "cosine similarity" against every single package in the database to see how conceptually close they are to your dream trip. To make sure the recommendations are actually practical, it applies hard mathematical penalties to any package that exceeds your budget or time constraints. This guarantees that you are only ever shown truly viable, highly personalised options.
