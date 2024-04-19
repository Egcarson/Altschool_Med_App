from fastapi import APIRouter, HTTPException, status
from schema.appointment import Appointment, appointments, CreateAppointment, AppointmentStatus
from schema.patient import Patient, patients
from services.appointment import appointment_service
from schema.doctor import Doctor, doctors
from datetime import datetime

appointment_router = APIRouter()

# this function is retrieving all appointments


@appointment_router.get("/", status_code=200)
async def get_all_appointments():
    return {
        "message": "Appointments fetched successfully",
        "data": appointments
    }

# created an instance for creating a new appointment


@appointment_router.post("/", status_code=201)
async def create_appointment(appoint_in: CreateAppointment):
    appointment = appointment_service.create_apt(appoint_in)

    return {
        "message": "Appointment created successfully",
        "data": appointment
    }

# created an instance to complete an appointment


@appointment_router.put("/complete{id}", status_code=200)
def complete_appointment(id: int):
    appointment = appointment_service.complete_apt(id)
    if appointment:
        return {
            "message": "Appointment completed successfully"
        }


# created an instance to cancel an appointment


@appointment_router.delete("/{id}", status_code=200)
async def cancel_appointment(id: int):
    appointment = appointment_service.cancel_apt(id)
    if appointment:
        return {
            "message": "Appointment canceled successfully"
        }
