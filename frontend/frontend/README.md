# Dish Management System

This project is a full-stack application for managing and displaying dish information, including a database, API, and front-end dashboard.

## Getting Started

### Prerequisites

- Python 3.x
- Node.js
- npm

### Setting Up

1. Clone the repository.

   ```
   git clone https://github.com/your-repo/dish-management-system.git
   cd dish-management-system

2. Set up the backend.
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Initialize the SQLite database.
sqlite3 dishes.db < schema.sql
python populate_db.py

4. Start the backend server.
flask run

5. Set up the frontend.
cd ../frontend/frontend
npm install

6. Start the frontend server.
npm start
