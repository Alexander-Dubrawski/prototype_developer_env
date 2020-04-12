from zmq import REQ, Context, Socket

from settings import client_url


class BaseSocket:
    """Base Socket that interacts directly with zmq."""

    def __init__(self):
        """Initialize a BaseSocket."""
        self._url = client_url
        self.open()

    def __enter__(self):
        """Return self for a context manager."""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Call close with a context manager."""
        self.close()
        return None

    def open(self):
        """Open socket connection."""
        context = Context(io_threads=1)
        socket = context.socket(REQ)
        socket.connect(self._url)
        self._socket: Socket = socket

    def close(self):
        """Close socket connection."""
        self._socket.disconnect(self._url)
        self._socket.close()

    def send_message(self, message):
        """Send message to socket."""
        self._socket.send(message)
        response = self._socket.recv()
        return response
