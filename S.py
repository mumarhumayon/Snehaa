import streamlit as st
from datetime import datetime

# ---------------- PAGE SETTINGS ---------------- #
st.set_page_config(
    page_title="For Sneha ✨",
    page_icon="💖",
    layout="centered"
)

# ---------------- CSS FOR MOBILE ---------------- #
st.markdown("""
<style>
/* Remove default padding/margin */
.stApp {
    background: linear-gradient(135deg, #141e30, #243b55);
    min-height: 100vh;
}

.block-container {
    padding: 1rem !important;
    max-width: 100% !important;
}

/* Card - responsive */
.card {
    background: rgba(255,255,255,0.08);
    padding: 2rem 1.5rem;
    border-radius: 28px;
    text-align: center;
    margin: 1rem auto;
    backdrop-filter: blur(2px);
}

/* Mobile-friendly title */
.title {
    font-size: clamp(2.5rem, 8vw, 3.5rem);
    font-weight: bold;
    background: linear-gradient(to right, #ff4d6d, #ff85a1);
    background-clip: text;
    -webkit-background-clip: text;
    color: transparent;
    margin: 0.5rem 0;
}

/* Message text */
.msg {
    font-size: clamp(1rem, 4.5vw, 1.2rem);
    line-height: 1.7;
    color: #f1f1f1;
    margin: 1.5rem 0;
}

/* Highlight color */
.highlight {
    color: #ff9ecb;
    font-weight: 600;
}

/* Footer */
.footer {
    margin-top: 2rem;
    color: rgba(255,255,255,0.6);
    font-size: 0.8rem;
    font-style: italic;
}

/* Remove all Streamlit default elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Better touch targets on mobile */
div, span, p {
    -webkit-tap-highlight-color: transparent;
}
</style>
""", unsafe_allow_html=True)

today = datetime.now().strftime("%B %d, %Y")

# ---------------- MAIN CARD ---------------- #
html_code = f"""
<div class="card">
    <div style="font-size:1.2rem; color:#ffb3c6;">
        💌 A Special Message For
    </div>
    
    <div class="title">
        Sneha ✨
    </div>
    
    <div class="msg">
        Thank you for trusting me with your project ❤️
        <br><br>
        I've officially
        <span class="highlight">started working on the app</span>,
        and I'm genuinely excited to create something
        <span class="highlight">beautiful, modern, and impressive.</span> 💫
        <br><br>
        Every detail is being crafted with creativity,
        passion, and dedication because your project deserves nothing less 🌸
    </div>
    
    <div class="footer">
        Started on • {today}
    </div>
</div>
"""

st.markdown(html_code, unsafe_allow_html=True)

# ---------------- GENTLE EFFECTS ---------------- #
st.balloons()
