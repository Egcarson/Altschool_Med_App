from schema.patient import Patient, patients


class PatientService():

    @staticmethod
    def id_validate(patient_id: int):
        for patient in patients:
            if patient.patient_id == patient_id:
                return patient

    @staticmethod
    def name_validate(first_name: str, last_name: str):
        for patient in patients:
            if patient.first_name == first_name and patient.last_name == last_name:
                return patient


patient_service = PatientService()
