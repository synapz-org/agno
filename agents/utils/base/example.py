"""Example usage of the BasicAgent class."""

from basic_agent import BasicAgent


def test_agents():
    """Test both OpenAI and Anthropic agents."""
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

    # Test both agents
    test_message = "What is the capital of France?"

    print("\nTesting OpenAI Agent:")
    print(f"Question: {test_message}")
    response = openai_agent.chat(test_message)
    print(f"Response: {response}")

    print("\nTesting Anthropic Agent:")
    print(f"Question: {test_message}")
    response = anthropic_agent.chat(test_message)
    print(f"Response: {response}")


if __name__ == "__main__":
    test_agents()
