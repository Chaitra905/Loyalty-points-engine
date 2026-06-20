# Loyalty Points Engine

Backend service built using FastAPI for managing loyalty points.

## Features

- Transaction event ingestion
- Idempotent event processing
- Configurable rules engine
- Immutable points ledger
- Point redemption
- Transaction reversal
- Automated tests


## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pytest


## Project Architecture


backend

app/
- routers
- models
- schemas
- services


## Run Project


Install dependencies:

pip install -r requirements.txt


Start server:

uvicorn app.main:app --reload


API Docs:

http://127.0.0.1:8000/docs



## Design Decisions


### Idempotency

Each event has a unique event_id.
Before processing a new event, the system checks whether it already exists.

This prevents duplicate point awards.


### Ledger

Points are stored as immutable transactions instead of updating a balance directly.

Balance is calculated from ledger entries.


### Rules Engine

Point calculation rules are stored separately in rules.json,
allowing changes without modifying application logic.


## AI Usage Disclosure

AI tools were used for initial guidance and code review.
Architecture decisions, database design, API flow, and implementation choices were reviewed and modified based on understanding of backend requirements.