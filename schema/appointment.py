from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
from datetime import datetime
from schema.patient import Patient
from schema.doctor import Doctor


class AppointmentStatus(Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"


class Appointment(BaseModel):
    id: int
    patient: Optional[Patient]
    doctor: Optional[Doctor]
    date: datetime
    status: AppointmentStatus = AppointmentStatus.PENDING


class CreateAppointment(BaseModel):
    patient_id: int
    date: datetime


"""
appointments database
"""
appointments: List[Appointment] = []
