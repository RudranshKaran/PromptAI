from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_rephrase_endpoint():
    response = client.post(
        "/rephrase",
        json={"prompt": "Make me a better prompt generator"}
    )
    assert response.status_code == 200
    assert "enhanced_prompt" in response.json()
    
def test_invalid_request():
    response = client.post(
        "/rephrase",
        json={}
    )
    assert response.status_code == 422
