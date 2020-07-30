from consumer import consumer


def test_consumer():
    response = consumer.get_user_by_name("admin")
    print(response)
