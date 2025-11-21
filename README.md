Project Setup Guide

📌 Frontend Setup

1️⃣ Install dependencies
npm install axios
npm install axios clsx
npm install

2️⃣ Install TailwindCSS
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

3️⃣ Start the frontend server
npm start

📌 Backend Setup
1️⃣ Create a virtual environment
python -m venv .venv

2️⃣ Activate the virtual environment

Windows:

.venv\Scripts\activate


Mac/Linux:

source .venv/bin/activate

3️⃣ Install backend dependencies
pip install -r requirements.txt

4️⃣ Run the backend server (FastAPI)
uvicorn backend.main:app --reload --port 8000

✅ Both servers running

Frontend: http://localhost:3000

Backend: http://localhost:8001
