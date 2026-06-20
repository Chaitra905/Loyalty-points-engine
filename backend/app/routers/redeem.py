from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import Ledger
from ..schemas import RedeemRequest
from ..services import get_balance


router = APIRouter(
    prefix="/redeem",
    tags=["Redeem"]
)



def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



@router.post("/")
def redeem_points(
    request: RedeemRequest,
    db: Session = Depends(get_db)
):


    balance = get_balance(
        db,
        request.user_id
    )


    if balance <= 0 or request.points > balance:

        return {

            "error":
            "Insufficient points",

            "available_balance":
            balance

        }



    ledger = Ledger(

        user_id=request.user_id,

        event_id="REDEEM",

        transaction_type="DEBIT",

        points=-request.points

    )


    db.add(ledger)

    db.commit()



    return {

        "message":
        "Points redeemed successfully",

        "remaining_balance":
        balance - request.points

    }