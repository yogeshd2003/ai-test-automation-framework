import requests
from utils.config import BASE_URL, API_TIMEOUT
from utils.assertions import assert_response_time, assert_keys_present

def test_sentiment_api_valid_text():
    payload = {'text': 'I love this product'}
    response = requests.post(f"{BASE_URL}/sentiment", json=payload, timeout=API_TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    assert_keys_present(data, ['sentiment', 'confidence'])
    assert_response_time(response, 1.5)
