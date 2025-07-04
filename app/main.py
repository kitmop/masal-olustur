import os
from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import StreamingResponse, HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from app.schemas import StoryRequest
from app.prompts import create_prompt
from services.openai_client import generate_story_from_prompt
from services.tts_elevenlabs import stream_audio

import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def index():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.post("/generate-story")
def generate_story(request: StoryRequest):
    prompt = create_prompt(
        karakter=request.karakter,
        tema=request.tema,
        yas=request.yas,
        mekan=request.mekan,
        ders=request.ders,
        uzunluk=request.uzunluk
    )
    story = generate_story_from_prompt(prompt)
    return {
        "masal": story
    }


@app.post("/tts/")
async def tts_endpoint(text: str = Form(...)):
    try:
        logger.info("End pointin içindeyiz.")
        audio_generator = stream_audio(text)
        #return StreamingResponse(audio_generator, media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

