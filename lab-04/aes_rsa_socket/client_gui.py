import tkinter as tk
from tkinter import scrolledtext, messagebox
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading


class SecureChatClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Secure Chat Client")

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, height=20, width=50, state='disabled')
        self.text_area.pack(padx=10, pady=10)

        self.entry = tk.Entry(master, width=40)
        self.entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

        self.send_button = tk.Button(master, text="Send", width=10, command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=(5, 10), pady=(0, 10))

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Network setup
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 12345))

        # RSA key generation
        self.client_key = RSA.generate(2048)

        # Receive server public key
        server_public_key = RSA.import_key(self.client_socket.recv(2048))

        # Send client public key
        self.client_socket.send(self.client_key.publickey().export_key(format='PEM'))

        # Receive encrypted AES key
        encrypted_aes_key = self.client_socket.recv(2048)

        # Decrypt AES key
        cipher_rsa = PKCS1_OAEP.new(self.client_key)
        self.aes_key = cipher_rsa.decrypt(encrypted_aes_key)

        # Start receive thread
        self.running = True
        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()

    def encrypt_message(self, message):
        cipher = AES.new(self.aes_key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
        return cipher.iv + ciphertext

    def decrypt_message(self, encrypted_message):
        iv = encrypted_message[:AES.block_size]
        ciphertext = encrypted_message[AES.block_size:]
        cipher = AES.new(self.aes_key, AES.MODE_CBC, iv)
        decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decrypted_message.decode()

    def receive_messages(self):
        try:
            while self.running:
                encrypted_message = self.client_socket.recv(1024)
                if encrypted_message:
                    message = self.decrypt_message(encrypted_message)
                    self.append_message(f"[Server] {message}")
        except:
            self.append_message("[!] Connection closed.")

    def send_message(self):
        message = self.entry.get()
        if not message:
            return
        try:
            encrypted = self.encrypt_message(message)
            self.client_socket.send(encrypted)
            self.append_message(f"[You] {message}")
            self.entry.delete(0, tk.END)
            if message.lower() == "exit":
                self.running = False
                self.client_socket.close()
                self.master.quit()
        except Exception as e:
            messagebox.showerror("Send Error", str(e))

    def append_message(self, message):
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, message + '\n')
        self.text_area.yview(tk.END)
        self.text_area.config(state='disabled')

    def on_closing(self):
        try:
            self.send_message()  # send exit
        except:
            pass
        self.running = False
        self.client_socket.close()
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = SecureChatClient(root)
    root.mainloop()
