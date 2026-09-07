import re

def analyze_message(message):
    text = message.lower()
    risk_score = 0
    detected = []

    # 1. Threat Detection
    threat_words = [
        "blocked", "block", "police", "legal action", 
        "arrest", "case", "penalty", "account will be closed"
    ]
    for word in threat_words:
        if word in text:
            risk_score += 25
            detected.append("Threatening Language")
            break

    # 2. Urgency Detection
    urgency_words = [
        "urgent", "immediately", "within 24 hours", 
        "quick", "expires today", "last chance"
    ]
    for word in urgency_words:
        if word in text:
            risk_score += 20
            detected.append("Urgency/Panic Inducing")
            break

    # 3. Suspicious Keywords (UPI / Bank KYC Frauds)
    fraud_keywords = [
        "kyc", "otp", "lottery", "cashback", "reward", 
        "claim", "refund", "won", "update pan"
    ]
    for word in fraud_keywords:
        if word in text:
            risk_score += 25
            detected.append(f"Suspicious Keyword: {word.upper()}")
            break

    # 4. Malicious Link Detection
    link_pattern = r"(https?://\S+|www\.\S+|bit\.ly/\S+|tinyurl\.com/\S+)"
    if re.search(link_pattern, text):
        risk_score += 30
        detected.append("Suspicious URL / Link")

    # 5. Risk Category Decision
    risk_score = min(risk_score, 100)
    if risk_score >= 60:
        status = "HIGH RISK (SCAM)"
    elif risk_score >= 30:
        status = "MODERATE RISK"
    else:
        status = "SAFE"

    return {
        "risk_score": risk_score,
        "status": status,
        "reasons": detected
    }