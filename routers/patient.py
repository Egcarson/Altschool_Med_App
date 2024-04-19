from fastapi import APIRouter, HTTPException, status
from schema.patient import Patient, patients, CreatePatient, UpdatePatient
from services.patient import patient_service

patient_router = APIRouter()


@patient_router.post("/", status_code=201)
def create_patient(patient_in: CreatePatient):
    _id = len(patients) + 1

    new_patient = Patient(
        patient_id=_id,
        **patient_in.dict()
    )

    patients.append(new_patient)
    return {
        "message": "Patient created successfully",
        "data": new_patient
    }


@patient_router.get("/", status_code=200)
async def get_patients():
    return {
        "message": "Patients retrieved successfully",
        "data": patients
    }

# retreiving patient's information with id number


@patient_router.get("/{patient_id}", status_code=200)
async def get_patient(patient_id: int):
    patient = patient_service.id_validate(patient_id)
    if patient:
        return {
            "message": "Patient retrieved successfully",
            "data": patient
        }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Patient not found"
    )

# retrieving patient's information with patient's full name


@patient_router.get("/{first_name}/{last_name}")
def get_patient_by_name(first_name: str, last_name: str):
    patient_name = patient_service.name_validate(first_name, last_name)

    if patient_name:
        return {
            "message": "Patient retrieved successfully",
            "data": patient_name
        }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Nor vex check your spelling or Patient not found"
    )


@patient_router.put("/", status_code=200)
async def update_patient(patient_id: int, patient_in: UpdatePatient):
    patient = patient_service.id_validate(patient_id)
    if patient:
        patient.first_name = patient_in.first_name
        patient.last_name = patient_in.last_name
        patient.weight = patient_in.weight
        patient.height = patient_in.height
        patient.phone = patient_in.phone
        patient.email = patient_in.email
        return {
            "message": "Patient updated successfully",
            "data": patient
        }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Patient not found"
    )


@patient_router.delete("/", status_code=200)
async def delete_patient(patient_id: int):
    patient_del = patient_service.id_validate(patient_id)

    if patient_del:
        patients.remove(patient_del)
        return {
            "message": "Patient deleted successfully",
            "data": patient_del
        }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Patient not found or has been deleted"
    )
