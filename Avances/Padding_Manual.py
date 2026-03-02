def aplicar_padding(datos: bytes, block_size: int) -> bytes:
    padding_len = block_size - (len(datos) % block_size)
    padding = bytes([padding_len] * padding_len)
    return datos + padding


def remover_padding(datos: bytes) -> bytes:
    padding_len = datos[-1]

    if padding_len < 1 or padding_len > len(datos):
        raise ValueError("Padding inválido")

    return datos[:-padding_len]