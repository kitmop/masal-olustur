import os
from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import StreamingResponse, HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from app.schemas import StoryRequest
from app.prompts import create_prompt
from services.openai_client import generate_story_from_prompt
from services.tts_elevenlabs import stream_audio

app = FastAPI(title = "Masal Oluştur", version="1.0")

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get('/', response_class=HTMLResponse)
def root():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    static_path = os.path.join(current_dir, "../static/index.html")

    with open(static_path, "r", encoding="utf-8") as f:
        return f.read()

@app.get("/read-story", response_model=dict)
def read_story():
    return {"message": "Masal burada!"}


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
        audio_generator = stream_audio(text)
        return StreamingResponse(audio_generator, media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

