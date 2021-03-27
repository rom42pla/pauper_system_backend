from fastapi.testclient import TestClient
from main import app

client = TestClient(app=app)


def test_roll_dice():
    assert client.get(f"/utils/roll/d20").status_code == 200
    assert client.get(f"/utils/roll/2 - d8 + 4").status_code == 200
    assert client.get(f"/utils/roll/d10 + 3 d 4").status_code == 200
    assert client.get(f"/utils/roll/d0").status_code != 200
    assert client.get(f"/utils/roll/d-1").status_code != 200
