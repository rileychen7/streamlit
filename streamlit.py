import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Define the Lottie animation
def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Set Streamlit page config
st.set_page_config(page_title="My Webpage", page_icon=":snake:", layout="wide")

# Load Lottie animation
lottie_coding = load_lottieur("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# Navigation Bar
st.sidebar.title("Navigation")
sections = ["Home", "About Me", "My Projects", "Contact Me"]
selected_section = st.sidebar.radio("Go to", sections)

# Header
st.subheader("Hello, I'm Riley :wave:")

if selected_section == "Home":
    # Home section content
    pass
elif selected_section == "About Me":
    # About Me section content
    st.header("About Me")
    st.write("I am a freshman computer science student at the University at Buffalo, passionate about exploring the limitless possibilities of technology. Currently, I am diving deep into the world of Python and using it to help me build this personal website. But when I'm not immersed in the world of Python you can often find me playing badminton, soccer, or eating. I look forward to expanding my knowledge and taking on exciting challenges that lie ahead.")
    st_lottie(lottie_coding)
elif selected_section == "My Projects":
    # My Projects section content
    st.header("My Projects")
    
    # Add project images or icons
    project_images = [Image.open("project1.jpg"), Image.open("project2.jpg")]  # Replace with your image paths
    
    # Display images with descriptions
    for i, project_image in enumerate(project_images):
        st.image(project_image, caption=f"Project {i+1}")
        st.write("Description of the project.")
        
    # Add clickable links or buttons to learn more about each project
    if st.button("Learn more about Project 1"):
        st.write("Project 1 details")
    if st.button("Learn more about Project 2"):
        st.write("Project 2 details")
elif selected_section == "Contact Me":
    # Contact Me section content
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

# Footer
st.sidebar.markdown("---")
st.sidebar.write("© 2023 Your Name")

# Additional styling and clickable links can be added to each section as needed.
