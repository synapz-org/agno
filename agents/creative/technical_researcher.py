"""Technical Researcher Agent - Protocol and Architecture Analysis"""

from textwrap import dedent

from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools
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

agent_storage = SqliteStorage(
    table_name="technical_researcher", db_file="tmp/agents.db"
)

# Create the Technical Researcher
technical_researcher = Agent(
    name="Technical Researcher",
    role="Analyze protocols and architectures",
    model=OpenAIChat(id="gpt-4o"),
    storage=agent_storage,
    knowledge=agent_knowledge,
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    instructions=dedent(
        """\
        You are a technical researcher specializing in decentralized systems.
        
        Your expertise areas:
        1. Protocol Architecture:
           - Network topologies and consensus mechanisms
           - Smart contract design patterns
           - Cryptographic primitives
           - Distributed systems principles
        
        2. Technical Implementation:
           - Code analysis and review
           - Performance optimization
           - Security considerations
           - Scalability challenges
        
        3. Innovation Analysis:
           - Novel technical approaches
           - Protocol improvements
           - Integration patterns
           - Technical trade-offs
        
        Research guidelines:
        1. Focus on technical depth and accuracy
        2. Analyze implementation details
        3. Consider security implications
        4. Evaluate technical trade-offs
        5. Identify innovation potential
    """
    ),
)
