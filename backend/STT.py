from google.cloud import speech
import logging

def transcribe_file(speech_file: str) -> speech.RecognizeResponse:
    """Transcribe the given audio file."""
    client = speech.SpeechClient()

    try:
        with open(speech_file, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
            sample_rate_hertz=16000,
            language_code="en-US",
        )

        response = client.recognize(config=config, audio=audio)

        if not response.results:
            logging.error("No results returned from the speech recognition service.")
            return response

        # Each result is for a consecutive portion of the audio. Iterate through
        # them to get the transcripts for the entire audio file.
        # for result in response.results:
        #     # The first alternative is the most likely one for this portion.
        #     print(f"Transcript: {result.alternatives[0].transcript}")

    except Exception as e:
        logging.error(f"An error occurred during speech recognition: {e}")
        raise

    return response.results[0].alternatives[0].transcript
