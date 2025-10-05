
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

✅ Con esto tienes un sistema completo de **grabación + transcripción + limpieza automática** en español.  

---

# 🎙️ API de Transcripción de Voz a Texto (Wav2Vec2 + FastAPI)

## 📘 Descripción general

Esta API convierte **audio en texto en español** utilizando el modelo de inteligencia artificial **Wav2Vec2** de Hugging Face.  
Permite recibir un archivo de audio desde el **frontend (React)** o herramientas como **Postman**, procesarlo y devolver la transcripción en formato JSON.

---

## ⚙️ Requisitos previos

### 🔹 Sistema
- **Python 3.9 o superior**
- **pip** actualizado
- **ffmpeg** instalado y disponible en el PATH (necesario para leer archivos de audio)
  - Windows: descargar desde [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
  - Linux: `sudo apt install ffmpeg`
  - macOS: `brew install ffmpeg`

### 🔹 Librerías de Python necesarias

Instala todas las dependencias ejecutando:

```bash
pip install fastapi uvicorn transformers torch soundfile python-multipart
```

> 💡 Estas librerías cubren todo lo necesario para ejecutar la API.

---

## 🚀 Ejecución del servidor

Ejecuta el servidor desde la terminal con:

```bash
uvicorn api_transcribir_archivo:app --reload
```

Por defecto, la API se ejecutará en:

```
http://127.0.0.1:8000
```

---

## 🧩 Endpoints disponibles

### **POST /transcribir/**

**Descripción:**  
Recibe un archivo de audio en formato `.wav` o `.mp3` y devuelve la transcripción de voz a texto.

**Tipo de cuerpo (body):** `multipart/form-data`

| Campo | Tipo | Requerido | Descripción |
|--------|------|-----------|--------------|
| `file` | Archivo (`.wav` / `.mp3`) | ✅ | Archivo de audio a transcribir |

**Ejemplo de respuesta exitosa (HTTP 200):**
```json
{
  "transcripcion": "hola este es un ejemplo de prueba"
}
```

**Ejemplo de error (HTTP 500):**
```json
{
  "error": "ffmpeg not found"
}
```

---

## 🧪 Cómo probar la API

### 🔹 Opción 1: Usando Swagger UI
Abre en el navegador:
```
http://127.0.0.1:8000/docs
```
1. Busca el endpoint `/transcribir/`
2. Haz clic en **“Try it out”**
3. Sube un archivo `.wav` o `.mp3`
4. Pulsa **“Execute”**
5. Verás el texto transcrito en la respuesta.

---

### 🔹 Opción 2: Usando Postman
1. Crea una nueva petición **POST**
2. URL:
   ```
   http://127.0.0.1:8000/transcribir/
   ```
3. En la pestaña **Body**, selecciona:
   - **form-data**
   - **Key:** `file`
   - **Type:** *File*
   - **Value:** selecciona tu archivo `.wav`
4. Envía la petición
5. En la respuesta aparecerá la transcripción en JSON.

---

### 🔹 Opción 3: Desde una app React

El frontend puede usar la API nativa del navegador (`MediaRecorder`) para grabar audio y enviarlo con `fetch()` al backend.

La API espera exactamente un archivo en formato **FormData**, con el campo llamado `"file"`.

---

## 🔄 Flujo general del sistema

| Etapa | Acción | Tecnología |
|--------|--------|------------|
| 🎙️ 1. Grabación | El usuario graba su voz desde el navegador | React / MediaRecorder |
| 📤 2. Envío | React envía el archivo al backend | HTTP POST `/transcribir/` |
| 🧠 3. Procesamiento | FastAPI usa Wav2Vec2 para convertir voz a texto | Python + Transformers |
| 💬 4. Respuesta | La API devuelve la transcripción en formato JSON | FastAPI |
| 🖥️ 5. Visualización | React muestra el texto en pantalla | Frontend |

