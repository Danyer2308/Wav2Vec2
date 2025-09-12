import sounddevice as sd
import soundfile as sf
import numpy as np
import threading
from config import FRECUENCIA, ARCHIVO

grabando = True
frames = []

def grabar():
    global frames, grabando
    print("🎙️ Grabando... Presiona ENTER para detener.")

    def callback(indata, frames_count, time, status):
        if status:
            print(status)
        frames.append(indata.copy())

    with sd.InputStream(samplerate=FRECUENCIA, channels=1, callback=callback):
        while grabando:
            sd.sleep(100)

def detener():
    global grabando
    input()  # Espera a que presiones Enter
    grabando = False
    print("⏹️ Grabación detenida.")

def guardar():
    global frames
    audio = np.concatenate(frames, axis=0)
    sf.write(ARCHIVO, audio, FRECUENCIA)
    print(f"✅ Audio guardado en {ARCHIVO}")
    return ARCHIVO

def grabar_y_guardar():
    t1 = threading.Thread(target=grabar)
    t2 = threading.Thread(target=detener)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    return guardar()
