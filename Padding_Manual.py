def aplicar_padding(datos: bytes, block_size: int) -> bytes:
    
    padding_len = block_size - (len(datos) % block_size)
    padding = bytes([padding_len] * padding_len)
    return datos + padding


def remover_padding(datos: bytes) -> bytes:
    
    padding_len = datos[-1]

    # Validación básica
    if padding_len < 1 or padding_len > len(datos):
        raise ValueError("Padding inválido")

    return datos[:-padding_len]



def cifrar(mensaje: str, clave: str, block_size: int = 16) -> bytes:
    
    mensaje_bytes = mensaje.encode()
    clave_bytes = clave.encode()

    # Aplicar padding
    mensaje_padded = aplicar_padding(mensaje_bytes, block_size)

    ciphertext = bytearray()

    for i in range(len(mensaje_padded)):
        k = clave_bytes[i % len(clave_bytes)]
        ciphertext.append(mensaje_padded[i] ^ k)

    return bytes(ciphertext)


def descifrar(ciphertext: bytes, clave: str, block_size: int = 16) -> str:
    
    clave_bytes = clave.encode()

    plaintext_padded = bytearray()

    for i in range(len(ciphertext)):
        k = clave_bytes[i % len(clave_bytes)]
        plaintext_padded.append(ciphertext[i] ^ k)

    # Remover padding
    plaintext = remover_padding(bytes(plaintext_padded))

    return plaintext.decode()



mensaje = "Implementacion de padding manual"
clave = "clave_segura"

print("Mensaje original:", mensaje)

cipher = cifrar(mensaje, clave)
print("Ciphertext:", cipher)

plain = descifrar(cipher, clave)
print("Mensaje descifrado:", plain)