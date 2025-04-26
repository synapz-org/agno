"""Technical Analyst Agent - Market Analysis Specialist

This agent performs technical analysis on Bittensor subnets, identifying patterns,
trends, and potential trading opportunities.
"""

from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools

# Initialize storage
agent_storage = SqliteStorage(table_name="technical_analyst", db_file="tmp/agents.db")

# Create the Technical Analyst
technical_analyst = Agent(
    name="Technical Analyst",
    role="Analyze market trends and patterns",
    model=OpenAIChat(id="gpt-4o"),
    storage=agent_storage,
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    instructions=dedent(
        """\
        You are a technical analysis specialist for Bittensor subnets.
        
        Your analysis focus:
        1. Technical Indicators:
           - Moving averages
           - RSI and momentum
           - Volume analysis
           - Support/resistance levels
        
        2. Pattern Recognition:
           - Chart patterns
           - Trend analysis
           - Breakout signals
           - Reversal patterns
        
        3. Market Structure:
           - Market cycles
           - Trend phases
           - Volume profiles
           - Order flow analysis
        
        Analysis guidelines:
        1. Use multiple timeframes
        2. Confirm signals with volume
        3. Consider market context
        4. Identify key levels
        5. Assess risk/reward ratios
    """
    ),
)
