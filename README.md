📌 Hospital Patient Management API

A RESTful backend API built with Flask and PostgreSQL for managing hospital patient records stored in a structured database schema.

This project demonstrates backend development skills including API design, database integration, and real-world debugging using SQLAlchemy ORM.

🚀 Features
Retrieve all patients (GET /patients)
Retrieve individual patient (GET /patients/<id>)
PostgreSQL database integration
Schema-based data modeling (analytics.patients)
SQLAlchemy ORM for database interaction
Real-time API testing using curl
Debugging of database and schema mismatches
🛠 Tech Stack
Python
Flask
Flask-SQLAlchemy
PostgreSQL
psycopg2
🧱 Project Structure
flask-hospital-api/
│
├── app.py              # Main Flask application
├── config.py           # Database configuration
├── models.py           # SQLAlchemy models
├── requirements.txt    # Dependencies
└── README.md
🗄 Database Schema

The project uses a PostgreSQL database:

Database: hospitaldb
Schema: analytics
Table: patients
📡 API Endpoints
🔹 Get all patients
GET /patients
🔹 Get patient by ID
GET /patients/<patient_id>

⚙️ Setup Instructions
1. Clone repository
git clone <your-repo-link>
cd flask-hospital-api
2. Install dependencies
pip install -r requirements.txt
3. Run the application
python app.py
4. Test API
curl http://127.0.0.1:5000/patients
🧠 Key Learning Outcomes

This project helped me gain hands-on experience in:

Building RESTful APIs with Flask
Working with PostgreSQL databases
Using SQLAlchemy ORM for database queries
Handling schema-based database structures
Debugging backend and database integration issues
Testing APIs using curl

⚠️ Challenges Solved
Fixed database schema mismatch (analytics.patients)
Resolved SQLAlchemy query issues
Debugged Flask runtime errors (IndentationError, NameError)
Handled API routing and request validation issues
Improved understanding of backend architecture

📈 Future Improvements
Add POST endpoint for creating patients
Add PUT endpoint for updating patient records
Add DELETE endpoint for removing records
Add input validation and error handling
Modularize code into blueprints (routes/models separation)
👤 Author

Aspiring Data Engineer (Nigeria)
