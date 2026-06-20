from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import Event, Ledger
from ..schemas import EventCreate
from ..rules import calculate_points


router = APIRouter(
    prefix="/events",
    tags=["Events"]
)



def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



@router.post("/")
def create_event(
    event: EventCreate,
    db: Session = Depends(get_db)
):


    # Idempotency check

    existing = db.query(
        Event
    ).filter(
        Event.event_id == event.event_id
    ).first()



    if existing:

        return {
            "message":
            "Event already processed",
            "event_id":
            event.event_id
        }



    # Calculate points

    points = calculate_points(
        event.event_type,
        event.amount
    )



    # Save event

    new_event = Event(

        event_id = event.event_id,

        user_id = event.user_id,

        event_type = event.event_type,

        amount = event.amount

    )


    db.add(new_event)



    # Create ledger entry

    ledger = Ledger(

        user_id = event.user_id,

        event_id = event.event_id,

        transaction_type = "CREDIT",

        points = points

    )


    db.add(ledger)


    db.commit()



    return {

        "message":
        "Event processed successfully",

        "points_awarded":
        points

    }