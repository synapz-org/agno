"""Technical Analyst Agent - Market Analysis Specialist

This agent performs technical analysis on Bittensor subnets, identifying patterns,
trends, and potential trading opportunities.
"""

from textwrap import dedent
from typing import Dict, List

from pydantic import BaseModel, Field

from agno.agent import Agent, DevelopmentStatus
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools


# Define structured output models
class TechnicalIndicators(BaseModel):
    rsi: float = Field(..., description="Relative Strength Index")
    macd: float = Field(..., description="Moving Average Convergence Divergence")
    bollinger_bands: Dict[str, float] = Field(..., description="Bollinger Bands values")
    moving_averages: Dict[str, float] = Field(..., description="Moving averages")


class TechnicalAnalysis(BaseModel):
    subnet_id: int = Field(..., description="ID of the subnet")
    timeframe: str = Field(..., description="Analysis timeframe")
    trend_strength: float = Field(..., description="Trend strength (0-1)")
    key_levels: Dict[str, List[float]] = Field(
        ..., description="Support/resistance levels"
    )
    indicators: TechnicalIndicators = Field(..., description="Technical indicators")
    patterns: List[str] = Field(..., description="Identified chart patterns")
    confidence_score: float = Field(..., description="Analysis confidence (0-1)")
    timestamp: str = Field(..., description="Analysis timestamp")

    class Config:
        json_schema_extra = {
            "required": [
                "subnet_id",
                "timeframe",
                "trend_strength",
                "key_levels",
                "indicators",
                "patterns",
                "confidence_score",
                "timestamp",
            ],
            "properties": {
                "subnet_id": {"type": "integer"},
                "timeframe": {"type": "string"},
                "trend_strength": {"type": "number"},
                "key_levels": {"type": "object"},
                "indicators": {"type": "object"},
                "patterns": {"type": "array"},
                "confidence_score": {"type": "number"},
                "timestamp": {"type": "string"},
            },
        }


# Initialize storage
agent_storage = SqliteStorage(table_name="technical_analyst", db_file="tmp/agents.db")

# Create the Technical Analyst
technical_analyst = Agent(
    name="Technical Analyst",
    role="Perform technical analysis on subnet metrics",
    model=OpenAIChat(id="gpt-4o"),
    storage=agent_storage,
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    response_model=TechnicalAnalysis,
    status=DevelopmentStatus.EXPERIMENTAL,
    version="0.0.1",
    instructions=dedent(
        """\
        You are a technical analysis specialist for Bittensor subnets.
        
        Your analysis focus:
        1. Price Analysis:
           - Trend identification
           - Support/resistance levels
           - Chart patterns
           - Price action signals
        
        2. Volume Analysis:
           - Volume trends
           - Volume-price relationships
           - Accumulation/distribution
           - Market participation
        
        3. Technical Indicators:
           - Moving averages
           - RSI and momentum
           - MACD and trend
           - Volume indicators
        
        Analysis guidelines:
        1. Use multiple timeframes
        2. Confirm signals
        3. Consider context
        4. Update analysis
        5. Document findings
    """
    ),
)
