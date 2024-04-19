from fastapi import FastAPI
from routers.patient import patient_router
from routers.doctor import doctor_router
from routers.appointment import appointment_router

app = FastAPI()

app.include_router(patient_router, prefix='/patients', tags=['Patient'])
app.include_router(doctor_router, prefix='/doctors', tags=['Doctor'])
app.include_router(appointment_router,
                   prefix='/appointments', tags=['Appointment'])


@app.get("/")
async def root():
    return {"message": "Hello User! navigate to the docs page just add /docs to your url"}
