import assemblyai as aai
from dotenv import load_dotenv
import os
import re

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


def summarize(audio_file):
    transcriber = aai.Transcriber()
    try:
        # Step 1: Transcribe an audio file.
        transcript = transcriber.transcribe(audio_file)
        # # Step 2: Define a summarization prompt.
        prompt = "Provide a brief summary of the transcript."
        # Step 3: Apply LeMUR.
        result = transcript.lemur.task(
            prompt, final_model=aai.LemurModel.claude3_5_sonnet
        )
        return result.response
    except:
        print(f"Summarization failed")


def diarization(audio_file):
    config = aai.TranscriptionConfig(
        speaker_labels=True,
    )

    try:
        transcript = aai.Transcriber().transcribe(audio_file, config)
        response = ""
        for utterance in transcript.utterances:
            response += (f"Speaker {utterance.speaker}: {utterance.text} \n")
        return response
    except:
        print(f"Diarization failed")


def count_words(text):
    # Use regex to find all words (ignores punctuation)
    words = re.findall(r'\b\w+\b', text)

    # Count the number of words
    word_count = len(words)
    return word_count
