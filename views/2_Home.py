import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animations from a URL
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error loading Lottie animation: {e}")
        return None

# Load the Lottie animation
lottie_coding = load_lottieurl("https://lottie.host/89abf601-d767-4328-b0ab-76e2bdbd7733/JH0aBcvx6L.json")

# Streamlit layout
with st.container():
    st.title("Welcome to Ryan's Biography!")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    
    with left_column:
        st.header("Who am I?")
        st.write(
            """
            Hi, I'm **Joseph Ryan B. Ruperez**. 

            A first-year **Computer Engineering** student from **Surigao del Norte State University**.

            To know more about me, check the tabs on the left side. 
            """
        )

    with right_column:
        if lottie_coding:
            st_lottie(lottie_coding, height=300, key="coding")
        else:
            st.error("Lottie animation failed to load. Please check the URL or try again later.")

with st.container():
    st.write("---")
    st.subheader("Connect with Me")

socials = {
    "Instagram": {
        "url": "https://www.instagram.com/curriedawson01/profilecard/?igsh=MXhtdTZsejQ5eDNiMg==",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"
    },
    "Facebook": {
        "url": "https://www.facebook.com/share/nUCFEEMoznRVhzP7/",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg"
    }
}

# Display social media links with logos
for platform, details in socials.items():
    st.markdown(
        f"""
        <a href="{details['url']}" target="_blank" style="text-decoration: none;">
            <img src="{details['logo']}" alt="{platform}" width="50" style="margin-right: 15px;">
        </a>
        """,
        unsafe_allow_html=True,
    )
