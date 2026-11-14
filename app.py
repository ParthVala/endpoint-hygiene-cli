import json


def filter_high_severity_alerts(alerts: list[dict]) -> list[dict]:
    """Filter alerts to return only high or critical severity."""
    return [
        alert
        for alert in alerts
        if alert.get("severity", "").lower() in ("high", "critical")
    ]


if __name__ == "__main__":
    # Simulated JSON response from Microsoft Graph / CrowdStrike FalconPy
    sample_alerts = [
        {"id": "101", "title": "Suspicious PowerShell", "severity": "high"},
        {"id": "102", "title": "USB Blocked", "severity": "low"},
        {"id": "103", "title": "Mimikatz Detected", "severity": "critical"},
    ]
    high_alerts = filter_high_severity_alerts(sample_alerts)
    print(json.dumps(high_alerts, indent=2))