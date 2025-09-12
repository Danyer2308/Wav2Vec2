from transformers import pipeline
from config import MODELO
from postprocesador import limpiar_transcripcion

def transcribir(archivo):
    print("📝 Transcribiendo con Wav2Vec2...")
    asr = pipeline("automatic-speech-recognition", model=MODELO)

    result = asr(archivo)
    texto = result["text"]

    # 🔹 Aplicar post-procesador
    texto_limpio = limpiar_transcripcion(texto)

    print("\nTexto transcrito:")
    print("RAW  :", texto)
    print("LIMPIO:", texto_limpio)

    with open("transcripcion.txt", "w", encoding="utf-8") as f:
        f.write(texto_limpio)

    print("📄 Transcripción guardada en transcripcion.txt")
    return texto_limpio

