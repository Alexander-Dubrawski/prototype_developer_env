from flask import Flask
from flask_cors import CORS
from flask_restx import Api, Resource
from base_socket import BaseSocket

app = Flask(__name__)
CORS(app)
api = Api(app)


def send_message(message):
    with BaseSocket() as socket:
        response = socket.send_message(message)
    return response


@api.route("/throughput")
class Throughput(Resource):
    def get(self, **kwargs):
        return send_message(b"throughput").decode("utf-8")


@api.route("/latency")
class Latency(Resource):
    def get(self, **kwargs):
        return send_message(b"latency").decode("utf-8")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
