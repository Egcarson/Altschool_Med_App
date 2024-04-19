from schema.doctor import Doctor, doctors


class DoctorService():

    @staticmethod
    def id_validate(id: int):
        for doc in doctors:
            if doc.id == id:
                return doc

    @staticmethod
    def specialization_validate(specialization: str):
        doctors_with_specialization = []
        for doctor in doctors:
            if doctor.specialization == specialization:
                doctors_with_specialization.append(doctor)
        if doctors_with_specialization:
            return doctors_with_specialization


doctor_service = DoctorService()
