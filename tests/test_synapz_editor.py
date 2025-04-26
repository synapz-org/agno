"""Test suite for Synapz Editor agent functionality."""

import pytest
from pathlib import Path
import sys

# Add the project root to Python path
root_dir = str(Path(__file__).parent.parent)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from agents.creative.synapz_editor import agent


def test_agent_initialization():
    """Test that the agent is properly initialized with all components."""
    assert agent is not None
    assert agent.knowledge is not None
    assert agent.storage is not None
    assert agent.model is not None
    assert agent.tools is not None


def test_knowledge_base():
    """Test that the knowledge base can be queried."""
    # Test a simple query about Bittensor
    response = agent.run("What is Bittensor?")
    assert response is not None
    assert len(response.content) > 0


def test_vector_search():
    """Test that the vector database can perform semantic search."""
    # Test semantic search with similar but different queries
    response1 = agent.run("Explain decentralized AI")
    response2 = agent.run("Describe distributed artificial intelligence")

    # The responses should be similar in content
    assert response1 is not None
    assert response2 is not None
    assert len(response1.content) > 0
    assert len(response2.content) > 0


def test_session_storage():
    """Test that the session storage is working."""
    # Make a query
    initial_response = agent.run("What is Polkadot?")

    # Make a follow-up query that should use context
    followup_response = agent.run("How does it relate to JAM?")

    assert initial_response is not None
    assert followup_response is not None
    # The follow-up should reference Polkadot in its response
    assert "Polkadot" in followup_response.content


if __name__ == "__main__":
    pytest.main([__file__])
