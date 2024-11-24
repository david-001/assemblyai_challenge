import assemblyai as aai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
assemblyai_api_key = os.getenv("AssemblyAI_API_KEY")

# Configure AssemblyAI
aai.settings.api_key = assemblyai_api_key
transcriber = aai.Transcriber()
config = aai.TranscriptionConfig(speaker_labels=True)


def transcribe(audio_file):
    transcriber = aai.Transcriber()
    try:
        transcript = transcriber.transcribe(audio_file)
        if transcript.status == aai.TranscriptStatus.error:
            print(transcript.error)
        else:
            return transcript.text
    except:
        print(f"Transcription failed: {transcript.error}")
