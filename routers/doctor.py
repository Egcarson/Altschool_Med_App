from fastapi import APIRouter, HTTPException, status
from schema.doctor import Doctor, CreateDoctor, UpdateDoctor, doctors
from services.doctor import doctor_service

doctor_router = APIRouter()

# you see this code right here? its used in adding new doctors to our squad


@doctor_router.post("/", status_code=201)
def create_doctor(doctor_in: CreateDoctor):
    _id = len(doctors) + 1
    new_doctor = Doctor(
        id=_id,
        **doctor_in.dict()
    )
    doctors.append(new_doctor)
    return {
        "message": "Doctor created successfully",
        "data": new_doctor
    }

# retrieving all doctors


@doctor_router.get("/", status_code=200)
def get_doctors():
    return {
        "message": "Doctors retrieved successfully",
        "data": doctors
    }


# retrieving doctors base on specializations
@doctor_router.get("/specialization/{specialization}", status_code=200)
def get_doctors_by_specializations(specialization: str):
    doctor = doctor_service.specialization_validate(specialization)
    if doctor:
        return {
            "message": "Doctors retrieved successfully base on specializations",
            "data": doctor
        }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Not a valid specialization"
    )


# retreiving doctors information with id
@doctor_router.get("/{id}", status_code=200)
def get_doctors_by_id(id: int):
    doctor = doctor_service.id_validate(id)

    if doctor:
        return {
            "message": "Doctor retrieved successfully",
            "data": doctor
        }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Doctor with id {id} not found"
    )


# updating doctors information
@doctor_router.put("/", status_code=200)
def update_doctor(id: int, doctor_in: UpdateDoctor):
    doctor = doctor_service.id_validate(id)
    if doctor:
        doctor.first_name = doctor_in.first_name
        doctor.last_name = doctor_in.last_name
        doctor.specialization = doctor_in.specialization
        doctor.phone = doctor_in.phone
        doctor.email = doctor_in.email
        doctor.is_available = doctor_in.is_available
        return {
            "message": "Doctor updated successfully",
            "data": doctor
        }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Doctor with id {id} not found"
    )

# initialized an instance for availability update


@doctor_router.put("/{id}", status_code=200)
def status_update(id: int, is_available: bool):
    doctor = doctor_service.id_validate(id)

    if doctor:
        doctor.is_available = is_available
        return {
            "message": "Doctor status updated succesfully successfully",
            "data": doctor
        }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Doctor with id {id} not found"
    )


# deleting doctors information


@doctor_router.delete("/", status_code=200)
async def delete_doctor(id: int):
    doctor = doctor_service.id_validate(id)
    if doctor:
        doctors.remove(doctor)
        return {
            "message": "Doctor has been deleted successfully!",
            "data": doctor
        }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Doctor with id {id} not found or has been deleted"
    )
