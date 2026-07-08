# API Documentation

The backend of this system is a RESTful API built with Flask. I designed it to be as clean and predictable as possible. 

All endpoints return JSON. If something goes wrong, you'll receive a standard error object: `{"error": "Description of what broke"}`.

---

## 1. Recommendations

### `POST /recommendations/recommend`
This is the core "Brain" of the application. Send it a user's travel preferences, and the Scikit-learn engine will score and return the top 5 most highly correlated travel packages.

**Request Body (JSON):**
```json
{
    "user_preferences": {
        "destination_type": "international",
        "destination": "Singapore",
        "budget": 200000,
        "duration": 8,
        "hotel_category": "4 star",
        "activities": [
            "Culture",
            "Sightseeing"
        ],
        "package_type": "Luxury",
        "best_for": "Couples"
    }
}
```

**Response (200 OK):**
Returns a list of package objects, ordered by highest match score.
```json
{
   "data": [
      {
         "activities": "Theme Parks, Aquarium Visit, Cable Car Ride",
         "best_for": "Families",
         "cities_covered": "Singapore City, Sentosa Island",
         "country": "Singapore",
         "created_at": "Sun, 05 Jul 2026 18:55:32 GMT",
         "duration": "6D/5N",
         "estimated_cost": 95000.0
    }
  ]
}
```

---

## 2. Travel Packages

### `GET /packages/domestic`
Fetches a list of all domestic travel packages available in the database.

### `GET /packages/domestic/<package_id>`
Fetches the detailed itinerary and stats for a specific domestic package (e.g., `GOA001`).

### `GET /packages/international`
Fetches a list of all international travel packages.

### `GET /packages/international/<package_id>`
Fetches the detailed itinerary and stats for a specific international package.

---

## 3. Attractions & Maps

### `GET /attractions`
I integrated the OpenTripMap API to dynamically find cool places to visit near a selected city.

**Query Parameters:**
- `city` (string, required) - The name of the city (e.g., `?city=Paris`).

**Response (200 OK):**
```json
{
  "status": "success",
  "data": [
      {
         "category": "Attraction",
         "distance_m": 1,
         "latitude": 35.68948745727539,
         "longitude": 139.69171142578125,
         "name": "Meigaza Theater",
         "xid": "Q35134725"
      }
  ]
}
```

---

## 4. System Health

### `GET /`
A simple ping endpoint to verify that the Flask server is up and running.

**Response (200 OK):**
```json
{
    "message": "Welcome to the Tourism Recommendation System",
    "success": true
}
```

### `GET /health`
A simple endpoint to verify the health of the API's.
**Response (200 OK):**
```json
{
    "message": "API is healthy",
    "success": true
}
```

