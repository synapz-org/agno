"""Synapz Teams - Flexible Agent Combinations

This file demonstrates how to create different team combinations using the
specialized agents. Each team is optimized for different types of content creation.
"""

from textwrap import dedent

from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.team.team import Team

from .technical_researcher import technical_researcher
from .philosophical_analyst import philosophical_analyst
from .content_architect import content_architect

# Initialize team storage
team_storage = SqliteStorage(table_name="synapz_teams", db_file="tmp/agents.db")

# Technical Analysis Team
technical_team = Team(
    name="Technical Analysis Team",
    members=[technical_researcher, content_architect],
    model=OpenAIChat(id="gpt-4o"),
    mode="coordinate",
    storage=team_storage,
    show_tool_calls=True,
    markdown=True,
    instructions=dedent(
        """\
        You are the Technical Analysis Team Lead, focusing on deep technical
        analysis and clear presentation of complex systems.
        
        Your responsibilities:
        1. Technical Depth:
           - Ensure comprehensive technical coverage
           - Verify implementation details
           - Analyze system architecture
           - Evaluate technical trade-offs
        
        2. Presentation:
           - Structure technical information clearly
           - Create conceptual frameworks
           - Use precise terminology
           - Maintain technical accuracy
    """
    ),
)

# Philosophical Analysis Team
philosophical_team = Team(
    name="Philosophical Analysis Team",
    members=[philosophical_analyst, content_architect],
    model=OpenAIChat(id="gpt-4o"),
    mode="coordinate",
    storage=team_storage,
    show_tool_calls=True,
    markdown=True,
    instructions=dedent(
        """\
        You are the Philosophical Analysis Team Lead, focusing on ethical
        implications and societal impact.
        
        Your responsibilities:
        1. Philosophical Depth:
           - Explore ethical considerations
           - Analyze societal implications
           - Question underlying assumptions
           - Consider multiple perspectives
        
        2. Presentation:
           - Structure philosophical arguments
           - Create conceptual frameworks
           - Build logical progression
           - Maintain intellectual rigor
    """
    ),
)

# Comprehensive Analysis Team
comprehensive_team = Team(
    name="Comprehensive Analysis Team",
    members=[technical_researcher, philosophical_analyst, content_architect],
    model=OpenAIChat(id="gpt-4o"),
    mode="coordinate",
    storage=team_storage,
    show_tool_calls=True,
    markdown=True,
    instructions=dedent(
        """\
        You are the Comprehensive Analysis Team Lead, combining technical and
        philosophical insights.
        
        Your responsibilities:
        1. Analysis Integration:
           - Combine technical and philosophical perspectives
           - Ensure comprehensive coverage
           - Maintain balance between depth areas
           - Synthesize diverse insights
        
        2. Presentation:
           - Structure complex information
           - Create unified frameworks
           - Build compelling narratives
           - Maintain intellectual rigor
    """
    ),
)

# Example usage
if __name__ == "__main__":
    # Technical analysis example
    technical_team.print_response(
        message="Analyze the technical architecture of Bittensor's subnet system.",
        stream=True,
    )

    # Philosophical analysis example
    philosophical_team.print_response(
        message="Explore the ethical implications of decentralized AI governance.",
        stream=True,
    )

    # Comprehensive analysis example
    comprehensive_team.print_response(
        message="Provide a comprehensive analysis of decentralized AI systems, "
        "including both technical architecture and philosophical implications.",
        stream=True,
    )
