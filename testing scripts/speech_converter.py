import os
from load_keys import load_env
from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)

load_env()

speech_api = os.getenv('DEEPGRAM_API_KEY')
AUDIO_FILE = './testing scripts/recordings/recording0.wav'


def speech_to_text():
    try:
        # STEP 1 Create a Deepgram client using the API key
        deepgram = DeepgramClient(speech_api)

        with open(AUDIO_FILE, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        #STEP 2: Configure Deepgram options for audio analysis
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
        )

        # STEP 3: Call the transcribe_file method with the text payload and options
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)

        # STEP 4: Print the response
        transcript = response["results"]["channels"][0]["alternatives"][0]["transcript"]

        return transcript

    except Exception as e:
        return (f"Exception: {e}")