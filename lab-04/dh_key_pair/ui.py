import tkinter as tk
from tkinter import messagebox, scrolledtext
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class DHApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diffie-Hellman Key Exchange")

        self.text_area = scrolledtext.ScrolledText(root, width=100, height=25)
        self.text_area.pack(padx=10, pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.server_button = tk.Button(self.button_frame, text="Start Server", command=self.run_server)
        self.server_button.grid(row=0, column=0, padx=10)

        self.client_button = tk.Button(self.button_frame, text="Start Client", command=self.run_client)
        self.client_button.grid(row=0, column=1, padx=10)

        # Biến lưu
        self.parameters = None
        self.server_private_key = None
        self.server_public_key = None
        self.client_private_key = None
        self.client_public_key = None
        self.shared_key = None

    def log(self, msg):
        self.text_area.insert(tk.END, msg + "\n")
        self.text_area.see(tk.END)

    def run_server(self):
        self.parameters = dh.generate_parameters(generator=2, key_size=2048)
        self.server_private_key = self.parameters.generate_private_key()
        self.server_public_key = self.server_private_key.public_key()

        self.log("[Server] Generated DH parameters and key pair.")
        pem = self.server_public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open("server_public_key.pem", "wb") as f:
            f.write(pem)
        self.log("[Server] Public key saved to 'server_public_key.pem'.")

    def run_client(self):
        try:
            with open("server_public_key.pem", "rb") as f:
                server_pub = serialization.load_pem_public_key(f.read(), backend=default_backend())
        except FileNotFoundError:
            messagebox.showerror("Error", "Public key not found. Run Server first.")
            return

        self.parameters = server_pub.parameters()
        self.client_private_key = self.parameters.generate_private_key()
        self.client_public_key = self.client_private_key.public_key()

        self.log("[Client] Generated key pair using server's parameters.")

        # Tính shared key
        self.shared_key = self.client_private_key.exchange(server_pub)
        self.log("[Client] Shared secret computed successfully.")
        self.log("Shared Secret (hex):")
        self.log(self.shared_key.hex())


if __name__ == "__main__":
    root = tk.Tk()
    app = DHApp(root)
    root.mainloop()
