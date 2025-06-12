# aes_utils.py
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

AES_KEY = get_random_bytes(16)  # Khóa bí mật (AES-128)

def encrypt_message(key: bytes, message: str) -> str:
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + ct_bytes).decode()

def decrypt_message(key: bytes, encrypted: str) -> str:
    raw = base64.b64decode(encrypted)
    iv = raw[:AES.block_size]
    ct = raw[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()
