from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define the Lottie animation loading function
def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Set Streamlit page config
st.set_page_config(page_title="My Webpage", page_icon=":snake:", layout="wide")

# Load Lottie animation
lottie_coding = load_lottieur("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# Header
with st.container():
    st.subheader("Hello, I'm Riley :wave:")

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("About Me")
            st.write("##")
            st.write("""I am a freshman computer science student at the University at Buffalo, passionate about exploring the limitless possibilities of technology.
Currently, I am diving deep into the world of Python and using it to help me build this personal website. But when I'm not immersed in the world of Python you can often find me playing
badminton, soccer, or eating. I look forward to expanding my knowledge and taking on exciting challenges that lie ahead.""")

    # Display the Lottie animation
    with right_column:
        st_lottie(lottie_coding)

# Projects
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))

    with image_column:
       
        pass

    with text_column:
        st.subheader("Personal Website")
        st.write("""-Leveraged Streamlit to create a dynamic personal website, highlighting industry insights and accomplishments, resulting in an enhanced online presence. 
        Developing a visually captivating and interactive platform not only enhanced the accessibility of accomplishments but also substantially magnified visibility in the expansive digital landscape.
        Through the implementation of a user-friendly contact form and feedback system, the personal website experienced a 50% rise in user-provided insights and networking connections, 
        resulting in an enhanced online presence and increased visibility in the digital landscape.""")


# Contact Form
st.write("---")
st.header("Contact Me")

col1, col2 = st.columns([3, 1])  

email_input_width = "100%"  
message_input_width = "100%"  

with col1:
    st.write("Have questions or want to get in touch? Use the form below to contact me!")

    st.markdown(
        f"""
        <form action="https://formsubmit.co/rchen92@buffalo.edu" method="POST">
            <div style="margin-bottom: 20px;">
                <label for="email" style="font-size: 18px;">Your Email:</label>
                <input type="email" id="email" name="email" required style="width: {email_input_width}; padding: 10px; font-size: 16px; background-color: #f0f0f0; border: 1px solid #ccc; border-radius: 5px;">
            </div>
            <div style="margin-bottom: 20px;">
                <label for "message" style="font-size: 18px;">Your Message:</label>
                <textarea id="message" name="message" required style="width: {message_input_width}; padding: 10px; font-size: 16px; background-color: #f0f0f0; border: 1px solid #ccc; border-radius: 5px;"></textarea>
            </div>
            <button type="submit" style="background-color: #2ecc71; color: #fff; padding: 10px 20px; border: none; cursor: pointer; border-radius: 5px;">Send</button>
        </form>
        """,
        unsafe_allow_html=True,
    )

# Right Column - Empty Space
with col2:
    st.empty()
