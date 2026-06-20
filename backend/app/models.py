from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime , timezone

from .database import Base


class Event(Base):

    __tablename__ = "events"


    id = Column(Integer, primary_key=True)

    event_id = Column(
        String,
        unique=True,
        index=True
    )

    user_id = Column(String)

    event_type = Column(String)

    amount = Column(Float)

    timestamp = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )



class Ledger(Base):

    __tablename__ = "ledger"


    id = Column(Integer, primary_key=True)

    user_id = Column(String)

    event_id = Column(String)

    transaction_type = Column(String)

    points = Column(Integer)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )