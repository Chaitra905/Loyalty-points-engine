from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routers import events, redeem, reversal


Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="Loyalty Points Engine"
)


# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(
    events.router
)

app.include_router(
    redeem.router
)

app.include_router(
    reversal.router
)



@app.get("/")
def home():

    return {
        "message":
        "Loyalty Points Engine Running"
    }