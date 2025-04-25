"""Example usage of the BasicAgent class."""

import os
from basic_agent import BasicAgent


def test_agents():
    """Test OpenAI, Anthropic, GROQ, and ElevenLabs agents."""
    # Create an agent with OpenAI
    openai_agent = BasicAgent(
        provider="openai",
        system_prompt=(
            "You are a helpful assistant that provides clear and concise answers."
        ),
    )

    # Create an agent with Anthropic
    anthropic_agent = BasicAgent(
        provider="anthropic",
        system_prompt=(
            "You are a helpful assistant that provides clear and concise answers."
        ),
    )

    # Create an agent with GROQ
    groq_agent = BasicAgent(
        provider="groq",
        system_prompt=(
            "You are a helpful assistant that provides clear and concise answers."
        ),
    )

    # Create an agent with ElevenLabs
    elevenlabs_agent = BasicAgent(
        provider="elevenlabs",
        voice_id="21m00Tcm4TlvDq8ikWAM",  # Default voice
    )

    # Test all agents
    test_message = "What is the capital of France?"

    print("\nTesting OpenAI Agent:")
    print(f"Question: {test_message}")
    response = openai_agent.chat(test_message)
    print(f"Response: {response}")

    print("\nTesting Anthropic Agent:")
    print(f"Question: {test_message}")
    response = anthropic_agent.chat(test_message)
    print(f"Response: {response}")

    print("\nTesting GROQ Agent:")
    print(f"Question: {test_message}")
    response = groq_agent.chat(test_message)
    print(f"Response: {response}")

    print("\nTesting ElevenLabs Agent (Text):")
    print(f"Question: {test_message}")
    response = elevenlabs_agent.chat(test_message)
    print(f"Response: {response}")

    print("\nTesting ElevenLabs Agent (Audio):")
    print(f"Question: {test_message}")
    audio_response = elevenlabs_agent.chat(test_message, output_format="audio")
    # Save the audio response
    with open("response.mp3", "wb") as f:
        f.write(audio_response)
    print("Audio response saved as 'response.mp3'")


if __name__ == "__main__":
    test_agents()
