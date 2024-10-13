import unittest
from src.app import app
from faker import Faker

fake = Faker()
Faker.seed(1000000)

def mock_task_client():
    class TaskMock:
        def create_task(self):
            return None

    return TaskMock()

class TestRegisterEmailFailsWhenEmailIsMissing(unittest.TestCase):
    def setUp(self):
        self.headers = {"Authorization": "Bearer Token"}
        self.user = dict()
        self.user["app_uuid"] = fake.uuid4()
        self.user["blocked_reason"] = fake.text()

    def test_should_return_400_when_email_is_missing(self, *args):
        with app.test_client() as test_client:
            response = test_client.post(
                f"/blacklists",
                json=self.user,
                content_type="application/json",
                headers=self.headers,
            )
        assert response.status_code == 400
