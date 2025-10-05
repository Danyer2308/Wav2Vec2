from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware 
from transformers import pipeline
import soundfile as sf
import tempfile
import os

app = FastAPI(title="API Wav2Vec2 para React")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

asr = pipeline("automatic-speech-recognition", model="jonatasgrosman/wav2vec2-large-xlsr-53-spanish")

@app.post("/transcribir/")
async def transcribir_audio(file: UploadFile = File(...)):
    """
    Recibe un archivo de audio (wav/mp3) desde el frontend y devuelve la transcripción.
    """
    try:

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            contents = await file.read()
            tmp.write(contents)
            tmp_path = tmp.name

        audio, sr = sf.read(tmp_path)

        result = asr({"array": audio, "sampling_rate": sr})
        texto = result["text"]

        os.remove(tmp_path)  

        return JSONResponse(content={"transcripcion": texto})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

