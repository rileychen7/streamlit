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

with st.container():
    st.write("---")

    # 💬 Quick Emoji Feedback (Top Section)
    st.markdown("""
    <div style="text-align:center; margin-bottom: 30px;">
        <h4 style="margin-bottom:10px;">Quick feedback</h4>
        <p style="font-size:15px; color:gray; margin-top:-5px;">Tap an emoji to give 1-second feedback. It sends your response to me instantly.</p>
        <form action="https://formsubmit.co/rchen92@buffalo.edu" method="POST" style="margin-top:10px;">
            <input type="hidden" name="_subject" value="Quick Emoji Feedback">
            <input type="hidden" name="_captcha" value="false">
            <button type="submit" name="feedback" value="😀" style="background:none;border:none;font-size:30px;cursor:pointer;">😀</button>
            <button type="submit" name="feedback" value="😐" style="background:none;border:none;font-size:30px;cursor:pointer;">😐</button>
            <button type="submit" name="feedback" value="😞" style="background:none;border:none;font-size:30px;cursor:pointer;">😞</button>
        </form>
    </div>
    """, unsafe_allow_html=True)

    # 📬 Contact Form (Below)
    contact_form = """
    <form action="https://formsubmit.co/rchen92@buffalo.edu" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_subject" value="New Contact Message from Riley's Portfolio">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

    # 🎨 Styling (keeps your clean light look)
    st.markdown("""
        <style>
        form {
            text-align: left;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            border: 1px solid #ccc;
            border-radius: 8px;
            font-family: "Inter", sans-serif;
            font-size: 15px;
        }
        textarea {
            height: 120px;
        }
        button {
            background-color: #111;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 500;
            transition: 0.2s ease;
        }
        button:hover {
            background-color: #333;
        }
        </style>
    """, unsafe_allow_html=True)
