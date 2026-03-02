from Crypto.Cipher import DES
from Avances.Generacion_Llaves import key_des
from Avances.Padding_Manual import aplicar_padding, remover_padding


BLOCK_SIZE = 8  # DES usa bloques de 8 bytes


def cifrar_des_ecb(mensaje: str, clave: bytes) -> bytes:
    cipher = DES.new(clave, DES.MODE_ECB)

    mensaje_bytes = mensaje.encode("utf-8")
    mensaje_padded = aplicar_padding(mensaje_bytes, BLOCK_SIZE)

    ciphertext = cipher.encrypt(mensaje_padded)
    return ciphertext


def descifrar_des_ecb(ciphertext: bytes, clave: bytes) -> str:
    cipher = DES.new(clave, DES.MODE_ECB)

    plaintext_padded = cipher.decrypt(ciphertext)
    plaintext = remover_padding(plaintext_padded)

    return plaintext.decode("utf-8")


if __name__ == "__main__":

    clave = key_des()
    print("Clave DES:", clave.hex())

    mensaje = "Implementacion DES ECB con PKCS7 manual"
    print("Mensaje original:", mensaje)

    ciphertext = cifrar_des_ecb(mensaje, clave)
    print("Ciphertext (hex):", ciphertext.hex())

    mensaje_descifrado = descifrar_des_ecb(ciphertext, clave)
    print("Mensaje descifrado:", mensaje_descifrado)

    if mensaje == mensaje_descifrado:
        print("El mensaje se recuperó correctamente.")
    else:
        print("Error en el descifrado.")