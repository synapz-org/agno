from enum import Enum
from typing import List, Optional, Type, Callable

from pydantic import BaseModel

from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage


class DevelopmentStatus(Enum):
    """Development status of an agent."""

    EXPERIMENTAL = "experimental"  # Early development, unstable
    BETA = "beta"  # Testing phase, major features complete
    STABLE = "stable"  # Production ready, well tested
    DEPRECATED = "deprecated"  # No longer maintained


class Agent:
    def __init__(
        self,
        name: str,
        role: str,
        model: OpenAIChat,
        storage: Optional[SqliteStorage] = None,
        tools: Optional[List[Callable]] = None,
        show_tool_calls: bool = False,
        markdown: bool = False,
        response_model: Optional[Type[BaseModel]] = None,
        instructions: Optional[str] = None,
        status: DevelopmentStatus = DevelopmentStatus.EXPERIMENTAL,
        version: str = "0.1.0",
    ):
        self.name = name
        self.role = role
        self.model = model
        self.storage = storage
        self.tools = tools or []
        self.show_tool_calls = show_tool_calls
        self.markdown = markdown
        self.response_model = response_model
        self.instructions = instructions
        self.status = status
        self.version = version

    def get_status_info(self) -> str:
        """Get formatted status information."""
        return f"{self.name} v{self.version} ({self.status.value})"
