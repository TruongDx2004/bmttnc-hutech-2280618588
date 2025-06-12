import tkinter as tk
from tkinter import ttk, messagebox
import hashlib
from Crypto.Hash import SHA3_256
from hashlib import blake2b

# Custom simple MD5 implementation
def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def simple_md5(message):
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476
    original_length = len(message)
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += original_length.to_bytes(8, 'little')

    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]
        a0, b0, c0, d0 = a, b, c, d

        for j in range(64):
            if j < 16:
                f = (b & c) | ((~b) & d)
                g = j
            elif j < 32:
                f = (d & b) | ((~d) & c)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            else:
                f = c ^ (b | (~d))
                g = (7 * j) % 16

            temp = d
            d = c
            c = b
            b = (b + left_rotate((a + f + 0x5A827999 + words[g]) & 0xFFFFFFFF, 3)) & 0xFFFFFFFF
            a = temp

        a = (a + a0) & 0xFFFFFFFF
        b = (b + b0) & 0xFFFFFFFF
        c = (c + c0) & 0xFFFFFFFF
        d = (d + d0) & 0xFFFFFFFF

    return '{:08x}{:08x}{:08x}{:08x}'.format(a, b, c, d)

# Hashing methods
def calculate_md5(input_str):
    return hashlib.md5(input_str.encode()).hexdigest()

def calculate_sha256(input_str):
    return hashlib.sha256(input_str.encode()).hexdigest()

def calculate_sha3(input_str):
    h = SHA3_256.new()
    h.update(input_str.encode())
    return h.hexdigest()

def calculate_blake2(input_str):
    h = blake2b(digest_size=64)
    h.update(input_str.encode())
    return h.hexdigest()

def run_hash():
    text = entry.get()
    if not text:
        messagebox.showwarning("Lỗi", "Vui lòng nhập chuỗi cần băm.")
        return

    method = algorithm.get()
    if method == "Simple MD5":
        result.set(simple_md5(text.encode()))
    elif method == "MD5":
        result.set(calculate_md5(text))
    elif method == "SHA-256":
        result.set(calculate_sha256(text))
    elif method == "SHA-3":
        result.set(calculate_sha3(text))
    elif method == "BLAKE2":
        result.set(calculate_blake2(text))

# UI Setup
root = tk.Tk()
root.title("Hash Algorithms GUI")

tk.Label(root, text="Nhập chuỗi:").pack(pady=(10, 0))
entry = tk.Entry(root, width=60)
entry.pack(pady=5)

tk.Label(root, text="Chọn thuật toán:").pack()
algorithm = ttk.Combobox(root, values=["Simple MD5", "MD5", "SHA-256", "SHA-3", "BLAKE2"])
algorithm.set("MD5")
algorithm.pack(pady=5)

tk.Button(root, text="Băm", command=run_hash).pack(pady=10)

result = tk.StringVar()
tk.Label(root, text="Kết quả băm:").pack()
tk.Entry(root, textvariable=result, width=80).pack(pady=5)

root.mainloop()
