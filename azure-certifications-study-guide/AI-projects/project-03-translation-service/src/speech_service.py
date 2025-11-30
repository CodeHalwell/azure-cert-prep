"""
Azure Speech service wrapper.
"""

import azure.cognitiveservices.speech as speechsdk
from config import settings


class SpeechService:
    """Azure Speech service client."""

    def __init__(self):
        self.speech_config = speechsdk.SpeechConfig(
            subscription=settings.speech_key,
            region=settings.speech_region,
        )

    def speech_to_text(self, audio_data: bytes, language: str = "en-US") -> str:
        """
        Convert speech audio to text.

        Args:
            audio_data: Audio bytes (WAV format)
            language: Recognition language

        Returns:
            Transcribed text
        """
        self.speech_config.speech_recognition_language = language

        # Create audio stream from bytes
        audio_stream = speechsdk.audio.PushAudioInputStream()
        audio_stream.write(audio_data)
        audio_stream.close()

        audio_config = speechsdk.audio.AudioConfig(stream=audio_stream)
        recognizer = speechsdk.SpeechRecognizer(
            speech_config=self.speech_config,
            audio_config=audio_config,
        )

        result = recognizer.recognize_once()

        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return result.text
        elif result.reason == speechsdk.ResultReason.NoMatch:
            raise ValueError("Speech could not be recognized")
        else:
            raise RuntimeError(f"Speech recognition failed: {result.reason}")

    def text_to_speech(
        self, text: str, language: str = "en-US", voice: str = None
    ) -> bytes:
        """
        Convert text to speech audio.

        Args:
            text: Text to synthesize
            language: Output language
            voice: Voice name (optional)

        Returns:
            Audio bytes (WAV format)
        """
        self.speech_config.speech_synthesis_language = language

        if voice:
            self.speech_config.speech_synthesis_voice_name = voice

        # Use in-memory audio output
        synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=self.speech_config,
            audio_config=None,  # Return audio data instead of playing
        )

        result = synthesizer.speak_text(text)

        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            return result.audio_data
        else:
            raise RuntimeError(f"Speech synthesis failed: {result.reason}")

    def get_voices(self, language: str = None) -> list[dict]:
        """
        Get available voices.

        Args:
            language: Filter by language (optional)

        Returns:
            List of voice information
        """
        synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=self.speech_config,
            audio_config=None,
        )

        result = synthesizer.get_voices_async(language).get()

        voices = []
        for voice in result.voices:
            voices.append({
                "name": voice.name,
                "display_name": voice.local_name,
                "language": voice.locale,
                "gender": voice.gender.name,
            })

        return voices


speech_service = SpeechService()
