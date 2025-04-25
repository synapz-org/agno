import os
import requests
from typing import Optional


class ElevenLabsClient:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("ELEVENLABS_API_KEY")
        if not self.api_key:
            raise ValueError(
                "ElevenLabs API key is required. "
                "Please set it in the ELEVENLABS_API_KEY "
                "environment variable."
            )

        self.base_url = "https://api.elevenlabs.io/v1"
        self.headers = {"xi-api-key": self.api_key, "Content-Type": "application/json"}

    def text_to_speech(
        self,
        text: str,
        voice_id: str = "21m00Tcm4TlvDq8ikWAM",
        output_path: Optional[str] = None,
    ) -> bytes:
        """
        Convert text to speech using ElevenLabs API.

        Args:
            text: The text to convert to speech
            voice_id: The ID of the voice to use (default is a standard voice)
            output_path: Optional path to save the audio file

        Returns:
            bytes: The audio data
        """
        url = f"{self.base_url}/text-to-speech/{voice_id}"

        data = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.5},
        }

        response = requests.post(url, json=data, headers=self.headers)
        response.raise_for_status()

        audio_data = response.content

        if output_path:
            with open(output_path, "wb") as f:
                f.write(audio_data)

        return audio_data
