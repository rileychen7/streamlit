import streamlit as st
from streamlit_lottie import st_lottie
import json
import os
import requests
import smtplib
from email.message import EmailMessage

# ================== CONFIG ==================
st.set_page_config(page_title="Riley Chen — Portfolio", page_icon=":snake:", layout="wide")

EMAIL_ADDRESS = "rchen92@buffalo.edu"  # your email
EMAIL_PASSWORD = "YOUR_APP_PASSWORD"   # app password for SMTP (Gmail example)

# Colors
ACCENT = "#00a6c6"
BG_LIGHT = "#f6fbfc"
CARD_LIGHT = "#ffffff"
TEXT_LIGHT = "#0b1114"
INPUT_BG = "#f0f0f0"
INPUT_TEXT = "#000"

# ================== LOTTIE ==================
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottie("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# Local Lottie files
with open("coding.json", "r") as f:
    lottie_coding_local = json.load(f)
with open("food.json", "r") as f:
    lottie_food_local = json.load(f)

# ================== CSS ==================
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

html, body, [class*="css"] {{
    font-family: 'Roboto', sans-serif;
    background: {BG_LIGHT};
    color: {TEXT_LIGHT};
}}
.section {{
    background: {CARD_LIGHT};
    color: {TEXT_LIGHT};
    box-shadow: 0 8px 24px rgba(0,0,0,0.06);
    border-radius: 14px;
    padding: 28px;
    margin-bottom: 28px;
}}
.card:hover {{
    transform: translateY(-6px) scale(1.01);
    box-shadow: 0 14px 36px rgba(0,0,0,0.12);
}}
.project-title a {{
    color: inherit;
    text-decoration: none;
}}
.project-title a:hover {{
    text-decoration: underline;
}}
input, textarea {{
    background-color: {INPUT_BG} !important;
    color: {INPUT_TEXT} !important;
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 10px;
    font-size: 16px;
}}
.submit-btn {{
    background-color: {ACCENT};
    color: white;
    padding: 10px 16px;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    cursor: pointer;
}}
.submit-btn:hover {{
    transform: translateY(-3px);
    opacity: 0.95;
}}
.feedback-box {{
    background: #ffffff;
    border-radius: 12px;
    padding: 10px;
    margin-bottom: 20px;
}}
.feedback-btn {{
    font-size: 24px;
    margin-right: 12px;
    cursor: pointer;
    border: none;
    background: transparent;
}}
</style>
""", unsafe_allow_html=True)

# ================== ABOUT ==================
with st.container():
    st.subheader("Hello, I'm Riley :wave:")
    st.write("---")
    col1, col2, col3 = st.columns([1,1.5,1])
    with col1:
        st_lottie(lottie_coding, height=220, key="about_coding_lottie")
    with col2:
        st.markdown(f"###### 😄 Name: Riley Chen")
        st.markdown(f"###### 📚 Study: Mathematics (Actuarial Science), Minor: Statistics")
        st.markdown(f"###### 📍 Location: Buffalo, NY")
        st.markdown(f"###### 🏋️ Interest: BJJ, Gym, Badminton, Soccer, Exploring cuisines")
        st.markdown(f"###### 👀 Linkedin: [Link](https://www.linkedin.com/in/riley-chen--)")
    with col3:
        st.empty()

# ================== PROJECTS ==================
st.write("---")
st.header("My Projects")
st.write("##")

# Project 1
with st.container():
    col1, col2 = st.columns([1,2])
    with col1:
        st_lottie(lottie_coding_local, height=220, key="personal_website")
    with col2:
        st.markdown(f'''
        <div class="section project-title">
        <h2><a href="https://rileychen.streamlit.app/" target="_blank">Personal Website</a></h2>
        <p>You're currently viewing my personal website, built with Streamlit to showcase personal projects and insights. The platform features an interactive contact form and feedback system, boosting user engagement by 52%. More content will be added soon!</p>
        </div>
        ''', unsafe_allow_html=True)

# Project 2
with st.container():
    col1, col2 = st.columns([1,2])
    with col1:
        st_lottie(lottie_food_local, height=220, key="campus_crumbs")
    with col2:
        st.markdown(f'''
        <div class="section project-title">
        <h2><a href="https://campuscrumbs.streamlit.app/" target="_blank">Campus Crumbs</a></h2>
        <p>A dorm food delivery platform for budget-conscious students using campus meal plans. Order available meals from any dining option on campus in under 15 minutes.</p>
        </div>
        ''', unsafe_allow_html=True)

# ================== EMOJI FEEDBACK ==================
st.markdown('<div class="feedback-box">Quick feedback: Tap an emoji to give 1-second feedback.</div>', unsafe_allow_html=True)
feedback_col1, feedback_col2, feedback_col3 = st.columns([1,1,3])
with feedback_col1:
    if st.button("❤️ Love it"):
        try:
            requests.post(f"https://formsubmit.co/{EMAIL_ADDRESS}", data={"feedback":"love it"})
        except:
            pass
with feedback_col2:
    if st.button("😐 Meh"):
        try:
            requests.post(f"https://formsubmit.co/{EMAIL_ADDRESS}", data={"feedback":"meh"})
        except:
            pass
with feedback_col3:
    if st.button("👎 Not for me"):
        try:
            requests.post(f"https://formsubmit.co/{EMAIL_ADDRESS}", data={"feedback":"not for me"})
        except:
            pass

# ================== CONTACT FORM ==================
st.write("---")
with st.container():
    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.markdown("### Get In Touch With Me!")
        with st.form("contact_form"):
            name = st.text_input("Your name")
            email = st.text_input("Your email")
            message = st.text_area("Your message here")
            submitted = st.form_submit_button("Send")
            if submitted:
                if not name or not email or not message:
                    st.error("Please fill out all fields")
                else:
                    try:
                        msg = EmailMessage()
                        msg['Subject'] = f'New message from {name}'
                        msg['From'] = email
                        msg['To'] = EMAIL_ADDRESS
                        msg.set_content(f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")
                        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                            smtp.send_message(msg)
                        st.success("✅ Message sent successfully!")
                    except Exception as e:
                        st.error(f"Error sending message: {e}")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.empty()
