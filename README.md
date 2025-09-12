
# 🎙️ Wav2Vec2

Este proyecto permite **grabar audio desde el micrófono**, transcribirlo automáticamente a texto en español usando **Wav2Vec2**, y guardar el resultado en un archivo de texto.

---

## 🚀 Requisitos previos
- Python 3.9+ (probado en Python 3.11)
- Visual Studio Code (u otro editor de Python)
- Micrófono funcional

---

## 📦 Instalación de dependencias

### 🔹 Librerías principales
```bash
pip install torch transformers sounddevice soundfile librosa
```

### 🔹 Dependencias opcionales (mejor calidad de transcripción)
```bash
pip install pyctcdecode
pip install https://github.com/kpu/kenlm/archive/master.zip
```

### 🔹 ffmpeg
Wav2Vec2 requiere `ffmpeg` para leer audio.

- **Windows**: Descargar desde [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)  
  y agregar `C:\ffmpeg\bin` al **PATH**.  
- **Linux**:
  ```bash
  sudo apt install ffmpeg
  ```
- **MacOS**:
  ```bash
  brew install ffmpeg
  ```

Verificar instalación con:
```bash
ffmpeg -version
```

---

## 📂 Estructura del proyecto

```
proyecto_asr/
│── main.py             # Punto de entrada
│── grabador.py         # Lógica de grabación
│── transcriptor.py     # Transcripción con Wav2Vec2
│── postprocesador.py   # Limpieza del texto transcrito
│── config.py           # Configuración general
│── transcripcion.txt   # Último resultado guardado
│── grabacion.wav       # Última grabación
```

---

## ▶️ Uso

Ejecutar:

```bash
python main.py
```

1. El programa comienza a grabar 🎙️  
2. Presiona **Enter** para detener ⏹️  
3. Se guarda `grabacion.wav`  
4. Se transcribe con Wav2Vec2  
5. Se aplica el **post-procesador**  
6. El texto final se muestra en consola y se guarda en `transcripcion.txt`  

---

## 📚 Librerías usadas

| Librería        | Uso |
|-----------------|-----|
| **torch**       | Backend deep learning |
| **transformers**| Modelos Hugging Face (Wav2Vec2) |
| **sounddevice** | Grabación desde micrófono |
| **soundfile**   | Guardar/leer `.wav` |
| **librosa**     | Procesamiento de audio (resampleo) |
| **ffmpeg**      | Decodificación de audio |
| **pyctcdecode** | (Opcional) Mejor decodificación |
| **kenlm**       | (Opcional) Modelo de lenguaje |

---

## ✨ Post-procesador de texto

Archivo: `postprocesador.py`

```python
import re

def limpiar_transcripcion(texto: str) -> str:
    texto = re.sub(r"\s+", " ", texto.strip())
    if len(texto) > 0:
        texto = texto[0].upper() + texto[1:]
    if not texto.endswith((".", "!", "?")):
        texto += "."
    palabras = texto.split()
    resultado = []
    for i, palabra in enumerate(palabras, 1):
        resultado.append(palabra)
        if i % 12 == 0 and i != len(palabras):
            resultado.append(",")
    return " ".join(resultado)
```

Integración en `transcriptor.py`:

```python
from postprocesador import limpiar_transcripcion

texto_limpio = limpiar_transcripcion(result["text"])
```

---

✅ Con esto tienes un sistema completo de **grabación + transcripción + limpieza automática** en español.  
