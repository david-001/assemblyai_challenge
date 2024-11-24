from taipy.gui import Gui, State, download
from assembly_ai.controller import transcribe
import io

audio_file = ""
transcript_text = ""

page = """
# Taipy Transcriber

Load Audio: <|{audio_file}|file_selector|label=Select File|on_action=load_audio_action|extensions=.wav,.mp3|drop_message=Drop Message|>

Transcript:
<|card
<|{transcript_text}|>
|>


<|{None}|file_download|label=Download File|on_action=download_action|>

"""


def load_audio_action(state):
    state.transcript_text = transcribe(state.audio_file)


def download_action(state):
    if state.transcript_text != "":
        buffer = io.StringIO()
        buffer.write(state.transcript_text)
        download(state, content=bytes(
            buffer.getvalue(), "UTF-8"), name="transcript.txt")


if __name__ == "__main__":
    Gui(page=page).run(title="Taipy Transcriber")
