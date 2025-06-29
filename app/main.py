from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from .schemas import StoryRequest
from .prompts import create_prompt
from .services.openai_client import generate_story_from_prompt
from .services.tts_elevenlabs import stream_audio

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get('/', response_class=HTMLResponse)
def root():
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
        audio_generator = stream_audio(text)
        return StreamingResponse(audio_generator, media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))