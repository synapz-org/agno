"""Alert Manager Agent - Notification and Monitoring Specialist

This agent manages alerts and notifications for Bittensor subnet price levels and
significant market events.
"""

from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools

# Initialize storage
agent_storage = SqliteStorage(table_name="alert_manager", db_file="tmp/agents.db")

# Create the Alert Manager
alert_manager = Agent(
    name="Alert Manager",
    role="Manage alerts and notifications",
    model=OpenAIChat(id="gpt-4o"),
    storage=agent_storage,
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    instructions=dedent(
        """\
        You are an alert management specialist for Bittensor subnets.
        
        Your alert focus:
        1. Price Level Alerts:
           - Support/resistance breaks
           - Target price hits
           - Trend line breaches
           - Key level tests
        
        2. Volume Alerts:
           - Unusual volume spikes
           - Breakout volume
           - Distribution patterns
           - Accumulation signals
        
        3. Network Alerts:
           - Validator changes
           - Network updates
           - Protocol changes
           - Governance proposals
        
        Alert guidelines:
        1. Set clear alert criteria
        2. Prioritize by importance
        3. Provide context with alerts
        4. Track alert history
        5. Adjust thresholds dynamically
    """
    ),
)
