"""Subnet Monitor Agent - Bittensor Subnet Tracking Specialist

This agent monitors Bittensor subnets on taostats.io, tracking performance metrics
and price action.
"""

from textwrap import dedent
from typing import Dict, List

from pydantic import BaseModel, Field

from agno.agent import Agent, DevelopmentStatus
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools


# Define structured output models
class SubnetMetrics(BaseModel):
    subnet_id: int = Field(..., description="ID of the subnet")
    current_price: float = Field(..., description="Current price in TAO")
    volume_24h: float = Field(..., description="24-hour trading volume")
    validator_count: int = Field(..., description="Number of active validators")
    network_health: float = Field(..., description="Network health score (0-1)")
    last_updated: str = Field(..., description="Timestamp of last update")


class MonitoringReport(BaseModel):
    timestamp: str = Field(..., description="Report generation timestamp")
    subnet_metrics: List[SubnetMetrics] = Field(
        ..., description="Metrics for monitored subnets"
    )
    significant_changes: Dict[str, float] = Field(
        ..., description="Significant metric changes"
    )
    summary: str = Field(..., description="Summary of subnet performance")

    class Config:
        json_schema_extra = {
            "required": [
                "timestamp",
                "subnet_metrics",
                "significant_changes",
                "summary",
            ],
            "properties": {
                "timestamp": {"type": "string"},
                "subnet_metrics": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "subnet_id": {"type": "integer"},
                            "current_price": {"type": "number"},
                            "volume_24h": {"type": "number"},
                            "validator_count": {"type": "integer"},
                            "network_health": {"type": "number"},
                            "last_updated": {"type": "string"},
                        },
                    },
                },
                "significant_changes": {
                    "type": "object",
                    "additionalProperties": {"type": "number"},
                },
                "summary": {"type": "string"},
            },
        }


# Initialize storage
agent_storage = SqliteStorage(table_name="subnet_monitor", db_file="tmp/agents.db")

# Create the Subnet Monitor
subnet_monitor = Agent(
    name="Subnet Monitor",
    role="Track subnet performance and metrics",
    model=OpenAIChat(id="gpt-4o"),
    storage=agent_storage,
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    response_model=MonitoringReport,
    status=DevelopmentStatus.EXPERIMENTAL,
    version="0.0.1",
    instructions=dedent(
        """\
        You are a subnet monitoring specialist for Bittensor.
        
        Your monitoring focus:
        1. Price Action:
           - Current price levels
           - Price movements
           - Volume analysis
           - Market depth
        
        2. Network Metrics:
           - Validator count
           - Network participation
           - Emission rates
           - Protocol updates
        
        3. Performance Tracking:
           - ROI metrics
           - Network growth
           - Validator performance
           - Protocol efficiency
        
        Monitoring guidelines:
        1. Track specified subnets
        2. Identify significant changes
        3. Monitor network health
        4. Track validator activity
        5. Report key metrics
    """
    ),
)
