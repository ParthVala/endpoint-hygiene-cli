def count_alerts_by_severity(alerts: list[dict]) -> dict:
    """Count security alerts by severity."""

    summary = {}

    for alert in alerts:
        severity = alert.get("severity", "unknown").lower()
        summary[severity] = summary.get(severity, 0) + 1

    return summary


if __name__ == "__main__":
    sample_alerts = [
        {"id": "101", "severity": "high"},
        {"id": "102", "severity": "low"},
        {"id": "103", "severity": "critical"},
        {"id": "104", "severity": "high"},
    ]

    print(count_alerts_by_severity(sample_alerts))