import tkinter as tk
from tornado.websocket import websocket_connect
import tornado.ioloop
import threading

class WebSocketAESClient:
    def __init__(self, master):
        self.master = master
        self.master.title("AES Client")
        self.master.geometry("500x300")

        self.label = tk.Label(master, text="Nhập thông điệp:")
        self.label.pack()

        self.entry = tk.Entry(master, width=50)
        self.entry.pack()

        self.send_button = tk.Button(master, text="Gửi", command=self.send_message)
        self.send_button.pack(pady=5)

        self.output_label = tk.Label(master, text="Kết quả mã hoá AES:")
        self.output_label.pack()

        self.result_text = tk.Text(master, height=8, width=60)
        self.result_text.pack()

        self.connection = None

        # Start WebSocket connection in another thread
        threading.Thread(target=self.start_websocket, daemon=True).start()

    def start_websocket(self):
        self.loop = tornado.ioloop.IOLoop()
        tornado.ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')
        self.loop.make_current()
        self.loop.run_sync(self.connect)

    async def connect(self):
        try:
            self.connection = await websocket_connect("ws://localhost:8888/ws")
            self.read_message()
        except Exception as e:
            print("WebSocket connection error:", e)

    def send_message(self):
        if self.connection and self.entry.get():
            message = self.entry.get()
            self.connection.write_message(message)

    def read_message(self):
        self.connection.read_message(callback=self.on_message)

    def on_message(self, message):
        if message:
            self.result_text.insert(tk.END, message + "\n")
            self.result_text.see(tk.END)
        self.read_message()  # Continue listening

# Start tkinter GUI
if __name__ == "__main__":
    root = tk.Tk()
    client = WebSocketAESClient(root)
    root.mainloop()
