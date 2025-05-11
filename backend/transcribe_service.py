import os
from pydub import AudioSegment
import azure.cognitiveservices.speech as speechsdk
from config import AZURE_COG_ENDPOINT, AZURE_COG_KEY

def transcribe(audio_path):
    # Convert webm to wav (Azure doesn't support webm directly)
    base = os.path.splitext(audio_path)[0]
    wav_path = f"{base}.wav"
    audio = AudioSegment.from_file(audio_path)
    audio.export(wav_path, format="wav")

    speech_config = speechsdk.SpeechConfig(
        subscription=AZURE_COG_KEY,
        endpoint=AZURE_COG_ENDPOINT
    )
    audio_config = speechsdk.audio.AudioConfig(filename=wav_path)
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    result = recognizer.recognize_once()

    return result.text if result.reason == speechsdk.ResultReason.RecognizedSpeech else ""