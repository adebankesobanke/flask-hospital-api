# Flask Hospital API

A RESTful API built with Python and Flask for managing hospital patient records. This project demonstrates API development fundamentals including CRUD operations, JSON responses, HTTP status codes, route parameters, and error handling.

## Features

* Create a patient record
* Retrieve all patients
* Retrieve a specific patient by ID
* Update an existing patient
* Delete a patient
* JSON request and response handling
* Dynamic route parameters
* HTTP status code handling
* Basic error handling

## Technologies Used

* Python
* Flask
* JSON
* REST APIs
* Git
* GitHub

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd flask-hospital-api
```

### Create and activate a virtual environment

```bash
python -m venv venv
source venv/Scripts/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

The application will run at:

```text
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint       | Description                |
| ------ | -------------- | -------------------------- |
| GET    | /              | Health check               |
| GET    | /patients      | Retrieve all patients      |
| GET    | /patients/<id> | Retrieve a patient by ID   |
| POST   | /patients      | Create a new patient       |
| PUT    | /patients/<id> | Update an existing patient |
| DELETE | /patients/<id> | Delete a patient           |

## Example Responses

### Get Patient

```json
{
  "patient_id": 2,
  "name": "Jane Smith"
}
```

### Patient Not Found

```json
{
  "error": "Patient not found"
}
```

Status Code:

```text
404 Not Found
```

## Future Improvements

* PostgreSQL integration
* SQLAlchemy ORM integration
* Appointment management endpoints
* Docker containerization
* Authentication and authorization
* Unit and integration testing

## Learning Outcomes

This project demonstrates:

* REST API design principles
* CRUD operations
* HTTP methods (GET, POST, PUT, DELETE)
* HTTP status codes
* JSON data handling
* Git and GitHub workflow
* Flask application development
