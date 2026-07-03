import { useState } from "react";
import {DESTINATIONS, PACKAGE_TYPES, HOTEL_CATEGORIES, BEST_FOR, ACTIVITIES} from "../../utils/constants";

function RecommendationForm() {

    const [formData, setFormData] = useState({
        destination_type: "",
        country: "",
        budget: "",
        duration: "",
        package_type: "",
        best_for: "",
        hotel_category: "",
        activity: []
        }
    );

    const[activityInput, setActivityInput] = useState("");

    const handleChange = (event) =>{
        const {name, value} = event.target;
        if (name === "destination_type"){
            setFormData((prev) => ({
                ...prev,
                destination_type: value,
                country: ""
            }));
            return;
        }
        setFormData((prev) => ({
            ...prev,
            [name]: value
        }));
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        const payload = {
            user_preferences: formData
        };

        console.log(payload);
    };

    const addActivity = (activity) => {
        if(formData.activity.includes(activity)){
            return;
        }
        setFormData((prev) => ({
            ...prev,
            activity: [...prev.activity, activity]
        }));
        setActivityInput("");
    };

    const removeActivity = (activity) => {
        setFormData((prev) => ({
            ...prev,
            activity: prev.activity.filter((item) => item !== activity)
    }))
    }

    const filteredDestination = DESTINATIONS[formData.destination_type] || [];

    const filteredActivity = ACTIVITIES.filter((activity) =>
        activity
            .toLowerCase()
            .includes(activityInput.toLowerCase()) &&
        !formData.activity.includes(activity)
    );

    return (
        <form onSubmit={handleSubmit}>

            <h2>Travel Preferences</h2>
            <hr />
            {/* Destination Type Selection*/}
            <div>
                <label>Destination Type</label>
                <select
                    name="destination_type"
                    value={formData.destination_type}
                    onChange={handleChange}
                    required
                >
                    <option value="">Select Destination Type</option>
                    <option value="Domestic">Domestic</option>
                    <option value="International">International</option>
                </select>
            </div>

            <br />

            {/* Select destination */}
            <div>
                <label>Destination</label>
                <select 
                    name="country"
                    value={formData.country}
                    onChange={handleChange}
                    required
                    disabled={!formData.destination_type}
                >
                    <option value = "">Select Your Prefered Destination</option>

                    {filteredDestination.map((destination) => (
                        <option
                            key={destination}
                            value={destination}
                        >
                            {destination}
                        </option>
                    ))}
                </select>
            </div>

            <br />

            {/* User's Budget */}
            <div>
                <label>Budget</label>
                <input
                    type="number"
                    name="budget"
                    placeholder="Enter Budget"
                    value={formData.budget}
                    onChange={handleChange}
                    required
                />
            </div>

            <br />

            {/* User's Duration in days*/}
            <div>
                <label>Duration (Days)</label>
                <input
                    type="number"
                    name="duration"
                    min="1"
                    placeholder="Enter Duration"
                    value={formData.duration}
                    onChange={handleChange}
                    required
                />
            </div>

            <br />

            {/*User's Prefered Hotel Category*/}
            <div>
                <label>Hotel Category</label>
                <select
                    name="hotel_category"
                    value={formData.hotel_category}
                    onChange={handleChange}
                    required
                >
                    <option value="">Select Your Preferred Hotel Categoroy</option>
                    {HOTEL_CATEGORIES.map((hotel) => (
                        <option
                            key={hotel}
                            value={hotel}
                        >
                            {hotel}
                        </option>
                    ))}
                </select>
            </div> 

            <br />

            {/*User's Choose thier Package Type*/}
            <div>
                <label>Package Type</label>
                <select
                    name="package_type"
                    value={formData.package_type}
                    onChange={handleChange}
                    required
                >
                    <option value="">Select Your Prefered Package Type</option>
                    {PACKAGE_TYPES.map((type) => (
                        <option
                            key={type}
                            value={type}
                        >
                            {type}
                        </option>
                    ))}
                </select>
            </div>

            <br />

            {/* Distinguish between solo, couples, family */}
            <div>
                <label>Best For</label>
                <select 
                    name="best_for"
                    value={formData.best_for}
                    onChange={handleChange}
                    required
                >
                    <option value="">Select</option>
                    {BEST_FOR.map((item)=>(
                        <option 
                            key={item}
                            value={item}
                        >
                            {item}
                        </option>

                    ))}
                </select>
            </div>

            <br />

            {/* User's Prefered Activities */}
            <div>
                <label>Activities</label>
                <br />
                <input
                    type="text"
                    placeholder="Search Activities..."
                    value={activityInput}
                    onChange={(e) =>
                        setActivityInput(e.target.value)
                    }
                />
                {
                    activityInput && (
                        <div>
                            {filteredActivity.length === 0 ? (
                                <p>No Activity Found</p>
                            ) : (
                                filteredActivity.map((activity) => (
                                    <div
                                        key={activity}
                                        onClick={() => addActivity(activity)}
                                        style={{
                                            cursor: "pointer",
                                            padding: "5px"
                                        }}
                                    >
                                        {activity}
                                    </div>
                                ))
                            )}
                        </div>
                    )
                }
            </div>

            <br />

            {/* User Selects the Activities */}
            <div>
                {formData.activity.map((activity) => (
                    <span
                        key={activity}
                        style={{
                            display: "inline-block",
                            padding: "5px 10px",
                            margin: "5px",
                            border: "1px solid black",
                            borderRadius: "20px"
                        }}
                    >
                        {activity}
                        <button
                            type="button"
                            onClick={() => removeActivity(activity)}
                            style={{
                                marginLeft: "8px",
                                cursor: "pointer"
                            }}
                        >
                            ✕
                        </button>
                    </span>
                ))}
            </div>

            <br />

            <button type="submit">
                Get Recommendations
            </button>
        </form>
    );
}

export default RecommendationForm;