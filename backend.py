import random

def predict_profile(followers, following, posts, bio_length, has_profile_pic, scam_type):

    trust_score = 100
    red_flags = []
    green_flags = []

    if followers < 50:
        trust_score -= 30
        red_flags.append("Very few followers — typical of newly created fake accounts.")
    else:
        green_flags.append("Decent follower count adds credibility.")

    if following > 0 and followers > 0 and (following / max(followers, 1)) > 5:
        trust_score -= 25
        red_flags.append("Following far more accounts than followers — mass-follow scam tactic.")

    if posts < 5:
        trust_score -= 20
        red_flags.append("Almost no posts — profile likely created recently for scam purposes.")
    else:
        green_flags.append("Regular posting history is a positive sign.")

    if bio_length < 10:
        trust_score -= 15
        red_flags.append("Very short or empty bio — genuine users usually describe themselves.")
    else:
        green_flags.append("Bio is filled out — adds authenticity.")

    if not has_profile_pic:
        trust_score -= 10
        red_flags.append("No profile picture — common in bot and scam accounts.")
    else:
        green_flags.append("Profile picture is present.")

    trust_score = max(0, min(100, trust_score))

    if trust_score >= 70:
        prediction = "✅ Genuine Profile"
        risk_level = "LOW RISK"
    elif trust_score >= 40:
        prediction = "⚠️ Suspicious Profile"
        risk_level = "MEDIUM RISK"
    else:
        prediction = "🚨 Scam Profile Detected"
        risk_level = "HIGH RISK"

    scam_labels = {
        "Romance Scam":    "💔 Romance Scam — builds emotional relationships to extract money.",
        "Job Scam":        "💼 Job Scam — offers fake jobs to collect personal info or fees.",
        "Investment Scam": "📈 Investment/Crypto Scam — promises high returns to steal funds.",
        "Impersonation":   "🎭 Impersonation — pretends to be a known person or brand.",
        "Prize/Lottery":   "🎁 Prize/Lottery Scam — claims you won a prize to get your details.",
        "None / Not Sure": "🔍 No specific scam type selected.",
    }
    scam_detail = scam_labels.get(scam_type, "Unknown")

    explanation = f"""
**Risk Level: {risk_level}**

**Profile Summary:**
- Followers: {followers} | Following: {following} | Posts: {posts}
- Bio Length: {bio_length} characters | Profile Picture: {"Yes" if has_profile_pic else "No"}
- Scam Type Selected: {scam_type}

**🚩 Red Flags Detected ({len(red_flags)}):**
"""
    if red_flags:
        for flag in red_flags:
            explanation += f"\n- {flag}"
    else:
        explanation += "\n- No major red flags found."

    explanation += f"""

**✅ Positive Signals ({len(green_flags)}):**
"""
    if green_flags:
        for g in green_flags:
            explanation += f"\n- {g}"
    else:
        explanation += "\n- No positive signals found."

    explanation += f"""

**🔍 Scam Pattern Analysis:**
{scam_detail}

**🛡️ Safety Recommendations:**
"""
    if trust_score < 40:
        explanation += """
- Do NOT share personal information with this account.
- Do NOT send money or click any links they share.
- Report this profile to the platform immediately.
- Block the account to prevent further contact."""
    elif trust_score < 70:
        explanation += """
- Be cautious before trusting this profile.
- Verify their identity through other channels before sharing information.
- Avoid financial transactions with this account."""
    else:
        explanation += """
- Profile appears genuine based on available signals.
- Always stay cautious online — even genuine-looking profiles can be compromised.
- Never share passwords or financial details."""

    return trust_score, prediction, explanation, risk_level