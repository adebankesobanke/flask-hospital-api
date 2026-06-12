from flask import Flask, jsonify

app = Flask(__name__)

patients = [
    {"patient_id": 1, "name": "John Doe"},
    {"patient_id": 2, "name": "Jane Smith"},
    {"patient_id": 3, "name": "Mike Brown"}
]

@app.route("/")
def home():
    return "Hospital API is running!"

@app.route("/patients")
def get_patients():
    return jsonify(patients)
@app.route("/patients/<int:patient_id>")
def get_patient(patient_id):

    for patient in patients:
        if patient["patient_id"] == patient_id:
            return jsonify(patient)

    return {"error": "Patient not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)