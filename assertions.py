def assert_response_time(response, max_seconds):
    assert response.elapsed.total_seconds() < max_seconds

def assert_keys_present(data, keys):
    for key in keys:
        assert key in data
