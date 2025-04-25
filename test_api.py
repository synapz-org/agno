import os
from dotenv import load_dotenv
import openai
import anthropic

# Load environment variables
load_dotenv()


def test_openai():
    print("\nTesting OpenAI API...")
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment variables")
        return False

    client = openai.OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Write a short test message."}],
        )
        print("OpenAI API Test Successful!")
        print("Response:", response.choices[0].message.content)
        return True
    except Exception as e:
        print(f"OpenAI API Test Failed: {str(e)}")
        return False


def test_anthropic():
    print("\nTesting Anthropic API...")
    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment variables")
        return False

    client = anthropic.Anthropic(api_key=api_key)

    try:
        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=100,
            messages=[{"role": "user", "content": "Write a short test message."}],
        )
        print("Anthropic API Test Successful!")
        print("Response:", response.content[0].text)
        return True
    except Exception as e:
        print(f"Anthropic API Test Failed: {str(e)}")
        return False


if __name__ == "__main__":
    # Install required packages if not already installed
    try:
        import openai
        import anthropic
    except ImportError:
        print("Installing required packages...")
        os.system("pip install openai anthropic python-dotenv")
        import openai
        import anthropic

    # Test both APIs
    openai_success = test_openai()
    anthropic_success = test_anthropic()

    # Print summary
    print("\nAPI Test Summary:")
    print(f"OpenAI: {'✅ Success' if openai_success else '❌ Failed'}")
    print(f"Anthropic: {'✅ Success' if anthropic_success else '❌ Failed'}")
