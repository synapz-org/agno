"""Bittensor Monitor Team - Subnet Tracking and Analysis

A team of specialized agents working together to monitor and analyze Bittensor
subnets, providing technical analysis and alerts for significant events.
"""

from textwrap import dedent

from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.team.team import Team

from .subnet_monitor import subnet_monitor
from .technical_analyst import technical_analyst
from .alert_manager import alert_manager

# Initialize team storage
team_storage = SqliteStorage(table_name="bittensor_monitor", db_file="tmp/agents.db")

# Create the Monitoring Team
monitoring_team = Team(
    name="Bittensor Monitor Team",
    members=[subnet_monitor, technical_analyst, alert_manager],
    model=OpenAIChat(id="gpt-4o"),
    mode="coordinate",
    storage=team_storage,
    show_tool_calls=True,
    markdown=True,
    instructions=dedent(
        """\
        You are the Bittensor Monitor Team Lead, coordinating subnet monitoring,
        technical analysis, and alert management.
        
        Your responsibilities:
        1. Monitoring Coordination:
           - Track specified subnets
           - Monitor key metrics
           - Identify significant events
           - Coordinate team responses
        
        2. Analysis Integration:
           - Combine monitoring data
           - Integrate technical analysis
           - Assess market context
           - Provide comprehensive insights
        
        3. Alert Management:
           - Set alert criteria
           - Prioritize notifications
           - Provide context
           - Track alert history
    """
    ),
)

# Example usage
if __name__ == "__main__":
    # Monitor specific subnets
    monitoring_team.print_response(
        message="Monitor subnet 1 and subnet 5 for price action and set alerts "
        "for key support/resistance levels.",
        stream=True,
    )

    # Analyze market trends
    monitoring_team.print_response(
        message="Analyze the current market structure and identify potential "
        "trading opportunities in the subnet ecosystem.",
        stream=True,
    )

    # Set up alerts
    monitoring_team.print_response(
        message="Set up alerts for subnet 1 when it reaches $500 and subnet 5 "
        "when it breaks its current resistance level.",
        stream=True,
    )
