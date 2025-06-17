# Voice Chat Backend API

A FastAPI-based backend service that converts voice recordings to text using OpenAI's Whisper model and generates AI responses using GPT-4.

## Features

- 🎤 **Voice-to-Text**: Convert audio files to text using OpenAI Whisper
- 🤖 **AI Chat**: Generate intelligent responses using GPT-4
- 📁 **File Upload**: Handle audio file uploads (MP3, WAV, WebM)
- 🔄 **RESTful API**: Simple HTTP endpoints for easy integration
- ⚡ **Fast Processing**: Built with FastAPI for high performance

## Prerequisites

- Python 3.8+
- OpenAI API Key

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd voice-chat-backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Configuration

### Getting OpenAI API Key

1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign in to your account
3. Create a new API key
4. Copy the key to your `.env` file

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

## Usage

### Starting the Server

```bash
# Development mode with auto-reload
uvicorn main:app --reload

# Production mode
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### API Documentation

Once the server is running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## API Endpoints

### POST `/voice-chat/`

Convert audio to text and generate AI response.

**Request:**
- Method: `POST`
- Content-Type: `multipart/form-data`
- Body: Audio file (field name: `audio`)

**Supported Audio Formats:**
- MP3
- WAV
- WebM
- M4A

**Response:**
```json
{
  "question": "What is the weather like today?",
  "response": "I don't have access to real-time weather data..."
}
```

**Error Response:**
```json
