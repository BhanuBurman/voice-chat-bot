from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import openai
import os
import tempfile
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Verify API key is loaded
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is required")

# Use the new Client instance
client = openai.OpenAI(api_key=api_key)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/voice-chat/")
async def voice_chat(audio: UploadFile = File(...)):
    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            tmp.write(await audio.read())
            tmp_path = tmp.name

        # Transcribe audio
        with open(tmp_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )

        question = transcription.text

        # Get chat completion
        chat_completion = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": question}]
        )

        # Clean up temporary file
        os.unlink(tmp_path)

        return {
            "question": question,
            "response": chat_completion.choices[0].message.content
        }

    except Exception as e:
        # Clean up temporary file in case of error
        if 'tmp_path' in locals():
            try:
                os.unlink(tmp_path)
            except:
                pass

        return {"error": str(e)}


@app.get("/")
async def root():
    return {"message": "Voice Chat API is running"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)