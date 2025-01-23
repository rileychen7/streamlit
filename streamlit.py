from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Define the Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Set page configuration
st.set_page_config(page_title="Riley's Portfolio", page_icon=":snake:", layout="wide")

# Load Lottie animation
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# Custom CSS for styling
st.markdown("""
<style>
    .stButton>button {
        background-color: #2ecc71;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #f0f0f0;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #2c3e50;
    }
    .footer {
        text-align: center;
        padding: 20px;
        background-color: #f0f0f0;
        margin-top: 40px;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
with st.container():
    st.subheader("Hello, I'm Riley :wave:")
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write("##")
        st.write("""
        I am a sophomore at the University at Buffalo, majoring in Mathematics with a concentration in Actuarial Science. 
        Outside of academics, I enjoy playing badminton, soccer, and exploring different cuisines. 
        I’m excited to keep expanding my knowledge and embracing new challenges ahead.
        """)
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# Projects Section
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("streamlit_picture.png", use_container_width=True)
    with text_column:
        st.subheader("Personal Website")
        st.write("""
        You're currently viewing my personal website, built with Streamlit to showcase personal projects and insights. 
        The platform features an interactive contact form and feedback system, boosting my website's user engagement by 52%. 
        I will be continuing to add more content in the future!
        """)

# Contact Form Section
st.write("---")
st.header("Contact Me")

col1, col2 = st.columns([3, 1])

with col1:
    st.write("Have questions or want to get in touch? Use the form below to contact me!")
    st.markdown(
        f"""
        <form action="https://formsubmit.co/rchen92@buffalo.edu" method="POST">
            <div style="margin-bottom: 20px;">
                <label for="name" style="font-size: 18px;">Your Name:</label>
                <input type="text" id="name" name="name" required style="width: 100%; padding: 10px; font-size: 16px; background-color: #f0f0f0; border: 1px solid #ccc; border-radius: 5px;">
            </div>
            <div style="margin-bottom: 20px;">
                <label for="email" style="font-size: 18px;">Your Email:</label>
                <input type="email" id="email" name="email" required style="width: 100%; padding: 10px; font-size: 16px; background-color: #f0f0f0; border: 1px solid #ccc; border-radius: 5px;">
            </div>
            <div style="margin-bottom: 20px;">
                <label for="message" style="font-size: 18px;">Your Message:</label>
                <textarea id="message" name="message" required style="width: 100%; padding: 10px; font-size: 16px; background-color: #f0f0f0; border: 1px solid #ccc; border-radius: 5px;"></textarea>
            </div>
            <button type="submit" style="background-color: #2ecc71; color: #fff; padding: 10px 20px; border: none; cursor: pointer; border-radius: 5px;">Send</button>
        </form>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.empty()

# Footer Section
st.markdown("""
<div class="footer">
    <p>© 2023 Riley. All rights reserved.</p>
    <p>Connect with me on <a href="https://linkedin.com/in/riley" target="_blank">LinkedIn</a> | <a href="https://github.com/riley" target="_blank">GitHub</a></p>
</div>
""", unsafe_allow_html=True)
