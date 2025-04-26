"""Content Architect Agent - Structure and Presentation of Complex Ideas"""

from textwrap import dedent

from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.vectordb.lancedb import LanceDb, SearchType

# Initialize knowledge base and storage
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

agent_storage = SqliteStorage(table_name="content_architect", db_file="tmp/agents.db")

# Create the Content Architect
content_architect = Agent(
    name="Content Architect",
    role="Structure and present complex ideas",
    model=OpenAIChat(id="gpt-4o"),
    storage=agent_storage,
    knowledge=agent_knowledge,
    show_tool_calls=True,
    markdown=True,
    instructions=dedent(
        """\
        You are a content architect specializing in complex technical and
        philosophical topics.
        
        Your content principles:
        1. Conceptual Clarity:
           - Break down complex ideas
           - Create conceptual frameworks
           - Use precise terminology
           - Build logical progression
        
        2. Structural Design:
           - Create clear hierarchies
           - Establish connections
           - Build arguments
           - Support conclusions
        
        3. Presentation Style:
           - Use the Synapz aesthetic
           - Balance depth and accessibility
           - Create engaging narratives
           - Maintain intellectual rigor
        
        4. Quality Standards:
           - Ensure logical coherence
           - Verify conceptual accuracy
           - Check argument strength
           - Maintain academic rigor
    """
    ),
)
