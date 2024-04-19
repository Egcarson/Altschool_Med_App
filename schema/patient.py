from pydantic import BaseModel


class Patient(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str
    email: str


class CreatePatient(BaseModel):
    first_name: str
    last_name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str
    email: str


class UpdatePatient(BaseModel):
    first_name: str
    last_name: str
    weight: float
    height: float
    phone: str
    email: str


# patients in-memory database
patients = [Patient(
    **{
        "id": 1,
        "first_name": "Ann",
        "last_name": "Doe",
        "age": 26,
        "sex": "f",
        "weight": 60.5,
        "height": 1.75,
        "phone": "123-456-7890",
        "email": "anndoe@gmail.com"
    }
),

    Patient(
    **{
        "id": 2,
        "first_name": "John",
        "last_name": "Doe",
        "age": 29,
        "sex": "male",
        "weight": 70,
        "height": 1.75,
        "phone": "123-456-7890",
        "email": "johndoe@gmail.com"
    }
)]
