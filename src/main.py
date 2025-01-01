from taipy.gui import Gui, State, download
from assembly_ai.controller import transcribe, summarize, diarization
import io

audio_file = ""
transcript_text = ""

transcript_options = ["Transcribe", "Summarize", "Diarization"]
selected_transcript_option = transcript_options[0]
title = selected_transcript_option


page = """
# Sophisticated Speech-to-Text

<|{selected_transcript_option}|toggle|lov={transcript_options}|on_change=transcript_option_change|>
<|card|
<|title|
<|{title}|>
|>

Load Audio: <|{audio_file}|file_selector|label=Select File|on_action=load_audio_action|extensions=.wav,.mp3|drop_message=Drop Message|>

Transcript:
<|transcript-card|
<|{transcript_text}|text|mode=pre|>
|>

<|{None}|file_download|label=Download File|on_action=download_action|>

|>

"""


def load_audio_action(state):
    if state.selected_transcript_option == "Transcribe":
        state.transcript_text = transcribe(state.audio_file)
    elif state.selected_transcript_option == "Summarize":
        state.transcript_text = summarize(state.audio_file)
    elif state.selected_transcript_option == "Diarization":
        state.transcript_text = diarization(state.audio_file)


def download_action(state):
    if state.transcript_text != "":
        buffer = io.StringIO()
        buffer.write(state.transcript_text)
        download(state, content=bytes(
            buffer.getvalue(), "UTF-8"), name="transcript.txt")


def transcript_option_change(state):
    state.title = state.selected_transcript_option
    state.audio_file = ""
    state.transcript_text = ""


if __name__ == "__main__":
    Gui(page=page).run(page=page, title="Sophisticated Speech-to-Text", host="0.0.0.0", port="10000")
    # gui_service = Gui(page=page)
    # web_app = gui_service.run(title="Sophisticated Speech-to-Text", host="0.0.0.0", port="10000", debug=False, run_server=False)
