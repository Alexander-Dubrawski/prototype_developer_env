import zmq
from settings import server_url

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind(server_url)

print("Service running")

while True:
    #  Wait for next request from client
    message = socket.recv()
    if message == b"throughput":
        socket.send(b"throughput -> 200")
    elif message == b"latency":
        socket.send(b"latency -> 42")
    else:
        socket.send(b"error")
