# Lab 08: Speech Services – Transcription and Synthesis

## 🎯 Lab Goal

Use Azure AI Speech to:

- Transcribe audio to text (speech‑to‑text)
- Synthesize text to speech (text‑to‑speech)

---

## ✅ Prerequisites

- Azure AI Services (Speech enabled)
- Microphone access (optional but useful)
- Python 3.9+ with Speech SDK:

```bash
pip install azure-cognitiveservices-speech python-dotenv
```

---

## Step 1 – Configure Environment

Update `.env`:

```env
AZURE_SPEECH_KEY=<your-speech-key>
AZURE_SPEECH_REGION=<your-region>
```

---

## Step 2 – Transcribe from Microphone or File

```python
# speech_transcribe.py
import os
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk


load_dotenv()

speech_key = os.getenv("AZURE_SPEECH_KEY")
region = os.getenv("AZURE_SPEECH_REGION")

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=region)


def transcribe_from_mic():
	audio_config = speechsdk.AudioConfig(use_default_microphone=True)
	recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

	print("Say something...")
	result = recognizer.recognize_once()

	if result.reason == speechsdk.ResultReason.RecognizedSpeech:
		print("Recognized:", result.text)
	else:
		print("Speech not recognized:", result.reason)


if __name__ == "__main__":
	transcribe_from_mic()
```

Optionally, change to transcribe from a `.wav` file by using `AudioConfig(filename="path.wav")`.

---

## Step 3 – Synthesize Text to Speech

```python
# speech_synthesize.py
import os
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk


load_dotenv()

speech_key = os.getenv("AZURE_SPEECH_KEY")
region = os.getenv("AZURE_SPEECH_REGION")

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=region)
speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"


def synthesize(text: str):
	audio_config = speechsdk.AudioConfig(use_default_speaker=True)
	synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
	result = synthesizer.speak_text_async(text).get()

	if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
		print("Speech synthesized for text:", text)
	else:
		print("Speech synthesis canceled or failed.")


if __name__ == "__main__":
	synthesize("Hello from Azure AI Speech. This is AI-102 lab eight.")
```

Experiment with different voices and text.

---

## Step 4 – Consider Use Cases and Constraints

Discuss/take notes on:

- Latency and streaming needs for real‑time scenarios
- PII and compliance when sending audio to the cloud
- Batching vs streaming for long content

---

## ✅ Lab Checklist

- [ ] Speech key and region configured
- [ ] Simple transcription working (mic or file)
- [ ] Text‑to‑speech working with at least one neural voice
- [ ] Notes captured on latency, privacy, and deployment options

