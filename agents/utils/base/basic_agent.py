"""Basic agent implementation supporting multiple LLM providers."""

import os
from typing import Literal, Optional

import anthropic
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class BasicAgent:
    """A basic agent that can use either OpenAI or Anthropic as its LLM provider."""

    def __init__(
        self,
        provider: Literal["openai", "anthropic"] = "openai",
        model: Optional[str] = None,
        system_prompt: Optional[str] = None,
    ):
        """Initialize a basic agent with the specified provider and model.

        Args:
            provider: The LLM provider to use ("openai" or "anthropic")
            model: The specific model to use. If None, uses a default
            system_prompt: Optional system prompt to guide the agent's behavior
        """
        self.provider = provider
        self.system_prompt = system_prompt
        self.messages = []

        # Set default models if none specified
        if model is None:
            self.model = (
                "gpt-4o-mini" if provider == "openai" else "claude-3-opus-20240229"
            )
        else:
            self.model = model

        # Initialize the appropriate client
        if provider == "openai":
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("OPENAI_API_KEY not found in environment variables")
            self.client = openai.OpenAI(api_key=api_key)
            # Add system prompt for OpenAI
            if system_prompt:
                self.messages.append({"role": "system", "content": system_prompt})
        else:
            api_key = os.getenv("ANTHROPIC_API_KEY")
            if not api_key:
                raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
            self.client = anthropic.Anthropic(api_key=api_key)

    def chat(self, message: str) -> str:
        """Send a message to the agent and get its response.

        Args:
            message: The user's message

        Returns:
            The agent's response
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
            else:
                # For Anthropic, handle system prompt differently
                kwargs = {
                    "model": self.model,
                    "max_tokens": 1000,
                    "messages": self.messages,
                }
                if self.system_prompt:
                    kwargs["system"] = self.system_prompt

                response = self.client.messages.create(**kwargs)
                response_text = response.content[0].text

            # Add assistant response to history
            self.messages.append({"role": "assistant", "content": response_text})
            return response_text

        except Exception as e:
            print(f"Error in chat: {str(e)}")
            raise

    def clear_history(self) -> None:
        """Clear the conversation history."""
        self.messages = []
        if self.provider == "openai" and self.system_prompt:
            self.messages.append({"role": "system", "content": self.system_prompt})
