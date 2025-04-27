"""Synapz Editor - Web3 & AI Content Specialist

A sophisticated AI agent specialized in creating accessible, engaging content about
decentralized AI, blockchain, and biotech projects supported by Synapz.org.
"""

import sys
from pathlib import Path
from textwrap import dedent

from agno.agent import Agent, DevelopmentStatus
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

# Create the Synapz Editor
synapz_editor = Agent(
    name="Synapz Editor",
    role="Create and edit technical and philosophical content",
    model=OpenAIChat(id="gpt-4o"),
    storage=agent_storage,
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    response_model=Content,
    status=DevelopmentStatus.EXPERIMENTAL,
    version="0.0.1",
    instructions=dedent(
        """\
        You are a content creation specialist focusing on technical and philosophical topics.
        
        Your focus areas:
        1. Technical Content:
           - AI and blockchain technology
           - Decentralized systems
           - Technical architecture
           - Protocol design
        
        2. Philosophical Analysis:
           - Ethics of AI
           - Decentralization philosophy
           - Technological impact
           - Future implications
        
        3. Content Creation:
           - Blog posts
           - Technical documentation
           - Philosophical essays
           - Research summaries
        
        Content guidelines:
        1. Maintain technical accuracy
        2. Provide clear explanations
        3. Include relevant examples
        4. Cite sources properly
        5. Engage the reader
    """
    ),
)

# Example usage
if __name__ == "__main__":
    # Write a blog post about Bittensor's subnet ecosystem
    response = synapz_editor.run(
        "Write a blog post about Bittensor's subnet ecosystem, focusing on its "
        "role in decentralized AI development and real-world applications."
    )

    # Save the response to a file
    with open("bittensor_subnet_blog.md", "w") as f:
        f.write(response.content)
