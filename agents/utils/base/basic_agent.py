"""Basic agent implementation supporting multiple LLM providers."""

import os
from typing import Literal, Optional, Union

import anthropic
import groq
import openai
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class BasicAgent:
    """A basic agent that can use OpenAI, Anthropic, GROQ, or ElevenLabs."""

    def __init__(
        self,
        provider: Literal["openai", "anthropic", "groq", "elevenlabs"] = "openai",
        model: Optional[str] = None,
        system_prompt: Optional[str] = None,
        voice_id: Optional[str] = None,
    ):
        """Initialize a basic agent with the specified provider and model.

        Args:
            provider: The LLM provider to use
            model: The specific model to use. If None, uses a default
            system_prompt: Optional system prompt to guide the agent's behavior
            voice_id: Optional voice ID for ElevenLabs text-to-speech
        """
        self.provider = provider
        self.system_prompt = system_prompt
        self.messages = []
        self.voice_id = voice_id

        # Set default models if none specified
        if model is None:
            self.model = {
                "openai": "gpt-4o-mini",
                "anthropic": "claude-3-opus-20240229",
                "groq": "mixtral-8x7b-32768",
                "elevenlabs": "eleven_monolingual_v1",
            }[provider]
        else:
            self.model = model

        # Initialize the appropriate client
        if provider == "openai":
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("OPENAI_API_KEY not found in environment variables")
            self.client = openai.OpenAI(api_key=api_key)
            if system_prompt:
                self.messages.append({"role": "system", "content": system_prompt})
        elif provider == "anthropic":
            api_key = os.getenv("ANTHROPIC_API_KEY")
            if not api_key:
                raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
            self.client = anthropic.Anthropic(api_key=api_key)
        elif provider == "groq":
            api_key = os.getenv("GROQ_API_KEY")
            if not api_key:
                raise ValueError("GROQ_API_KEY not found in environment variables")
            self.client = groq.Groq(api_key=api_key)
            if system_prompt:
                self.messages.append({"role": "system", "content": system_prompt})
        else:  # ElevenLabs
            api_key = os.getenv("ELEVENLABS_API_KEY")
            if not api_key:
                raise ValueError(
                    "ELEVENLABS_API_KEY not found in environment variables"
                )
            self.api_key = api_key
            if not voice_id:
                self.voice_id = "21m00Tcm4TlvDq8ikWAM"  # Default voice

    def chat(
        self, message: str, output_format: Literal["text", "audio"] = "text"
    ) -> Union[str, bytes]:
        """Send a message to the agent and get its response.

        Args:
            message: The user's message
            output_format: The desired output format ("text" or "audio")

        Returns:
            The agent's response as text or audio bytes
        """
        # Add user message to history
        self.messages.append({"role": "user", "content": message})

        try:
            if self.provider == "openai":
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=self.messages,
                )
                response_text = response.choices[0].message.content
            elif self.provider == "anthropic":
                kwargs = {
                    "model": self.model,
                    "max_tokens": 1000,
                    "messages": self.messages,
                }
                if self.system_prompt:
                    kwargs["system"] = self.system_prompt
                response = self.client.messages.create(**kwargs)
                response_text = response.content[0].text
            elif self.provider == "groq":
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=self.messages,
                )
                response_text = response.choices[0].message.content
            else:  # ElevenLabs
                if output_format == "audio":
                    # Convert text to speech
                    url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice_id}"
                    headers = {
                        "Accept": "audio/mpeg",
                        "Content-Type": "application/json",
                        "xi-api-key": self.api_key,
                    }
                    data = {
                        "text": message,
                        "model_id": self.model,
                        "voice_settings": {"stability": 0.5, "similarity_boost": 0.5},
                    }
                    response = requests.post(url, json=data, headers=headers)
                    if response.status_code != 200:
                        raise ValueError(f"ElevenLabs API error: {response.text}")
                    return response.content
                else:
                    # For text output, just return the input message
                    response_text = message

            # Add assistant response to history
            if self.provider != "elevenlabs":
                self.messages.append({"role": "assistant", "content": response_text})
            return response_text

        except Exception as e:
            print(f"Error in chat: {str(e)}")
            raise

    def clear_history(self) -> None:
        """Clear the conversation history."""
        self.messages = []
        if self.provider in ["openai", "groq"] and self.system_prompt:
            self.messages.append({"role": "system", "content": self.system_prompt})
