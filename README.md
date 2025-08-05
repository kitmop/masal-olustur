# Masal Oluştur (Story Generator for Children)

**Masal Oluştur** is a lightweight, API-based backend that generates personalized children's stories using LLMs (Large Language Models) and converts them into audio using ElevenLabs TTS. It is designed as a minimal MVP to experiment with prompt engineering, FastAPI backend development, and voice synthesis integration.

## ✨ Features

- Custom story generation based on user inputs (e.g., character, setting, theme)
- LLM integration via OpenAI API (GPT-4)
- Structured prompt engineering for consistent tone and age-appropriate language
- ElevenLabs TTS (Text-to-Speech) support for audio generation
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
```

### Set your API keys

Create a `.env` file in the project root and add the following:

```env
OPENAI_API_KEY=your_openai_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

Make sure your code includes:

```python
from dotenv import load_dotenv
load_dotenv()
```

### Run the server

```bash
uvicorn main:app --reload
```

## 📁 Project Structure

```
masal-olustur/
├── main.py             # FastAPI app and endpoints
├── prompts.py          # Prompt templates
├── tts.py              # ElevenLabs TTS integration
├── schemas.py          # Pydantic models
├── utils.py            # Helper functions
├── requirements.txt
└── README.md
```

## 🧠 Motivation

This project was built to:
- Explore practical LLM prompt engineering
- Integrate external APIs (OpenAI, ElevenLabs)
- Build a deployable backend for creative applications
- Practice clean and modular Python backend design

## 👤 Author

Fatih Mustafa Tuğlu  
MSc Student @ TUM – Robotics & Computer Vision  
GitHub: [kitmop](https://github.com/kitmop)
