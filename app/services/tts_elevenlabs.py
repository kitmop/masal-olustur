import os
from elevenlabs.client import ElevenLabs
from elevenlabs import stream
from dotenv import load_dotenv

load_dotenv()
elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")

elevenlabs = ElevenLabs(
    api_key = elevenlabs_api_key
)

def stream_audio(text: str, voice_id: str = "PdYVUd1CAGSXsTvZZTNn", model_id: str = "eleven_multilingual_v1", output_format: str = "mp3_22050_32"):
    """
    ElevenLabs TTS için streaming audio generator döner.
    """
    return elevenlabs.text_to_speech.convert(
        voice_id=voice_id,
        text=text,
        model_id=model_id,
        output_format=output_format
    )