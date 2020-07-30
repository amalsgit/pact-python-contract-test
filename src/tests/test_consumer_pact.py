import pytest
from consumer import consumer
from pact import Consumer, Provider, Like


def test_get_user():
    pact = Consumer("UserClient").has_pact_with(Provider("UserProvider"))
    # pact.start_service

    expected_body = {"email": "admin@localhost", "id": 42, "username": "admin"}

    (
        pact.given("admin user exists")
        .upon_receiving("a request for admin user")
        .with_request("get", "users/admin")
        .will_respond_with(200, Like(expected_body))
    )

    with pact:
        user = consumer.get_user_by_name("admin")
        assert user.username == "admin"

    pact.stop_service
