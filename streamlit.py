import requests
import streamlit as st
from streamlit_lottie import st_lottie
import json
import os

# --- Page Config ---
st.set_page_config(page_title="My Webpage", page_icon=":snake:", layout="wide")

# --- Load Lottie Animations ---
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

# --- Detect Streamlit Theme ---
is_dark = st.get_option("theme.base") == "dark"
card_bg = "#1e1e1e" if is_dark else "#fff"
text_color = "#f5f5f5" if is_dark else "#000"
input_bg = "#2e2e2e" if is_dark else "#f0f0f0"
input_text = "#f5f5f5" if is_dark else "#000"

# --- Custom CSS ---
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

html, body, [class*="css"] {{
  font-family: 'Roboto', sans-serif;
}}

.section {{
  background: linear-gradient(to right, #f5f5f5, #e0f7fa);
  color: {text_color};
  box-shadow: 0 8px 20px rgba(0,0,0,0.15);
  border-radius: 15px;
  padding: 40px 30px;
  margin-bottom: 30px;
}}

.submit-btn {{
  background-color: #e0f7fa;
  color: {text_color};
  padding: 12px 25px;
  border: none;
  cursor: pointer;
  border-radius: 8px;
  font-size: 16px;
}}
.submit-btn:hover {{
  transform: scale(1.05);
  opacity: 0.85;
}}

input, textarea {{
  background-color: {input_bg} !important;
  color: {input_text} !important;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  font-size: 16px;
}}

/* Fix for blue/underlined links */
a {{
  color: inherit !important;
  text-decoration: none !important;
  font-weight: 500;
  transition: 0.2s ease;
}}
a:hover {{
  color: #555 !important;
  text-decoration: underline !important;
}}
</style>
""", unsafe_allow_html=True)

# --- About Me Section ---
with st.container():
    st.subheader("Hello, I'm Riley :wave:")
    st.write("---")

    # Three columns: Lottie | Info | Portrait
    col1, col2, col3 = st.columns([1, 1.5, 1])

    with col1:
        st_lottie(lottie_coding, height=220, key="about_coding_lottie")

    with col2:
        st.markdown(f"###### 😄 Name: Riley Chen")
        st.markdown(f"###### 📚 Study: Mathematics (Actuarial Science), Minor: Statistics")
        st.markdown(f"###### 📍 Location: Buffalo, NY")
        st.markdown(f"###### 🏋️ Interest: BJJ, Gym, Badminton, Soccer, Exploring cuisines")
        st.markdown(f"###### 👀 Linkedin: [Link](https://www.linkedin.com/in/riley-chen--)")

# --- Projects Section ---
st.write("---")
st.header("My Projects")
st.write("##")

# Project 1: Personal Website
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        st_lottie(lottie_coding_local, height=220, key="personal_website")
    with col2:
        st.markdown(f'''
        <div class="section">
            <h2><a href="https://rileychen.streamlit.app/" target="_blank">Personal Website</a></h2>
            <p>You're currently viewing my personal website, built with Streamlit to showcase personal projects and insights. The platform features an interactive contact form and feedback system, boosting my website's user engagement by 52%. I will be continuing to add more content in the future!</p>
        </div>
        ''', unsafe_allow_html=True)

# Project 2: Campus Crumbs
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        st_lottie(lottie_food_local, height=220, key="campus_crumbs")
    with col2:
        st.markdown(f'''
        <div class="section">
            <h2><a href="https://campuscrumbs.streamlit.app/" target="_blank">Campus Crumbs</a></h2>
            <p>There are days when the thought of leaving our dorms just to grab a meal feels like a task, especially when juggling assignments or feeling under the weather. While apps like UberEats and DoorDash exist, we, as budget-conscious college students, aim to save money and make the most of our prepaid meal plans. Order whatever's available from any dining option on campus and have your food delivered in less than 15 minutes. It's the ultimate solution for satisfying your cravings without the hassle, right at your dormsteps.</p>
        </div>
        ''', unsafe_allow_html=True)

# --- Feedback Section ---
st.write("---")
st.markdown("""
<div class="section" style="padding: 20px; text-align:center;">
  <h4 style="margin-bottom: 15px;">Quick Feedback</h4>
  <p>Tap an emoji to give 1-second feedback. It sends your response to my inbox instantly.</p>
  <form action="https://formsubmit.co/rchen92@buffalo.edu" method="POST">
    <button name="feedback" value="😀" style="font-size:28px; background:none; border:none; cursor:pointer;">😀</button>
    <button name="feedback" value="😐" style="font-size:28px; background:none; border:none; cursor:pointer;">😐</button>
    <button name="feedback" value="😞" style="font-size:28px; background:none; border:none; cursor:pointer;">😞</button>
  </form>
</div>
""", unsafe_allow_html=True)

# --- Contact Form Section ---
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown(f'''
    <div class="section" style="padding: 50px 40px;">
        <h2>Get in Touch</h2>
        <p style="max-width: 100%;">Have questions or want to get in touch? Use the form below!</p>
        <form action="https://formsubmit.co/rchen92@buffalo.edu" method="POST" style="max-width: 100%;">
            <div style="margin-bottom: 20px;">
                <label for="email" style="font-size: 18px;">Your Email:</label>
                <input type="email" id="email" name="email" required style="width: 100%; padding: 12px; font-size: 16px; border-radius: 5px; border: 1px solid #ccc;">
            </div>
            <div style="margin-bottom: 20px;">
                <label for="message" style="font-size: 18px;">Your Message:</label>
                <textarea id="message" name="message" required style="width: 100%; padding: 12px; font-size: 16px; border-radius: 5px; border: 1px solid #ccc;"></textarea>
            </div>
            <button type="submit" class="submit-btn">Send</button>
        </form>
    </div>
    ''', unsafe_allow_html=True)
