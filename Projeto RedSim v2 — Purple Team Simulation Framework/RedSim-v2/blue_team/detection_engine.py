def analyze_event(event):
    alerts = []

    if event.get("technique") == "T1547":
        alerts.append({
            "severity": "HIGH",
            "message": "Persistence technique detected",
            "mitre": "T1547"
        })

    if event.get("technique") == "T1071":
        alerts.append({
            "severity": "MEDIUM",
            "message": "Possible C2 communication",
            "mitre": "T1071"
        })

    return alerts
