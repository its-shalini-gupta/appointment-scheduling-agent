import React from "react";

export default function AppointmentConfirmation({ booking }) {
  if (!booking) return null;

  const details = booking.details || booking;

  return (
    <div className="confirm-box">
      <h3>Appointment Confirmed 🎉</h3>
      <p><strong>Date:</strong> {details.date}</p>
      <p><strong>Time:</strong> {details.start_time}</p>
      <p><strong>Patient:</strong> {details.patient?.name}</p>
      <p><strong>Confirmation ID:</strong> {booking.confirmation_code || "N/A"}</p>
    </div>
  );
}
