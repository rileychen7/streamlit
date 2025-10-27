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

with open("coding.json", "r") as f:
    lottie_coding_local = json.load(f)
with open("food.json", "r") as f:
    lottie_food_local = json.load(f)

# --- Custom CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

html, body, [class*="css"] {
  font-family: 'Roboto', sans-serif;
}

.section {
  background: linear-gradient(to right, #f5f5f5, #e0f7fa);
  color: #000;
  box-shadow: 0 8px 20px rgba(0,0,0,0.15);
  border-radius: 15px;
  padding: 40px 30px;
  margin-bottom: 30px;
}

.submit-btn {
  background-color: #e0f7fa;
  color: #000;
  padding: 12px 25px;
  border: none;
  cursor: pointer;
  border-radius: 8px;
  font-size: 16px;
}

.submit-btn:hover {
  transform: scale(1.05);
  opacity: 0.85;
}

input, textarea {
  background-color: #f0f0f0 !important;
  color: #000 !important;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  font-size: 16px;
}

a {
  color: inherit;
  text-decoration: none;
}

.feedback {
  display: flex;
  justify-content: center;
  gap: 12px;
  margin-bottom: 25px;
}

.feedback form {
  display: inline-block;
}

.feedback button {
  background: none;
  border: none;
  font-size: 26px;
  cursor: pointer;
  transition: transform 0.15s ease;
}

.feedback button:hover {
  transform: scale(1.2);
}
</style>
""", unsafe_allow_html=True)

# --- About Me Section ---
with st.container():
    st.subheader("Hello, I'm Riley :wave:")
    st.write("---")

    col1, col2, col3 = st.columns([1, 1.5, 1])

    with col1:
        st_lottie(lottie_coding, height=220, key="about_coding_lottie")

    with col2:
        st.markdown("""
        ###### 😄 Name: Riley Chen  
        ###### 📚 Study: Mathematics (Actuarial Science), Minor: Statistics  
        ###### 📍 Location: Buffalo, NY  
        ###### 🏋️ Interest: BJJ, Gym, Badminton, Soccer, Exploring cuisines  
        ###### 👀 Linkedin: [Link](https://www.linkedin.com/in/riley-chen--)  
        """)

# --- Projects Section ---
st.write("---")
st.header("My Projects")
st.write("##")

# Project 1
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        st_lottie(lottie_coding_local, height=220, key="personal_website")
    with col2:
        st.markdown('''
        <div class="section">
            <h2><a href="https://rileychen.streamlit.app/" target="_blank">Personal Website</a></h2>
            <p>You're currently viewing my personal website, built with Streamlit to showcase projects and insights. The platform includes an interactive contact form and feedback system.</p>
        </div>
        ''', unsafe_allow_html=True)

# Project 2
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        st_lottie(lottie_food_local, height=220, key="campus_crumbs")
    with col2:
        st.markdown('''
        <div class="section">
            <h2><a href="https://campuscrumbs.streamlit.app/" target="_blank">Campus Crumbs</a></h2>
            <p>Campus Crumbs lets UB students order from any campus dining location and have it delivered to their dorm in under 15 minutes — no need to step outside or pay delivery app fees.</p>
        </div>
        ''', unsafe_allow_html=True)

# --- Quick Feedback Section ---
st.write("---")
st.markdown("""
<div style="text-align:center; margin-bottom:5px;">
  <h3>Quick Feedback</h3>
  <p style="font-size:14px;">Tap an emoji to give 1-second feedback</p>
</div>

<div class="feedback">
  <form action="https://formsubmit.co/rchen92@buffalo.edu" method="POST">
    <input type="hidden" name="feedback" value="😍 Loved it!">
    <button type="submit">😍</button>
  </form>
  <form action="https://formsubmit.co/rchen92@buffalo.edu" method="POST">
    <input type="hidden" name="feedback" value="🙂 It was good!">
    <button type="submit">🙂</button>
  </form>
  <form action="https://formsubmit.co/rchen92@buffalo.edu" method="POST">
    <input type="hidden" name="feedback" value="😐 It's okay.">
    <button type="submit">😐</button>
  </form>
  <form action="https://formsubmit.co/rchen92@buffalo.edu" method="POST">
    <input type="hidden" name="feedback" value="😞 Needs improvement.">
    <button type="submit">😞</button>
  </form>
</div>
""", unsafe_allow_html=True)

# --- Contact Section ---
st.header("Contact Me")
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('''
    <div class="section" style="padding: 50px 40px;">
        <h2>Get in Touch</h2>
        <p>Have questions or want to get in touch? Use the form below!</p>
        <form action="https://formsubmit.co/rchen92@buffalo.edu" method="POST">
            <div style="margin-bottom: 20px;">
                <label for="email">Your Email:</label>
                <input type="email" id="email" name="email" required style="width: 100%;">
            </div>
            <div style="margin-bottom: 20px;">
                <label for="message">Your Message:</label>
                <textarea id="message" name="message" required style="width: 100%;"></textarea>
            </div>
            <button type="submit" class="submit-btn">Send</button>
        </form>
    </div>
    ''', unsafe_allow_html=True)
with col2:
    st.empty()
