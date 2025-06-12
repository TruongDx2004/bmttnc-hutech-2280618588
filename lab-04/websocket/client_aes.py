import tornado.ioloop
import tornado.websocket
import threading
import time

class WebSocketClient:
    def __init__(self, io_loop):
        self.connection = None
        self.io_loop = io_loop

    def start(self):
        self.connect()

    def connect(self):
        tornado.websocket.websocket_connect(
            "ws://localhost:8888/ws",
            callback=self.on_connect
        )

    def on_connect(self, future):
        try:
            self.connection = future.result()
            print("Connected to server.")
            self.start_input_thread()
            self.read_next_message()  # Bắt đầu vòng lặp đọc
        except Exception as e:
            print(f"Connection failed: {e}")
            self.io_loop.call_later(3, self.connect)

    def read_next_message(self):
        self.connection.read_message().add_done_callback(self.on_message)

    def on_message(self, future):
        message = future.result()
        if message is None:
            print("Connection closed by server.")
            return
        print(f"\n Encrypted message from server: {message}")
        self.read_next_message() 

    def start_input_thread(self):
        def input_loop():
            while True:
                msg = input("Enter message to send: ")
                self.io_loop.add_callback(self.send_message, msg)
        thread = threading.Thread(target=input_loop, daemon=True)
        thread.start()

    def send_message(self, msg):
        if self.connection:
            self.connection.write_message(msg)

def main():
    io_loop = tornado.ioloop.IOLoop.current()
    client = WebSocketClient(io_loop)
    client.start()
    io_loop.start()

if __name__ == "__main__":
    main()
