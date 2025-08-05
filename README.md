# Masal Oluştur (Story Generator for Children)

Masal Oluştur is a lightweight, API-based backend that generates personalized children's stories using LLMs (Large Language Models). It is designed as a minimal MVP to experiment with prompt engineering, FastAPI backend development, and voice synthesis integration.

## ✨ Features

- Custom story generation based on user inputs (e.g., character, setting, theme)
- LLM integration via OpenAI API (GPT-4)
- Structured prompt engineering for consistent tone and age-appropriate language
- Planned support for ElevenLabs TTS (Text-to-Speech)
- Deployed on Railway for rapid access and testing

## 🔧 Tech Stack

- **Python**
- **FastAPI** – Lightweight, async Python backend
- **OpenAI API** – For text generation
- **ElevenLabs API** – For audio generation
- **Railway** – Deployment platform

## 📦 Setup & Run

```bash
# Clone the repo
git clone https://github.com/kitmop/masal-olustur.git
cd masal-olustur

# Create environment
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set your OpenAI API key
OPENAI_API_KEY=your_openai_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key

# Run the server
uvicorn main:app --reload