from google.cloud import texttospeech
from google.cloud import storage
import os

# Initialize Google Cloud Storage client

def make_sound(text: str):
    storage_client = storage.Client()

    bucket_name = 'toyota-ai'
    bucket = storage_client.bucket(bucket_name)
# Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    filename = "output.mp3"
    # The response's audio_content is binary.
    with open(filename, "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)

    # Make the blob publicly readable (if necessary)
    blob.make_public()

    # The public URL can be used to directly access the file via HTTP.
    mp3_url = blob.public_url

    # Optionally, delete the local file after upload
    os.remove(filename)

    return mp3_url
    