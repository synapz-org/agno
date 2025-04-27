"""Alert Manager Agent - Notification and Monitoring Specialist

This agent manages alerts and notifications for Bittensor subnet price levels and
significant market events.
"""

from textwrap import dedent
from typing import Dict, List

from pydantic import BaseModel, Field

from agno.agent import Agent, DevelopmentStatus
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools


# Define structured output models
class AlertCriteria(BaseModel):
    subnet_id: int = Field(..., description="ID of the subnet")
    alert_type: str = Field(..., description="Type of alert")
    threshold: float = Field(..., description="Alert threshold value")
    timeframe: str = Field(..., description="Monitoring timeframe")
    priority: str = Field(..., description="Alert priority level")


class Alert(BaseModel):
    subnet_id: int = Field(..., description="ID of the subnet")
    alert_type: str = Field(..., description="Type of alert")
    trigger_value: float = Field(..., description="Value that triggered alert")
    threshold: float = Field(..., description="Alert threshold")
    severity: str = Field(..., description="Alert severity")
    timestamp: str = Field(..., description="Alert timestamp")
    context: str = Field(..., description="Alert context and details")


class AlertReport(BaseModel):
    timestamp: str = Field(..., description="Report generation timestamp")
    active_alerts: List[Alert] = Field(..., description="Current active alerts")
    alert_history: List[Alert] = Field(..., description="Recent alert history")
    summary: str = Field(..., description="Alert summary")

    class Config:
        json_schema_extra = {
            "required": ["timestamp", "active_alerts", "alert_history", "summary"],
            "properties": {
                "timestamp": {"type": "string"},
                "active_alerts": {"type": "array"},
                "alert_history": {"type": "array"},
                "summary": {"type": "string"},
            },
        }


# Initialize storage
agent_storage = SqliteStorage(table_name="alert_manager", db_file="tmp/agents.db")

# Create the Alert Manager
alert_manager = Agent(
    name="Alert Manager",
    role="Manage and trigger alerts based on subnet metrics",
    model=OpenAIChat(id="gpt-4o"),
    storage=agent_storage,
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    response_model=AlertReport,
    status=DevelopmentStatus.EXPERIMENTAL,
    version="0.0.1",
    instructions=dedent(
        """\
        You are an alert management specialist for Bittensor subnets.
        
        Your responsibilities:
        1. Alert Configuration:
           - Set price thresholds
           - Define metric triggers
           - Configure notification rules
        
        2. Alert Monitoring:
           - Track metric changes
           - Evaluate trigger conditions
           - Manage alert states
        
        3. Alert Actions:
           - Generate notifications
           - Escalate critical alerts
           - Update alert status
        
        Alert management guidelines:
        1. Monitor alert conditions
        2. Trigger appropriate actions
        3. Maintain alert history
        4. Handle alert resolution
        5. Report alert status
    """
    ),
)
