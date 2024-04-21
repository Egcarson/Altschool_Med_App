from fastapi import HTTPException, status
from schema.appointment import Appointment, appointments, CreateAppointment, AppointmentStatus
from schema.patient import Patient, patients
from schema.doctor import Doctor, doctors
from datetime import datetime


class AppointmentService():

    # logic for creating an appointment
    # this is to make the routing endpoints neater and more efficient
    @staticmethod
    def create_apt(appoint_in: CreateAppointment):
        #   check if the patient exists in the patient's database
        patient = next((pt for pt in patients if pt.id ==
                       appoint_in.patient_id), None)
        if not patient:
            raise HTTPException(
                status_code=404,
                detail="Patient not found"
            )

        #   check if the doctor exists in the doctor's database
        doctor = next((doc for doc in doctors if doc.is_available), None)
        if not doctor:
            raise HTTPException(
                status_code=404,
                detail="No doctor available. Please try again later."
            )

        # well then now, we can create a new appointment
        appointment_id = len(appointments) + 1
        new_appointment = Appointment(
            id=appointment_id,
            patient=patient,
            doctor=doctor,
            date=appoint_in.date
        )
        appointments.append(new_appointment)
        doctor.is_available = False
        return new_appointment

    # logic for completing an appointment
    @staticmethod
    def complete_apt(id: int):
        #   check if the appointment is available
        appointment = next(
            (app for app in appointments if app.id == id), None)

        if not appointment:
            raise HTTPException(
                status_code=404,
                detail="Appointment not found"
            )

        # checking if the appointment is already completed
        if appointment.status == AppointmentStatus.COMPLETED:
            raise HTTPException(
                status_code=400,
                detail="Appointment already completed! Please dont break my api bikonu!"
            )

        # checking if the doctor is available
        doctor = next((doc for doc in doctors if doc.id == id), None)

        if not doctor:
            raise HTTPException(
                status_code=404,
                detail="Doctor not found"
            )

        appointment.status = AppointmentStatus.COMPLETED
        doctor.is_available = True

        return appointment

    # logic for cancelling an appointment
    @staticmethod
    def cancel_apt(id: int):
        appointment = next(
            (app for app in appointments if app.id == id), None)

        if not appointment:
            raise HTTPException(
                status_code=404,
                detail="Appointment not found"
            )
        appointments.remove(appointment)
        appointment.doctor.is_available = True

        return appointment


appointment_service = AppointmentService()
