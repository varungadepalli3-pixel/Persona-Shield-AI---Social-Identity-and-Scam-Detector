import streamlit as st
from backend import predict_profile

st.set_page_config(page_title="PersonaShield AI", page_icon="🛡️", layout="centered")

st.markdown("<h1 style='text-align:center;'>🛡️ PersonaShield AI</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:gray;'>Social Identity Scam Detector</h4>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("### 📋 Enter Profile Details")

col1, col2 = st.columns(2)

with col1:
    followers  = st.number_input("👥 Followers",  min_value=0, value=0, step=1)
    posts      = st.number_input("📸 Posts",      min_value=0, value=0, step=1)
    has_pic    = st.selectbox("🖼️ Profile Picture", ["Yes", "No"])

with col2:
    following  = st.number_input("➕ Following",  min_value=0, value=0, step=1)
    bio_length = st.number_input("📝 Bio Length (characters)", min_value=0, value=0, step=1)
    scam_type  = st.selectbox("🎯 Suspected Scam Type", [
        "None / Not Sure", "Romance Scam", "Job Scam",
        "Investment Scam", "Impersonation", "Prize/Lottery"
    ])

st.markdown("---")

if st.button("🔍 Analyze Profile", use_container_width=True):

    has_profile_pic = True if has_pic == "Yes" else False

    trust_score, prediction, explanation, risk_level = predict_profile(
        followers, following, posts, bio_length, has_profile_pic, scam_type
    )

    st.markdown("## 📊 Analysis Result")

    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        st.metric(label="🔒 Trust Score", value=f"{trust_score} / 100")
        st.progress(trust_score / 100)

    st.markdown("<br>", unsafe_allow_html=True)

    if trust_score >= 70:
        st.success(f"**Prediction: {prediction}**")
    elif trust_score >= 40:
        st.warning(f"**Prediction: {prediction}**")
    else:
        st.error(f"**Prediction: {prediction}**")

    st.markdown("---")
    st.markdown("### 🤖 AI Analysis Report")
    st.markdown(explanation)

    st.markdown("---")
    st.caption("PersonaShield AI — Mini Project | GenAI Internship 2026")