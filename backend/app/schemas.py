from pydantic import BaseModel


class EventCreate(BaseModel):

    event_id:str

    user_id:str

    event_type:str

    amount:float

    timestamp:str



class RedeemRequest(BaseModel):

    user_id:str

    points:int



class ReverseRequest(BaseModel):

    event_id:str