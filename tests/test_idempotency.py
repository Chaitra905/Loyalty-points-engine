from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)



def test_duplicate_event():

    data = {

        "event_id":"TEST001",

        "user_id":"USER_TEST",

        "event_type":"deposit",

        "amount":500,

        "timestamp":"2026-06-20"

    }



    first = client.post(
        "/events/",
        json=data
    )


    second = client.post(
        "/events/",
        json=data
    )



    assert first.status_code == 200


    assert second.json()["message"] == "Event already processed"