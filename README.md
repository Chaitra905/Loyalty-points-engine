# Loyalty Points Engine 

A full-stack event-driven loyalty points management system built to handle customer reward events, point calculation, redemption, and transaction reversal with idempotency support.

This project was developed as a backend-focused assessment project with a React frontend dashboard and FastAPI.

---

# Features

## Event Processing

* Create loyalty events
* Automatic points calculation
* Rule-based reward system
* Prevent duplicate event processing using event_id

## Points Management

* View available balance
* Redeem points
* Validate insufficient balance
* Maintain transaction history

## Event Reversal

* Reverse previously processed events
* Restore points correctly
* Handle invalid event requests

## Reliability

* Idempotent API design
* Error handling
* Database persistence
* API documentation with Swagger

---

# Tech Stack

## Frontend

* React.js
* Vite
* Axios
* CSS3

## Backend

* Python
* FastAPI
* SQLAlchemy
* SQLite

## Testing

* Pytest
* FastAPI TestClient

---

# Project Structure

```
loyalty-points-engine
│
├── backend
│   │
│   ├── app
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── rules.py
│   │   ├── services.py
│   │   │
│   │   └── routers
│   │       ├── events.py
│   │       ├── redeem.py
│   │       └── reversal.py
│   │
│   ├── rules.json
│   ├── requirements.txt
│   └── loyalty.db
│
├── frontend
│   │
│   ├── src
│   ├── package.json
│   └── README.md
│
├── tests
│   ├── test_idempotency.py
│   └── test_redeem.py
│
└── README.md
```

---

# System Architecture

```
React Frontend
        |
        |
      Axios
        |
        |
FastAPI REST API
        |
        |
Business Logic Layer
        |
        |
SQLAlchemy ORM
        |
        |
SQLite Database
```

---

# Backend Setup

Navigate to backend:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run server:

```bash
uvicorn app.main:app --reload
```

Backend runs:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

Navigate:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run:

```bash
npm run dev
```

Frontend runs:

```
http://localhost:5173
```

---

# API Endpoints

## Create Event

POST

```
/events/
```

Example:

```json
{
 "event_id":"EV101",
 "user_id":"USER1",
 "event_type":"deposit",
 "amount":100,
 "timestamp":"2026-06-20"
}
```

Response:

```json
{
 "message":"Event processed successfully",
 "points_awarded":10
}
```

---

## Redeem Points

POST

```
/redeem/
```

Example:

```json
{
 "user_id":"USER1",
 "points":10
}
```

Response:

```json
{
 "message":"Points redeemed successfully",
 "remaining_balance":0
}
```

---

## Reverse Event

POST

```
/reverse/
```

Example:

```json
{
 "event_id":"EV101"
}
```

Response:

```json
{
 "message":"Event reversed successfully"
}
```

---

# Testing

Run tests:

```bash
pytest
```

Expected:

```
2 passed
```

Test coverage includes:

* Duplicate event prevention
* Redeem validation

---

# Deployment

The application can be deployed using:

Frontend:

* Render Static Site
* Netlify
* Vercel

Backend:

* Render Web Service

Production backend command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

---

# Key Design Decisions

## Idempotency

Each event uses a unique event_id to prevent duplicate point allocation.

## Rule-Based Points

Reward calculation is separated into rules.json, allowing business rules to change without modifying core logic.

## Transaction Based Ledger

Points are managed through transactions instead of directly modifying balances, improving reliability and traceability.

---

# Author

Chaitra

Full Stack Loyalty Points Engine Project
