"""Test script for financial monitoring agents.

This script tests the structured output of our financial monitoring agents:
- Subnet Monitor
- Technical Analyst
- Alert Manager
"""

from datetime import datetime

from subnet_monitor import subnet_monitor, SubnetMetrics, MonitoringReport
from technical_analyst import technical_analyst, TechnicalAnalysis, TechnicalIndicators
from alert_manager import alert_manager, Alert, AlertReport, AlertCriteria


def test_subnet_monitor():
    """Test the subnet monitor's structured output."""
    print("\nTesting Subnet Monitor...")

    # Test monitoring specific subnets
    response = subnet_monitor.run(
        "Monitor subnet 1 and subnet 5 for price action and network metrics."
    )

    # Verify response structure
    assert isinstance(response.content, MonitoringReport)
    assert isinstance(response.content.subnet_metrics, list)
    assert all(isinstance(m, SubnetMetrics) for m in response.content.subnet_metrics)

    print("Subnet Monitor test passed!")
    print(f"Report summary: {response.content.summary}")


def test_technical_analyst():
    """Test the technical analyst's structured output."""
    print("\nTesting Technical Analyst...")

    # Test technical analysis
    response = technical_analyst.run(
        "Analyze subnet 1's price action and identify key levels."
    )

    # Verify response structure
    assert isinstance(response.content, TechnicalAnalysis)
    assert isinstance(response.content.indicators, TechnicalIndicators)
    assert isinstance(response.content.key_levels, dict)

    print("Technical Analyst test passed!")
    print(f"Analysis confidence: {response.content.confidence_score}")


def test_alert_manager():
    """Test the alert manager's structured output."""
    print("\nTesting Alert Manager...")

    # Test alert setup
    response = alert_manager.run(
        "Set up price alerts for subnet 1 at $500 and subnet 5 at $300."
    )

    # Verify response structure
    assert isinstance(response.content, AlertReport)
    assert isinstance(response.content.active_alerts, list)
    assert all(isinstance(a, Alert) for a in response.content.active_alerts)

    print("Alert Manager test passed!")
    print(f"Active alerts: {len(response.content.active_alerts)}")


def main():
    """Run all tests."""
    print("Starting financial agent tests...")

    try:
        test_subnet_monitor()
        test_technical_analyst()
        test_alert_manager()

        print("\nAll tests passed successfully!")
    except Exception as e:
        print(f"\nTest failed: {str(e)}")


if __name__ == "__main__":
    main()
