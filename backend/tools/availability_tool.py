import requests

def get_availability(date, appointment_type="consultation"):
    return requests.get(
        "http://localhost:8001/api/calendly/availability",
        params={"date": date, "appointment_type": appointment_type}
    ).json()
