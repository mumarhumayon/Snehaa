import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="For Sneha ✨",
    page_icon="💫",
    layout="centered"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    color: white;
}

.main-card {
    margin-top: 40px;
    padding: 45px;
    border-radius: 30px;
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 8px 40px rgba(0,0,0,0.4);
    text-align: center;
    animation: fadeIn 1.2s ease-in-out;
}

.name {
    font-size: 72px;
    font-weight: 700;
    background: linear-gradient(90deg, #ff4d6d, #ff85a1, #ffd6e0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
    letter-spacing: 2px;
}

.heading {
    font-size: 22px;
    color: #f8f8f8;
    margin-bottom: 25px;
    font-weight: 500;
}

.message {
    font-size: 18px;
    color: #f1f1f1;
    line-height: 1.9;
    margin-top: 15px;
}

.highlight {
    color: #ff9ecb;
    font-weight: 600;
}

.custom-btn {
    margin-top: 30px;
    display: inline-block;
    padding: 14px 28px;
    border-radius: 50px;
    background: linear-gradient(90deg, #ff4d6d, #ff85a1);
    color: white;
    font-weight: 600;
    font-size: 16px;
    text-decoration: none;
    transition: 0.3s ease;
    box-shadow: 0 6px 20px rgba(255,77,109,0.4);
}

.custom-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 30px rgba(255,77,109,0.6);
}

.footer {
    margin-top: 30px;
    font-size: 14px;
    color: rgba(255,255,255,0.6);
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(25px);
    }
    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="main-card">

    <div class="heading">A Special Message For</div>

    <div class="name">Sneha ✨</div>

    <div class="message">
        Thank you for trusting me with your project. <br><br>

        I’ve officially <span class="highlight">started working on the app</span>,
        and I’m genuinely excited to turn your vision into something beautiful,
        modern, and impressive. 💫 <br><br>

        Every detail is being crafted with attention, creativity,
        and dedication because your project deserves nothing less. 🌸
    </div>

    <a class="custom-btn">
        Work In Progress 🚀
    </a>

    <div class="footer">
        Started on • {datetime.now().strftime("%B %d, %Y")}
    </div>

</div>
""", unsafe_allow_html=True)

st.balloons()

st.markdown("<br>", unsafe_allow_html=True)

st.success("The project journey has officially begun ✨")
