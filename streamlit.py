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
with st.container():
    st.write("---")
    st.header("Contact Me")
    st.write("##")
    st.write("Have questions or want to get in touch? Use the form below to contact me!")

    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Submit"):
        if email and message:
            try:
                smtp_server = "smtp.gmail.com"
                smtp_port = 587
                smtp_username = "rileychen2005@gmail.com"
                smtp_password = "Nexuss2005"
                sender_email = "your_email@gmail.com"
                receiver_email = "rileychen2005@example.com"  

                msg = MIMEMultipart()
                msg["From"] = sender_email
                msg["To"] = receiver_email
                msg["Subject"] = "Contact Form Submission"

                msg.attach(MIMEText(f"From: {email}\n\nMessage:\n{message}", "plain"))

                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(smtp_username, smtp_password)
                    server.sendmail(sender_email, receiver_email, msg.as_string())

                st.success("Message sent successfully!")
            except Exception as e:
                st.error(f"Error sending message: {e}")
        else:
            st.error("Please fill in both your email and message.")
