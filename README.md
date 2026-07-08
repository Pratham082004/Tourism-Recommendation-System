# ExploreX - Tourism Recommendation System

**ExploreX** is an intelligent, full-stack Tourism Recommendation System that acts as your 24/7 personal travel agent. Powered by a custom Machine Learning engine (Scikit-learn), a Flask REST API, and a dynamic React frontend, ExploreX mathematically scores and curates the absolute best travel packages tailored exactly to your budget, timeline, and unique interests.

## Documentation

I have split the documentation into dedicated files to keep this README clean:

- **[About the Project](docs/ABOUT.md)**: Details on what ExploreX does, why I chose to build it, and what makes it special.
- **[Architecture Deep-Dive](docs/ARCHITECTURE.md)**: Explains the Flask/React/Scikit-learn infrastructure and the ML Cosine Similarity engine.
- **[Installation & Setup Guide](INSTALL.md)**: Step-by-step instructions for running this project via Docker (Plug & Play) or Manual setup.
- **[API Documentation](docs/API_DOCUMENTATION.md)**: A complete list of all RESTful endpoints, expected JSON payloads, and responses.
- **[USAGE Documentation](USAGE.md)**: A complete guide on how to interact with the application.

## Project Structure

```text
Tourism-Recommendation-System/
│
├── backend/                  # Flask backend & ML logic
│   ├── app.py                # Application entry point
│   ├── config.py             # Configuration files
│   ├── controller/           # API route handlers
│   ├── database/             # Database connection logic
│   ├── ml/                   # Machine learning models
│   ├── repositories/         # Database data access layer
│   ├── routes/               # API blueprints
│   ├── services/             # Core business logic
│   └── requirements.txt      # Python dependencies
│
├── docs/                     # Project documentation
│   ├── ABOUT.md              # Project overview
│   ├── API_DOCUMENTATION.md  # API endpoints
│   └── ARCHITECTURE.md       # System architecture
│
├── frontend/                 # React frontend
│   ├── public/               # Static assets
│   ├── src/                  # React source code
│   ├── package.json          # Node dependencies
│   └── vite.config.js        # Vite configuration
│
├── mysql-db/                 # Custom MySQL docker setup
│
├── docker-compose.yml        # Docker configuration
├── INSTALL.md                # Installation guide
├── USAGE.md                  # Application usage guide
└── README.md                 # Main entry point
```

---

## Tech Stack

Frontend: React (JavaScript dialect), Vite  
Backend: Flask (Python web framework for building APIs)  
Database: MySQL (Relational Database to store our data)  
Machine Learning: Scikit-learn (To provide intelligent recommendations)  
Containerization Platform: Docker (To pack an application and all of its dependencies into a single unit called a container and run on any system that has Docker installed)  

## Referred Sites

https://react.dev/  
https://flask.palletsprojects.com/  
https://www.mysql.com/  
https://www.docker.com/  
https://scikit-learn.org/  
https://vitejs.dev/  
https://www.makemytrip.com/holidays-india/  
https://www.thomascook.in/  

## Dataset and Open-Source APIs Referred

*(Note: The following datasets and APIs were used as references to create a dummy dataset for the database)*

Kaggle Dataset : https://www.kaggle.com/datasets/dhrubangtalukdar/top-indian-places-to-visit-indian-tourism  
Kaggle Dataset : https://www.kaggle.com/datasets/rkiattisak/traveler-trip-data/data  
Open-Source API : https://dev.opentripmap.org/docs  
Icon : https://icons8.com/icons/  

## AI Usage Declaration

To be fully transparent, I used AI tools (like ChatGPT/Copilot) to help speed up repetitive tasks and debugging in this project:
- **Data Generation:** I used AI to help format and generate the dummy MySQL data based on the Kaggle datasets, as writing hundreds of rows of SQL inserts by hand is incredibly tedious.  
- **Error Fixing & Debugging:** I used AI to help troubleshoot obscure bugs, resolve syntax errors, and identify issues during development.

Everything else React UI, Flask architecture, Scikit-learn cosine similarity logic, SQL database schema, and Docker infrastructure was built by me.  

## ExploreX-Tourism Recommendation System Screenshots

### UI Screenshots
![Recommendation Form](frontend/project_screenshots/RecommendationForm.png)  
![Output Page 1](frontend/project_screenshots/Output1.png)  
![Output Page 2](frontend/project_screenshots/Output2.png)  
### Database Screenshots
![MySQL 1](frontend/project_screenshots/Mysql1.png)  
![MySQL 2](frontend/project_screenshots/Mysql2.png)
### API Screenshots
![Postman 1](frontend/project_screenshots/Postman1.png)  
![Postman 2](frontend/project_screenshots/Postman2.png)  
![Postman 3](frontend/project_screenshots/Postman3.png) 
### Docker Screenshots
![Docker Desktop 1](frontend/project_screenshots/DockerDesktop1.png)  
![Docker Desktop 2](frontend/project_screenshots/DockerDesktop2.png)


 

