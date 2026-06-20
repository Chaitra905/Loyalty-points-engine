from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)



def test_insufficient_balance():


    response = client.post(

        "/redeem/",

        json={

            "user_id":"UNKNOWN",

            "points":100

        }

    )


    assert response.json()["error"] == "Insufficient points"