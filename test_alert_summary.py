from alert_summary import count_alerts_by_severity


def test_count_alerts_by_severity():
    alerts = [
        {"id": "1", "severity": "high"},
        {"id": "2", "severity": "low"},
        {"id": "3", "severity": "high"},
    ]

    result = count_alerts_by_severity(alerts)

    assert result["high"] == 2
    assert result["low"] == 1