import os
from elevenlabs.client import ElevenLabs
from elevenlabs import stream
from dotenv import load_dotenv
import logging

load_dotenv()
elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


elevenlabs = ElevenLabs(
    api_key = elevenlabs_api_key
)

def stream_audio(text: str):
    logging.info("içeri giriyor.")
    """return elevenlabs.text_to_speech.convert(
        voice_id="PdYVUd1CAGSXsTvZZTNn",
        text=text,
        model_id="eleven_multilingual_v2",
        output_format="mp3_22050_32"
    )"""