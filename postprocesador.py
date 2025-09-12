import re

def limpiar_transcripcion(texto: str) -> str:
    """
    Post-procesa el texto transcrito:
    - Elimina espacios extra
    - Capitaliza la primera letra
    - Añade un punto al final si falta
    - Inserta comas simples en frases largas
    """
    # Quitar espacios repetidos
    texto = re.sub(r"\s+", " ", texto.strip())

    # Capitalizar primera letra
    if len(texto) > 0:
        texto = texto[0].upper() + texto[1:]

    # Añadir punto final si no existe
    if not texto.endswith((".", "!", "?")):
        texto += "."

    # Inserción de comas básicas: cada ~12 palabras
    palabras = texto.split()
    resultado = []
    for i, palabra in enumerate(palabras, 1):
        resultado.append(palabra)
        if i % 12 == 0 and i != len(palabras):
            resultado.append(",")
    texto = " ".join(resultado)

    return texto
