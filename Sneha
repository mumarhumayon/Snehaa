import streamlit as st
from datetime import datetime

# ---------------- PAGE SETTINGS ---------------- #
st.set_page_config(
    page_title="For Sneha ✨",
    page_icon="💖",
    layout="centered"
)

# ---------------- CSS ---------------- #
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #141e30, #243b55);
    color: white;
}

/* Card */
.card {
    background: rgba(255,255,255,0.08);
    padding: 40px;
    border-radius: 25px;
    text-align: center;
    margin-top: 50px;
    box-shadow: 0px 8px 30px rgba(0,0,0,0.35);
}

/* Title */
.title {
    font-size: 60px;
    font-weight: bold;
    background: linear-gradient(to right, #ff4d6d, #ff85a1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Message */
.msg {
    font-size: 20px;
    line-height: 1.8;
    color: #f1f1f1;
}

/* Highlight */
.highlight {
    color: #ff9ecb;
    font-weight: bold;
}

/* Button */
.btn {
    margin-top: 25px;
    display: inline-block;
    padding: 12px 28px;
    border-radius: 40px;
    background: linear-gradient(to right, #ff4d6d, #ff85a1);
    color: white;
    font-size: 18px;
    font-weight: bold;
}

/* Footer */
.footer {
    margin-top: 20px;
    color: rgba(255,255,255,0.7);
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

today = datetime.now().strftime("%B %d, %Y")

# ---------------- MAIN CARD ---------------- #
html_code = f"""
<div class="card">

    <div style="font-size:22px;">
        💌 A Special Message For
    </div>

    <div class="title">
        Sneha ✨
    </div>

    <div class="msg">

        Thank you for trusting me with your project ❤️ <br><br>

        I've officially
        <span class="highlight">started working on the app</span>,
        and I'm genuinely excited to create something
        <span class="highlight">beautiful, modern, and impressive.</span> 💫
        <br><br>

        Every detail is being crafted with creativity,
        passion, and dedication because your project deserves nothing less 🌸

    </div>

    <div class="btn">
        🚀 Work In Progress
    </div>

    <div class="footer">
        Started on • {today}
    </div>

</div>
"""

st.markdown(html_code, unsafe_allow_html=True)

# ---------------- EFFECTS ---------------- #
st.balloons()

st.success("✨ The project journey has officially begun!")
