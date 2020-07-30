import atexit
import unittest

from ..consumer import consumer

from pact import Consumer, Provider

PACT_MOCK_HOST = "localhost"
PACT_MOCK_PORT = "1234"

BASE_URL = "http://" + PACT_MOCK_HOST + ":" + PACT_MOCK_PORT

pact = Consumer("Consumer").has_pact_with(
    Provider("Provider"), host_name=PACT_MOCK_HOST, port=PACT_MOCK_PORT,
)
pact.start_service()
atexit.register(pact.stop_service)


class GetUserInfoContract(unittest.TestCase):
    def test_get_user(self):

        expected_body = {"email": "userA@localhost", "id": 42, "username": "userA"}

        (
            pact.given("userA exists in the system")
            .upon_receiving("a request to retrieve userA details")
            .with_request("get", "/users/userA")
            .will_respond_with(200, body=expected_body)
        )

        with pact:
            result = consumer.get_user_by_name(BASE_URL, "userA")

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json(), expected_body)
