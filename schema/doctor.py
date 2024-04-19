from pydantic import BaseModel


class Doctor(BaseModel):
    id: int
    first_name: str
    last_name: str
    specialization: str
    phone: str
    email: str
    is_available: bool = True


class CreateDoctor(BaseModel):
    first_name: str
    last_name: str
    specialization: str
    phone: str
    email: str
    is_available: bool = True


class UpdateDoctor(CreateDoctor):
    pass


# doctors in-memory database
doctors = [Doctor(
    **{
        "id": 1,
        "first_name": "Peter",
        "last_name": "Duru",
        "specialization": "Cardiologist",
        "phone": "1234567890",
        "email": "peterduru@gmail.com",
        "is_available": True
    }
),

    Doctor(
    **{
        "id": 2,
        "first_name": "Sandy",
        "last_name": "Adams",
        "specialization": "Surgeon",
        "phone": "1234567890",
        "email": "sandyadams@gmail.com",
        "is_available": False
    }
)]
