import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import AppointmentConfirmation from "./AppointmentConfirmation";
import "./chat.css";

export default function ChatInterface() {
  const [messages, setMessages] = useState([
    { from: "bot", text: "Hello! How can I help you today?" }
  ]);
  const [input, setInput] = useState("");
  const [confirmation, setConfirmation] = useState(null);
  const [loading, setLoading] = useState(false);

  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const pushMessage = (from, text) => {
    setMessages((prev) => [...prev, { from, text }]);
  };

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = input.trim();
    pushMessage("user", userMessage);
    setInput("");
    setLoading(true);

    try {
      const response = await axios.post("http://localhost:8001/api/chat/", {
        message: userMessage
      });

      pushMessage("bot", response.data.reply);

      if (response.data.meta?.booking) {
        setConfirmation(response.data.meta.booking);
      }
    } catch (error) {
      pushMessage("bot", "Something went wrong. Try again!");
    }

    setLoading(false);
  };

  return (
    <div className="chat-wrapper">
      <div className="chat-box">
        <h2 className="chat-title">Appointment Assistant</h2>

        <div className="messages">
          {messages.map((msg, i) => (
            <div key={i} className={`bubble ${msg.from}`}>
            {msg.from === "user" ? "🧑" : "🤖"} {msg.text}
            </div>
          ))}

          {loading && <div className="bubble bot">Typing...</div>}

          <div ref={messagesEndRef} />
        </div>

        <div className="input-box">
          <input
            type="text"
            placeholder="Type your message..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          />
          <button onClick={sendMessage}>Send</button>
        </div>
      </div>

      {confirmation && <AppointmentConfirmation booking={confirmation} />}
    </div>
  );
}
