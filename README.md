# Hospital Flask API

A beginner REST API built with Python and Flask for managing hospital patient data.

## Features

* Retrieve all patients
* Retrieve a specific patient by ID
* Return JSON responses
* Dynamic route parameters
* Basic error handling with HTTP 404 responses

## Technologies Used

* Python
* Flask
* JSON
* REST APIs

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd flask-hospital-api
```

### Create a virtual environment

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

### Home Endpoint

```http
GET /
```

Response:

```text
Hospital API is running!
```

### Get All Patients

```http
GET /patients
```

### Get Patient By ID

```http
GET /patients/2
```

Example Response:

```json
{
  "patient_id": 2,
  "name": "Jane Smith"
}
```

### Error Handling

```http
GET /patients/99
```

Response:

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
* CRUD operations
* Appointment management
* Docker containerization
* Authentication and authorization
