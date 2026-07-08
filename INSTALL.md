# Installation & Setup Guide

Getting a full-stack application (with a database and ML pipelines) running locally can sometimes be a nightmare. I hate spending hours debugging environment variables, so I dockerized everything to make it as "plug-and-play" as possible.

You have two options to run this project: **The Easy Way (Docker)** or **The Hard Way (Manual)**.

---

## Option 1: The Easy Way (Docker) 
I highly recommend this route. It will spin up the Frontend, Backend, and Database automatically, and even seed the database with the required dummy data.

**Prerequisites:**
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

**Steps:**
1. Clone the repository:
   ```bash
   git clone https://github.com/Pratham082004/ExploreX-Tourism-Recommendation-System
   cd ExploreX-Tourism-Recommendation-System
   ```
2. Run the command:
   ```bash
   docker-compose up  
   ```
3. **Wait about 30 seconds** for the database to fully initialize and seed the data. 
4. Open your browser and go to `http://localhost:5173`. You're done!

> [!TIP]
> **Troubleshooting Note:** If the backend keeps crashing on startup, it usually means Docker has cached an old version of the MySQL database. Run `docker-compose down -v` to wipe the old database volume, then try `docker-compose up` again.

---

## Option 2: The Hard Way (Manual Setup) 
If you want to actively develop the code and see hot-reloads, you'll want to run the services locally on your host machine.

### 1. Database Setup
You will need a local MySQL server running on port `3306`.
- Navigate to the `backend/` folder.
- Copy `.env.example` to a new file named `.env`.
- Update the database variables in `.env` to match your local MySQL credentials (e.g., `DB_HOST=localhost`, `DB_USER=tourism_user`, `DB_PASSWORD=tourism123`, `DB_NAME=tourism_db`, `DB_PORT=3306`).

### 2. Backend Setup (Python)
You need Python 3.9+ installed.
```bash
cd backend

# Create a virtual environment so we don't mess up your global Python packages
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate
# Activate it (Mac/Linux)
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt

# Start the Flask server
python app.py
```
*The backend API will now be running on `http://localhost:5000`.*

### 3. Frontend Setup (React)
You need Node.js installed. Open a **new** terminal window:
```bash
cd frontend

# Install the Node modules
npm install

# Start the Vite development server
npm run dev
```
*The frontend will now be running on `http://localhost:5173`.*
