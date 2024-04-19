# SECOND SEMESTER EXAMINATION

# Medical Appointment Application :rocket:

Hello! :wave:

Welcome to the Medical Appointment Application! This API facilitates appointment bookings between patients and doctors. It allows patients to create, cancel, and complete appointments, and doctors to set their availability status. This `README.md` file provides an overview of the application and guides you through the setup and usage.

## Table of Contents

1. [Features](#features)
2. [Setup](#setup)
3. [Endpoints](#endpoints)
    - [Patient Endpoints](#patient-endpoints)
    - [Doctor Endpoints](#doctor-endpoints)
    - [Appointment Endpoints](#appointment-endpoints)

## Features

- **CRUD for Patients**: Add, update, delete, and retrieve patient information.
- **CRUD for Doctors**: Add, update, delete, and retrieve doctor information.
- **Create Appointments**: Patients can schedule appointments with doctors.
- **Cancel Appointments**: Patients can cancel scheduled appointments.
- **Complete Appointments**: Completing an appointment marks it as finished and makes the doctor available for new appointments.
- **Set Doctor Availability**: Doctors can set their availability status to manage appointment bookings.

## Setup

To set up the Medical Appointment Application, follow these steps:

1. Clone the repository to your local machine:

    ```shell
    git clone https://github.com/Egcarson/Altschool_Med_App.git
    ```

2. Navigate to the project directory:

    ```shell
    cd Altschool_Med_App
    ```

3. Create a virtual environment:

    ```shell
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On macOS/Linux:

        ```shell
        source venv/bin/activate
        ```

    - On Windows:

        ```shell
        venv\Scripts\activate
        ```

5. Install the required dependencies:

    ```shell
    pip install -r requirements.txt
    ```

6. Start the FastAPI server:

    ```shell
    uvicorn app:app --reload
    ```

7. The API should now be running locally at [http://localhost:8000](http://localhost:8000).

## Endpoints

### Patient Endpoints

- **GET** `/patients/`: Retrieve a list of all patients.
- **GET** `/patients/{id}`: Retrieve information about a specific patient by ID.
- **POST** `/patients/`: Create a new patient.
- **PUT** `/patients/{id}`: Update an existing patient by ID.
- **DELETE** `/patients/{id}`: Delete a patient by ID.

### Doctor Endpoints

- **GET** `/doctors/`: Retrieve a list of all doctors.
- **GET** `/doctors/{id}`: Retrieve information about a specific doctor by ID.
- **GET** `/doctors/specification/{specification}`: Retrieve information about set of doctors having thesame specification.
- **POST** `/doctors/`: Create a new doctor.
- **PUT** `/doctors/{id}`: Update an existing doctor by ID.
- **DELETE** `/doctors/{id}`: Delete a doctor by ID.
- **PUT** `/doctors/{id}/availability`: Update a doctor's availability status.

### Appointment Endpoints

- **POST** `/appointments/`: Create a new appointment.
- **DELETE** `/appointments/{id}`: Cancel an appointment by ID.
- **PUT** `/appointments/complete/{id}`: Complete an appointment by ID.


This project is an [AltSchool](https://altschoolafrica.com/) second semester examination solution. Though feel free to use, modify, and distribute the application as you see fit.

# BYE :wave: :relaxed: