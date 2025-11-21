import requests

def book_appointment(payload):
    return requests.post(
        "http://localhost:8001/api/calendly/book",
        json=payload
    ).json()
