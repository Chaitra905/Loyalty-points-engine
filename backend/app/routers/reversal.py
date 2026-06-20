from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import Event, Ledger
from ..schemas import ReverseRequest


router = APIRouter(
    prefix="/reverse",
    tags=["Reversal"]
)



def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



@router.post("/")
def reverse_event(
    request: ReverseRequest,
    db: Session = Depends(get_db)
):


    event = db.query(
        Event
    ).filter(
        Event.event_id == request.event_id
    ).first()



    if not event:

        return {

            "error":
            "Event not found"

        }



    existing_reverse = db.query(
        Ledger
    ).filter(
        Ledger.event_id == request.event_id,
        Ledger.transaction_type=="REVERSAL"
    ).first()



    if existing_reverse:

        return {

            "message":
            "Already reversed"

        }



    original = db.query(
        Ledger
    ).filter(
        Ledger.event_id == request.event_id
    ).first()



    reversal = Ledger(

        user_id = event.user_id,

        event_id = request.event_id,

        transaction_type = "REVERSAL",

        points = -original.points

    )


    db.add(reversal)

    db.commit()



    return {

        "message":
        "Event reversed successfully",

        "reversed_points":
        original.points

    }