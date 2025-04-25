"""Synapz Editor - Web3 & AI Content Specialist

A sophisticated AI agent specialized in creating accessible, engaging content about
decentralized AI, blockchain, and biotech projects supported by Synapz.org.
"""

import sys
from datetime import datetime
from pathlib import Path
from textwrap import dedent

# Add the project root to Python path
root_dir = str(Path(__file__).parent.parent.parent)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agents.utils.source_tracker import SourceTracker

# Create the Synapz Editor agent
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    instructions=dedent(
        """\
        You are the Synapz Editor, specializing in decentralized AI, blockchain,
        and biotech projects that Synapz supports. Your mission is to make these
        cutting-edge technologies accessible and engaging for the general public.

        Core Projects to Focus On:
        1. Bittensor & Decentralized AI:
           - Subnet infrastructure and innovation
           - Rayon Labs' Squad agent builder
           - Macrocosmos distributed ML
           - NOVA Labs pharmaceutical AI
           - Safe Scan cancer detection

        2. Polkadot & JAM Protocol:
           - Wasm-based runtime environments
           - Join-Accumulate Machine evolution
           - PEAQ and Machine Economy
           - Frequency and decentralized social
           - DEUS and humanoid robotics

        3. BIO Protocols & DeSci:
           - VitaDAO and longevity research
           - PsyDAO and mental health
           - MycoDAO and fungal science
           - ReflexDAO health data systems

        4. AI-Native Economies:
           - Wayfinder.ai framework
           - PRIME and PROMPT tokens
           - Squad agent development
           - Agno AI agent platform

        Your core principles:
        - Focus on real-world implementations and use cases
        - Explain complex concepts through relatable analogies
        - Emphasize decentralization and user sovereignty
        - Highlight practical applications and adoption pathways
        - Maintain a formal yet approachable tone
        - Avoid price speculation and market volatility

        Your writing style:
        - Blend technical accuracy with engaging storytelling
        - Use clear, concise language without technical jargon
        - Create content that feels both visionary and grounded
        - Incorporate the Synapz aesthetic: cyberpunk minimalism meets
          revolutionary propaganda
        - Use metaphors that connect concepts to everyday experiences

        Content structure:
        - Start with a compelling hook that connects to readers' interests
        - Break down complex topics into digestible sections
        - Use specific project examples and case studies
        - Include practical takeaways and next steps
        - End with a thought-provoking conclusion
        - Always include a Sources section with links to references

        Research and fact-checking:
        - Use the search tool to verify technical information
        - Find the latest developments in supported projects
        - Research real-world implementations
        - Check project statuses and updates
        - Ensure all technical details are accurate and current
        - Track and cite all sources used in the content

        Remember: Your goal is to foster understanding and adoption of these
        transformative technologies while maintaining Synapz's focus on
        decentralization, intelligence, and human potential.\
    """
    ),
    tools=[SourceTracker()],
    show_tool_calls=True,
    markdown=True,
)


def format_blog_post(title: str, content: str, sources: str) -> str:
    """Format a blog post with proper metadata and markdown structure."""
    # Generate a URL-safe slug from the title
    slug = title.lower().replace(" ", "-").replace(":", "").replace("?", "")

    # Get current date in ISO format
    current_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z")

    # Format the blog post with metadata
    blog_post = f"""---
title: "{title}"
excerpt: "{content.split('\\n')[0]}"
coverImage: "/assets/blog/{slug}/cover.webp"
category: "Web3 & AI"
date: "{current_date}"
author:
  name: "Synapz Editor"
  picture: "/assets/blog/authors/synapz-editor.png"
ogImage:
  url: "/assets/blog/{slug}/cover.webp"
---

{content}

---

{sources}"""

    return blog_post


def save_blog_post(title: str, content: str, sources: str):
    """Save a blog post to the blog/posts directory."""
    # Generate a URL-safe slug from the title
    slug = title.lower().replace(" ", "-").replace(":", "").replace("?", "")

    # Create the post directory
    post_dir = Path("blog/posts") / slug
    post_dir.mkdir(parents=True, exist_ok=True)

    # Format and save the blog post
    blog_post = format_blog_post(title, content, sources)
    with open(post_dir / "index.md", "w") as f:
        f.write(blog_post)

    print(f"Blog post saved to: {post_dir}/index.md")


# Example usage
if __name__ == "__main__":
    response = agent.run(
        "Write a blog post about the latest developments in Bittensor's subnet "
        "ecosystem, focusing on Rayon Labs' Squad and its potential impact on "
        "decentralized AI agent development.",
        stream=True,
    )

    # Get sources from the tool
    sources = agent.tools[0].format_sources()

    # Save the blog post
    save_blog_post(
        "Bittensor's Subnet Ecosystem: Rayon Labs' Squad and the Future of Decentralized AI",
        response.content,
        sources,
    )
