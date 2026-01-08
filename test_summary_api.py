import requests
from utils.config import BASE_URL

def test_summary_empty_text():
    response = requests.post(f"{BASE_URL}/summary", json={'text': ''})
    assert response.status_code == 400
