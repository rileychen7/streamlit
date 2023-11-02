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
    st.write("...")
    st_lottie(lottie_coding)
elif selected_section == "My Projects":
    # My Projects section content
    st.header("My Projects")
    st.write("...")
elif selected_section == "Contact Me":
    # Contact Me section content
    st.header("Contact Me")
    st.write("...")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("© 2023 Your Name")

# Additional styling and clickable links can be added to each section as needed.
