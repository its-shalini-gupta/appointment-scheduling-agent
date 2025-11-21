import requests

def process_message(message: str, context: dict):
    msg = message.lower()

    if "book" in msg:
        return ("Sure! What date would you like to book? (YYYY-MM-DD)", {})

    # detect date
    if "-" in msg:
        date = msg.strip()
        r = requests.get(
            "http://localhost:8001/api/calendly/availability",
            params={"date": date, "appointment_type": "consultation"}
        ).json()

        slots = r["available_slots"][:5]
        if not slots:
            return ("No slots available on this date.", {})

        reply = "Available slots:\n" + "\n".join(
            f"- {s['start_time']}" for s in slots
        )
        return (reply, {"date": date})

    return ("I can help with booking. Say 'book appointment'.", {})
