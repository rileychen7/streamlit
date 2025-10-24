import requests
import streamlit as st
from streamlit_lottie import st_lottie
import json

# --- Page Config ---
st.set_page_config(page_title="My Webpage", page_icon=":snake:", layout="wide")

# --- Load Lottie Animations ---
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottie("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# --- Load Local Lottie for Campus Crumbs ---
with open("food.json", "r") as f:
    lottie_food_local = json.load(f)

# --- Custom CSS ---
st.markdown(
    """
    <style>
    /* Custom font */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Roboto', sans-serif;
    }

    /* Section padding and rounded cards */
    .section {
        padding: 40px;
        border-radius: 15px;
        margin-bottom: 30px;
    }

    /* Button style */
    .submit-btn {
        background-color: #2ecc71;
        color: #fff;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
        border-radius: 5px;
        font-size: 16px;
    }

    .submit-btn:hover {
        background-color: #27ae60;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Header / About Me Section ---
with st.container():
    st.subheader("Hello, I'm Riley :wave:")
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.markdown(
            """
            <div class="section" style="background: linear-gradient(to right, #f5f5f5, #e0f7fa);">
                <h2>About Me</h2>
                <p>I am a junior at the University at Buffalo, majoring in Mathematics with a concentration in Actuarial Science, and a minor in Statistics.</p>
                <p>Outside of academics, I enjoy playing badminton, soccer, and exploring different cuisines. I’m excited to keep expanding my knowledge and embracing new challenges ahead.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# --- Projects Section ---
st.write("---")
st.header("My Projects")
st.write("##")

# --- Project 1: Personal Website ---
with st.container():
    st.markdown(
        '<div class="section" style="background: #fff; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">',
        unsafe_allow_html=True
    )
    col1, col2 = st.columns([1, 2])
    with col1:
        st_lottie(lottie_coding, height=300, key="personal_website")
    with col2:
        st.subheader("Personal Website")
        st.write(
            "You're currently viewing my personal website, built with Streamlit to showcase personal projects and insights. "
            "The platform features an interactive contact form and feedback system, boosting my website's user engagement by 52%. "
            "I will be continuing to add more content in the future!"
        )
    st.markdown("</div>", unsafe_allow_html=True)

# --- Project 2: Campus Crumbs ---
with st.container():
    st.markdown(
        '<div class="section" style="background: #fff; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">',
        unsafe_allow_html=True
    )
    col1, col2 = st.columns([1, 2])
    with col1:
        st_lottie(lottie_food_local, height=300, key="campus_crumbs")
    with col2:
        st.markdown(
            '### [Campus Crumbs](https://campuscrumbs.streamlit.app/)',
            unsafe_allow_html=True,
        )
        st.write(
            "There are days when the thought of leaving our dorms just to grab a meal feels like a task, "
            "especially when juggling assignments or feeling under the weather. While apps like UberEats and DoorDash exist, "
            "we, as budget-conscious college students, aim to save money and make the most of our prepaid meal plans. "
            "Order whatever's available from any dining option on campus and have your food delivered in less than 15 minutes. "
            "It's the ultimate solution for satisfying your cravings without the hassle, right at your dormsteps."
        )
    st.markdown("</div>", unsafe_allow_html=True)

# --- Contact Form ---
st.write("---")
st.header("Contact Me")

col1, col2 = st.columns([3, 1])

with col1:
    st.write("Have questions or want to get in touch? Use the form below to contact me!")
    st.markdown(
        f"""
        <form action="https://formsubmit.co/rchen92@buffalo.edu" method="POST">
            <div style="margin-bottom: 20px;">
                <label for="email" style="font-size: 18px;">Your Email:</label>
                <input type="email" id="email" name="email" required 
                    style="width: 100%; padding: 10px; font-size: 16px; background-color: #f0f0f0; border: 1px solid #ccc; border-radius: 5px;">
            </div>
            <div style="margin-bottom: 20px;">
                <label for="message" style="font-size: 18px;">Your Message:</label>
                <textarea id="message" name="message" required 
                    style="width: 100%; padding: 10px; font-size: 16px; background-color: #f0f0f0; border: 1px solid #ccc; border-radius: 5px;"></textarea>
            </div>
            <button type="submit" class="submit-btn">Send</button>
        </form>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.empty()
