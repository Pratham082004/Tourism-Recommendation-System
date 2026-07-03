import RecommendationForm from "../components/RecommendationForm/RecommendationForm";

function Recommendation(){
    return (
        <main className="container">
            <h1>Find Your Perfect Trip</h1>
            <p>
                Fill in your travel preferences to receive personalized travel
                package recommendations.
            </p>

            <RecommendationForm />

        </main>
    );
}

export default Recommendation;