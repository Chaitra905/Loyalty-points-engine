from .models import Ledger


def get_balance(db,user_id):

    records = db.query(
        Ledger
    ).filter(
        Ledger.user_id==user_id
    ).all()


    return sum(
        x.points for x in records
    )