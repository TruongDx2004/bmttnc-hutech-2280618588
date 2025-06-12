import tkinter as tk
from tkinter import scrolledtext, ttk
import tornado.ioloop
import tornado.websocket
import threading
import queue
import functools

class WebSocketClient:
    """
    Lớp WebSocketClient được sửa đổi để giao tiếp với UI qua một hàng đợi (queue).
    """
    def __init__(self, url, ui_queue):
        self.url = url
        self.ui_queue = ui_queue  # Hàng đợi để gửi dữ liệu về UI
        self.connection = None
        self.io_loop = None

    def start(self):
        """Bắt đầu vòng lặp IOLoop và kết nối."""
        self.io_loop = tornado.ioloop.IOLoop()
        self.io_loop.make_current()
        self.connect_and_read()
        self.io_loop.start()
        self.log_to_ui("Tornado IOLoop has stopped.")

    def stop(self):
        """Dừng kết nối và IOLoop một cách an toàn."""
        if self.connection:
            self.connection.close()
        if self.io_loop:
            # Dừng IOLoop từ một luồng khác
            self.io_loop.add_callback(self.io_loop.stop)

    def log_to_ui(self, message):
        """Gửi tin nhắn vào hàng đợi để UI xử lý."""
        self.ui_queue.put(message)

    def connect_and_read(self):
        self.log_to_ui("Đang kết nối đến server...")
        tornado.websocket.websocket_connect(
            url=self.url,
            callback=self.maybe_retry_connection,
            on_message_callback=self.on_message,
            ping_interval=10,
            ping_timeout=30,
        )

    def maybe_retry_connection(self, future):
        """Xử lý kết quả kết nối, thử lại nếu thất bại."""
        try:
            self.connection = future.result()
            self.log_to_ui(">>> Kết nối thành công! <<<")
        except Exception as e:
            self.log_to_ui(f"Lỗi kết nối: {e}. Thử lại sau 3 giây...")
            # Sử dụng functools.partial để truyền tham số vào call_later
            retry_func = functools.partial(self.connect_and_read)
            self.io_loop.call_later(3, retry_func)

    def on_message(self, message):
        """Xử lý khi nhận được tin nhắn từ server."""
        if message is None:
            self.log_to_ui(">>> Mất kết nối. Đang kết nối lại... <<<")
            self.connect_and_read()
            return

        self.log_to_ui(f"Server gửi: {message}")
        # Lắng nghe tin nhắn tiếp theo (quan trọng đối với tornado)
        if self.connection:
            self.connection.read_message(callback=self.on_message)

class ClientUI(tk.Tk):
    def __init__(self, url):
        super().__init__()
        self.title("WebSocket Client")
        self.geometry("500x400")
        self.url = url
        
        self.ui_queue = queue.Queue()
        self.client_thread = None
        self.websocket_client = None

        self._create_widgets()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.process_ui_queue()

    def _create_widgets(self):
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Vùng hiển thị log
        log_label = ttk.Label(main_frame, text="Log từ Server:")
        log_label.pack(anchor="w")
        self.log_area = scrolledtext.ScrolledText(main_frame, state='disabled', height=15, wrap=tk.WORD)
        self.log_area.pack(fill=tk.BOTH, expand=True, pady=5)

        # Frame chứa các nút điều khiển
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=5)
        
        self.connect_button = ttk.Button(control_frame, text="Kết nối", command=self.start_client)
        self.connect_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

        self.disconnect_button = ttk.Button(control_frame, text="Ngắt kết nối", state='disabled', command=self.stop_client)
        self.disconnect_button.pack(side=tk.LEFT, expand=True, fill=tk.X)
    
    def log(self, message):
        """Hiển thị tin nhắn lên log_area."""
        self.log_area.config(state='normal')
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.config(state='disabled')
        self.log_area.see(tk.END) # Tự động cuộn xuống cuối

    def start_client(self):
        """Bắt đầu luồng client."""
        self.websocket_client = WebSocketClient(self.url, self.ui_queue)
        # Chạy tornado IOLoop trong một luồng riêng
        self.client_thread = threading.Thread(target=self.websocket_client.start, daemon=True)
        self.client_thread.start()
        
        self.connect_button.config(state='disabled')
        self.disconnect_button.config(state='normal')
        self.log(">>> Đã yêu cầu kết nối... <<<")

    def stop_client(self):
        """Dừng luồng client."""
        if self.websocket_client:
            self.websocket_client.stop()
        # Không cần join() vì luồng là daemon, nhưng đảm bảo IOLoop dừng
        self.client_thread = None 
        self.websocket_client = None
        
        self.connect_button.config(state='normal')
        self.disconnect_button.config(state='disabled')
        self.log(">>> Đã yêu cầu ngắt kết nối. <<<")

    def process_ui_queue(self):
        """Kiểm tra hàng đợi và cập nhật UI."""
        try:
            message = self.ui_queue.get_nowait()
            self.log(message)
        except queue.Empty:
            pass
        finally:
            # Lặp lại việc kiểm tra sau 100ms
            self.after(100, self.process_ui_queue)

    def on_closing(self):
        """Xử lý khi người dùng đóng cửa sổ."""
        self.stop_client()
        self.destroy()

if __name__ == "__main__":
    WEBSOCKET_URL = "ws://localhost:8888/websocket/"
    app = ClientUI(WEBSOCKET_URL)
    app.mainloop()