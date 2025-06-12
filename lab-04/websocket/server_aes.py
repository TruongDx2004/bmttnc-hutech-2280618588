import tornado.ioloop
import tornado.web
import tornado.websocket
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import base64

class WebSocketAESHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True  # Cho phép tất cả origin (cần thiết nếu dùng frontend riêng)

    def open(self):
        print("Client connected.")
        self.aes_key = get_random_bytes(16)

    def on_message(self, message):
        print(f"Received plaintext: {message}")
        try:
            iv = get_random_bytes(16)
            cipher = AES.new(self.aes_key, AES.MODE_CBC, iv)
            ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
            encoded = base64.b64encode(iv + ciphertext).decode()
            self.write_message(encoded)
            print(f"Sent encrypted message: {encoded}")  # <--- Thêm dòng này
        except Exception as e:
            print("Encryption/send error:", e)

    def on_close(self):
        print("Client disconnected.")

def make_app():
    return tornado.web.Application([
        (r"/ws", WebSocketAESHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server listening on ws://localhost:8888/ws")
    tornado.ioloop.IOLoop.current().start()
