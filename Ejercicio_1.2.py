from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad

from Avances.Generacion_Llaves import key_3des

import secrets


BLOCK_SIZE = 8 


def generar_iv() -> bytes:
    return secrets.token_bytes(BLOCK_SIZE)


def ajustar_clave_paridad(clave: bytes) -> bytes:
    """
    DES3 requiere bits de paridad correctos.
    """
    return DES3.adjust_key_parity(clave)


def cifrar_3des_cbc(mensaje: str, clave: bytes):
    iv = generar_iv()

    cipher = DES3.new(clave, DES3.MODE_CBC, iv)

    mensaje_bytes = mensaje.encode("utf-8")
    mensaje_padded = pad(mensaje_bytes, BLOCK_SIZE)

    ciphertext = cipher.encrypt(mensaje_padded)

    return iv, ciphertext


def descifrar_3des_cbc(ciphertext: bytes, clave: bytes, iv: bytes) -> str:
    cipher = DES3.new(clave, DES3.MODE_CBC, iv)

    mensaje_padded = cipher.decrypt(ciphertext)
    mensaje = unpad(mensaje_padded, BLOCK_SIZE)

    return mensaje.decode("utf-8")


if __name__ == "__main__":
    clave_raw = key_3des(192)
    clave = ajustar_clave_paridad(clave_raw)

    mensaje = "Cifrado 3DES en modo CBC correctamente implementado"

    print("Mensaje original:", mensaje)
    print("Clave (hex):", clave.hex())

    iv, ciphertext = cifrar_3des_cbc(mensaje, clave)

    print("IV:", iv.hex())
    print("Ciphertext:", ciphertext.hex())

    mensaje_descifrado = descifrar_3des_cbc(ciphertext, clave, iv)

    print("Mensaje descifrado:", mensaje_descifrado)

    if mensaje == mensaje_descifrado:
        print("Validación correcta")
    else:
        print("Error en descifrado")