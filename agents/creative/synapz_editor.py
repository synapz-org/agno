"""Synapz Editor - Web3 & AI Content Specialist

A sophisticated AI agent specialized in creating accessible, engaging content about
decentralized AI, blockchain, and biotech projects supported by Synapz.org.
"""

import sys
from pathlib import Path
from textwrap import dedent

from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.vectordb.lancedb import LanceDb, SearchType

# Add the project root to Python path
root_dir = str(Path(__file__).parent.parent.parent)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# Initialize knowledge base with project documentation
agent_knowledge = PDFUrlKnowledgeBase(
    urls=[
        "https://agno-public.s3.amazonaws.com/docs/bittensor.pdf",
        "https://agno-public.s3.amazonaws.com/docs/polkadot.pdf",
        "https://agno-public.s3.amazonaws.com/docs/desci.pdf",
    ],
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="synapz_knowledge",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
)

# Initialize storage for session management
agent_storage = SqliteStorage(table_name="synapz_editor", db_file="tmp/agents.db")

# Create the Synapz Editor agent
agent = Agent(
    name="Synapz Editor",
    model=OpenAIChat(id="gpt-4o"),
    storage=agent_storage,
    knowledge=agent_knowledge,
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    read_chat_history=True,
    markdown=True,
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
        1. Start with a compelling hook that connects to readers' interests
        2. Break down complex topics into digestible sections
        3. Use specific project examples and case studies
        4. Include practical takeaways and next steps
        5. End with a thought-provoking conclusion
        6. Always include a Sources section with links to references

        Research and fact-checking:
        1. First, search the knowledge base for accurate technical information
        2. If needed, supplement with web searches for:
           - Latest project developments and updates
           - Real-world implementations and case studies
           - Community feedback and adoption metrics
        3. Always verify technical details with primary sources
        4. Track and cite all sources used in the content

        Remember: Your goal is to foster understanding and adoption of these
        transformative technologies while maintaining Synapz's focus on
        decentralization, intelligence, and human potential.\
    """
    ),
)

# Example usage
if __name__ == "__main__":
    # Write a blog post about Bittensor's subnet ecosystem
    response = agent.run(
        "Write a blog post about Bittensor's subnet ecosystem, focusing on its "
        "role in decentralized AI development and real-world applications."
    )

    # Save the response to a file
    with open("bittensor_subnet_blog.md", "w") as f:
        f.write(response.content)
