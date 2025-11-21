from fastapi import APIRouter
import json, uuid, datetime
from pathlib import Path

router = APIRouter()

DATA = Path(__file__).resolve().parents[2] / "data" / "doctor_schedule.json"

def load():
    return json.load(open(DATA))

def save(data):
    json.dump(data, open(DATA, "w"), indent=2)

@router.get("/availability")
def availability(date: str, appointment_type: str):
    data = load()

    weekday = datetime.datetime.fromisoformat(date).strftime("%A").lower()
    hours = data["working_hours"].get(weekday)

    if not hours:
        return {"available_slots": []}

    start, end = hours
    fmt = "%H:%M"

    s_dt = datetime.datetime.strptime(start, fmt)
    e_dt = datetime.datetime.strptime(end, fmt)

    slots = []
    cursor = s_dt
    while cursor < e_dt:
        st = cursor.strftime(fmt)
        en = (cursor + datetime.timedelta(minutes=30)).strftime(fmt)
        cursor += datetime.timedelta(minutes=30)
        slots.append({"start_time": st, "end_time": en, "available": True})

    return {"available_slots": slots}

@router.post("/book")
def book(payload: dict):
    data = load()

    booking_id = "APPT-" + uuid.uuid4().hex[:6].upper()
    payload["id"] = booking_id

    data["appointments"].append(payload)
    save(data)

    return {"confirmation_code": booking_id, "details": payload}
