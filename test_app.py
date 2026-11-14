from app import filter_high_severity_alerts


def test_filter_high_severity_alerts():
    sample = [
        {"id": "1", "severity": "high"},
        {"id": "2", "severity": "low"},
    ]
    result = filter_high_severity_alerts(sample)
    assert len(result) == 1
    assert result[0]["id"] == "1"