from locust import HttpUser, task, between

class AIUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def sentiment_test(self):
        self.client.post('/sentiment', json={'text': 'Performance test'})
