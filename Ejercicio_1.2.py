from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
import secrets

def generar_clave_3des(longitud=24):
    if longitud not in (16, 24):
        raise ValueError("La clave debe ser de 16 o 24 bytes")
    
    while True:
        clave = secrets.token_bytes(longitud)
        try:
            
            clave_ajustada = DES3.adjust_key_parity(clave)
            DES3.new(clave_ajustada, DES3.MODE_CBC)  
            return clave_ajustada
        except ValueError:
           
            continue


def generar_iv():
    return secrets.token_bytes(8)

def cifrar_3des(mensaje: str, clave: bytes):
    
    iv = generar_iv()
    
    cipher = DES3.new(clave, DES3.MODE_CBC, iv)
    
    mensaje_bytes = mensaje.encode()
    
    mensaje_padded = pad(mensaje_bytes, DES3.block_size)
    
    ciphertext = cipher.encrypt(mensaje_padded)
    
    return iv, ciphertext


def descifrar_3des(ciphertext: bytes, clave: bytes, iv: bytes):
    
    cipher = DES3.new(clave, DES3.MODE_CBC, iv)
    
    mensaje_padded = cipher.decrypt(ciphertext)
    
    mensaje = unpad(mensaje_padded, DES3.block_size)
    
    return mensaje.decode()


clave = generar_clave_3des(24)

mensaje = "Cifrado 3DES en modo CBC correctamente implementado"

print("Mensaje original:", mensaje)

iv, cifrado = cifrar_3des(mensaje, clave)

print("IV:", iv.hex())
print("Ciphertext:", cifrado.hex())

mensaje_descifrado = descifrar_3des(cifrado, clave, iv)

print("Mensaje descifrado:", mensaje_descifrado)