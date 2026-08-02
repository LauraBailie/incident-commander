def analyze_incident(title, description):

    return {
        "summary": (
            f"Incident '{title}' affects the {description} "
            "service. AI recommendations will be available once "
            "Amazon Bedrock is configured."
        ),
        "severity": "Pending AI analysis",
        "recommendations": [
            "Verify service health",
            "Collect logs",
            "Notify stakeholders"
        ]
    }