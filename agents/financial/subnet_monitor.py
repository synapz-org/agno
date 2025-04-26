"""Subnet Monitor Agent - Bittensor Subnet Tracking

This agent monitors specific Bittensor subnets on taostats.io, tracking their
performance metrics and price action.
"""

from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools

# Initialize storage
agent_storage = SqliteStorage(table_name="subnet_monitor", db_file="tmp/agents.db")

# Create the Subnet Monitor
subnet_monitor = Agent(
    name="Subnet Monitor",
    role="Track and monitor Bittensor subnets",
    model=OpenAIChat(id="gpt-4o"),
    storage=agent_storage,
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    instructions=dedent(
        """\
        You are a Bittensor subnet monitoring specialist.
        
        Your monitoring focus:
        1. Subnet Metrics:
           - TAO price and volume
           - Network participation
           - Validator performance
           - Emission rates
        
        2. Performance Tracking:
           - Price action analysis
           - Volume trends
           - Network activity
           - Validator metrics
        
        3. Alert Criteria:
           - Price level breaches
           - Volume spikes
           - Network changes
           - Validator shifts
        
        Monitoring guidelines:
        1. Track specified subnets continuously
        2. Monitor key performance indicators
        3. Identify significant changes
        4. Report anomalies promptly
        5. Maintain historical context
    """
    ),
)
