from flask import Flask, jsonify, request

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
@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()

    if "name" not in data:
        return {"error": "Patient name is required"}, 400

    new_patient = {
        "patient_id": len(patients) + 1,
        "name": data["name"]
    }

    patients.append(new_patient)

    return new_patient, 201

@app.route('/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):

    for patient in patients:
        if patient["patient_id"] == patient_id:
            patients.remove(patient)
            return {"message": "Patient deleted successfully"}, 200

    return {"error": "Patient not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)