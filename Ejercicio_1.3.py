from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

from Avances.Generacion_Llaves import key_aes

from PIL import Image
import numpy as np


INPUT_IMAGE = "pic.png"
BLOCK_SIZE = 16


def encrypt_pixels(mode: str):

    KEY = key_aes(256)

    img = Image.open(INPUT_IMAGE)
    img = img.convert("RGB")

    pixel_array = np.array(img)
    pixel_bytes = pixel_array.tobytes()

    padded = pad(pixel_bytes, BLOCK_SIZE)

    if mode == "ECB":
        cipher = AES.new(KEY, AES.MODE_ECB)
        encrypted = cipher.encrypt(padded)

    elif mode == "CBC":
        iv = get_random_bytes(16)
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(padded)

        print("IV CBC:", iv.hex())

    else:
        raise ValueError("Modo no soportado")

    # Cortar padding extra para reconstrucción visual
    encrypted = encrypted[:len(pixel_bytes)]

    encrypted_array = np.frombuffer(encrypted, dtype=np.uint8)
    encrypted_array = encrypted_array.reshape(pixel_array.shape)

    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(f"pic_{mode}.png")

    print(f"Imagen cifrada en modo {mode} guardada.")


if __name__ == "__main__":
    encrypt_pixels("ECB")
    encrypt_pixels("CBC")