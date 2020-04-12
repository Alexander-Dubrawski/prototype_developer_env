from os import getenv

server_url = getenv("URL", "tcp://*:5555")
client_url = getenv("URL", "tcp://localhost:5555")
