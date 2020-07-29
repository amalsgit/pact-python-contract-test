from flask import Flask, abort, jsonify

fakedb = {"admin": {"username": "admin", "email": "admin@localhost", "id": 42}}

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return "Hello world"


@app.route("/users/<name>", methods=["GET"])
def get_user_by_name(name):
    user_data = fakedb.get(name)
    print(user_data)
    if not user_data:
        abort(404)
    response = jsonify(**user_data)
    return response


if __name__ == "__main__":
    app.run(debug=True)
