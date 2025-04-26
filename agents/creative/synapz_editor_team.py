"""Synapz Editor Team - Technical & Philosophical Analysis Squad

A team of AI agents working together to create deep technical and philosophical
content about decentralized AI, blockchain, and biotech projects. The team consists of:
1. Technical Researcher: Analyzes protocols and architectures
2. Philosophical Analyst: Explores implications and ethics
3. Content Architect: Structures and presents complex ideas
4. Lead Editor: Coordinates and synthesizes insights
"""

from textwrap import dedent

from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.team.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.vectordb.lancedb import LanceDb, SearchType

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

# Create the Technical Researcher
technical_agent = Agent(
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

# Create the Philosophical Analyst
philosophical_agent = Agent(
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

# Create the Content Architect
content_agent = Agent(
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

# Create the Synapz Editor Team
synapz_team = Team(
    members=[technical_agent, philosophical_agent, content_agent],
    model=OpenAIChat(id="gpt-4o"),
    mode="coordinate",
    storage=agent_storage,
    show_tool_calls=True,
    markdown=True,
    instructions=dedent(
        """\
        You are the Synapz Editor-in-Chief, leading a team of specialized agents.
        
        Your responsibilities:
        1. Team Coordination:
           - Delegate tasks to appropriate agents
           - Ensure comprehensive coverage
           - Maintain intellectual rigor
           - Synthesize diverse perspectives
        
        2. Content Quality:
           - Verify technical accuracy
           - Ensure philosophical depth
           - Maintain academic standards
           - Deliver insightful analysis
        
        3. Style and Tone:
           - Uphold the Synapz aesthetic
           - Balance technical and philosophical depth
           - Create compelling narratives
           - Maintain intellectual engagement
        
        4. Final Output:
           - Combine technical and philosophical insights
           - Structure for maximum impact
           - Include conceptual frameworks
           - Provide thought-provoking conclusions
    """
    ),
)

# Example usage
if __name__ == "__main__":
    # Create a comprehensive analysis of decentralized AI governance
    synapz_team.print_response(
        message="Analyze the technical architecture and philosophical implications "
        "of decentralized AI governance systems, focusing on Bittensor's approach.",
        stream=True,
    )
