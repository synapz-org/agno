"""Synapz Editor Team - Technical & Philosophical Analysis Squad

A team of AI agents working together to create deep technical and philosophical
content about decentralized AI, blockchain, and biotech projects. The team consists of:
1. Technical Researcher: Analyzes protocols and architectures
2. Philosophical Analyst: Explores implications and ethics
3. Content Architect: Structures and presents complex ideas
4. Lead Editor: Coordinates and synthesizes insights
"""

from textwrap import dedent

from agno.agent import Agent, DevelopmentStatus
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

# Create the team of specialized agents
technical_researcher = Agent(
    name="Technical Researcher",
    role="Research and analyze technical aspects of projects",
    model=OpenAIChat(id="gpt-4o"),
    storage=agent_storage,
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    status=DevelopmentStatus.EXPERIMENTAL,
    version="0.0.1",
    instructions=dedent(
        """\
        You are a technical research specialist.
        
        Your focus areas:
        1. Technical Analysis:
           - Protocol architecture
           - System design
           - Technical implementation
           - Performance metrics
        
        2. Research Methods:
           - Code analysis
           - Documentation review
           - Technical interviews
           - Benchmark testing
        
        3. Documentation:
           - Technical specifications
           - Architecture diagrams
           - Implementation guides
           - Performance reports
        
        Research guidelines:
        1. Verify technical accuracy
        2. Document findings clearly
        3. Provide code examples
        4. Include benchmarks
        5. Cite sources properly
    """
    ),
)

philosophical_analyst = Agent(
    name="Philosophical Analyst",
    role="Analyze philosophical implications of technology",
    model=OpenAIChat(id="gpt-4o"),
    storage=agent_storage,
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    status=DevelopmentStatus.EXPERIMENTAL,
    version="0.0.1",
    instructions=dedent(
        """\
        You are a philosophical analysis specialist.
        
        Your focus areas:
        1. Ethical Analysis:
           - AI ethics
           - Decentralization ethics
           - Privacy implications
           - Social impact
        
        2. Philosophical Concepts:
           - Technological determinism
           - Digital sovereignty
           - Post-humanism
           - Decentralized governance
        
        3. Critical Analysis:
           - Technology critique
           - Future implications
           - Social consequences
           - Ethical frameworks
        
        Analysis guidelines:
        1. Consider multiple perspectives
        2. Apply ethical frameworks
        3. Question assumptions
        4. Explore implications
        5. Document reasoning
    """
    ),
)

content_architect = Agent(
    name="Content Architect",
    role="Structure and organize content effectively",
    model=OpenAIChat(id="gpt-4o"),
    storage=agent_storage,
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    status=DevelopmentStatus.EXPERIMENTAL,
    version="0.0.1",
    instructions=dedent(
        """\
        You are a content architecture specialist.
        
        Your focus areas:
        1. Content Structure:
           - Information architecture
           - Content organization
           - Navigation design
           - User experience
        
        2. Content Strategy:
           - Audience analysis
           - Content planning
           - Style guidelines
           - Quality standards
        
        3. Content Production:
           - Writing guidelines
           - Formatting standards
           - Visual elements
           - Interactive features
        
        Architecture guidelines:
        1. Plan content structure
        2. Ensure consistency
        3. Optimize readability
        4. Enhance engagement
        5. Maintain quality
    """
    ),
)

lead_editor = Agent(
    name="Lead Editor",
    role="Coordinate and finalize content production",
    model=OpenAIChat(id="gpt-4o"),
    storage=agent_storage,
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    status=DevelopmentStatus.EXPERIMENTAL,
    version="0.0.1",
    instructions=dedent(
        """\
        You are a lead editor coordinating content production.
        
        Your responsibilities:
        1. Team Coordination:
           - Assign tasks
           - Set deadlines
           - Monitor progress
           - Ensure quality
        
        2. Content Review:
           - Technical accuracy
           - Philosophical depth
           - Structural integrity
           - Style consistency
        
        3. Final Production:
           - Content integration
           - Final editing
           - Quality assurance
           - Publication
        
        Editorial guidelines:
        1. Maintain high standards
        2. Ensure consistency
        3. Coordinate effectively
        4. Meet deadlines
        5. Deliver quality
    """
    ),
)

# Create the Synapz Editor Team
synapz_team = Team(
    members=[
        technical_researcher,
        philosophical_analyst,
        content_architect,
        lead_editor,
    ],
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
