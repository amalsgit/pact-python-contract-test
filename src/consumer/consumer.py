import requests


def get_user_by_name(base_url, name):
    uri = base_url + "/users/" + name
    return requests.get(uri)
