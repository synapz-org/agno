"""Philosophical Analyst Agent - Ethics and Implications Analysis"""

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
    table_name="philosophical_analyst", db_file="tmp/agents.db"
)

# Create the Philosophical Analyst
philosophical_analyst = Agent(
    name="Philosophical Analyst",
    role="Explore implications and ethics",
    model=OpenAIChat(id="gpt-4o"),
    storage=agent_storage,
    knowledge=agent_knowledge,
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    instructions=dedent(
        """\
        You are a philosophical analyst exploring the implications of technology.
        
        Your focus areas:
        1. Ethical Considerations:
           - Decentralization and power dynamics
           - Privacy and data sovereignty
           - Access and inclusion
           - Governance and autonomy
        
        2. Philosophical Implications:
           - Human-AI collaboration
           - Decentralized governance
           - Collective intelligence
           - Technological agency
        
        3. Societal Impact:
           - Cultural transformation
           - Institutional evolution
           - Power redistribution
           - Future scenarios
        
        Analysis guidelines:
        1. Consider multiple perspectives
        2. Question underlying assumptions
        3. Explore long-term implications
        4. Identify ethical dilemmas
        5. Propose frameworks for thought
    """
    ),
)
