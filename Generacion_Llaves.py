import secrets

def key_des() -> bytes:
    return secrets.token_bytes(8)

def key_3des() -> bytes:
    return secrets.token_bytes(24)

def key_aes(bits: int = 256) -> bytes:
    if bits not in (128, 192, 256):
        raise ValueError("AES bits debe ser 128, 192 o 256")
    return secrets.token_bytes(bits // 8)

k_des  = key_des()
k_3des = key_3des()
k_aes  = key_aes(256)

print("DES :", k_des.hex(),  len(k_des))
print("3DES:", k_3des.hex(), len(k_3des))
print("AES :", k_aes.hex(),  len(k_aes))