from pydantic import BaseModel

class Appointment(BaseModel):
    date: str
    start_time: str
    appointment_type: str
    patient_name: str
