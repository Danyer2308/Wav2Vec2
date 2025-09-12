from audio import grabar_y_guardar
from transcripcion import transcribir

if __name__ == "__main__":
    archivo = grabar_y_guardar()
    transcribir(archivo)