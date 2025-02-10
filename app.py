# app.py
import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import json
import time
from PIL import Image
import folium
from streamlit_folium import folium_static
import streamlit.components.v1 as components
import pickle
import io

# Configure Streamlit page
st.set_page_config(
    page_title="Clairvoyant Breast Cancer Intelligence Platform",
    page_icon="🎗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load and apply custom CSS
def load_css():
    css = """
    <style>
        .main { background-color: #FFF5F6; }
        .stButton>button { 
            background-color: #FF69B4;
            color: white;
            border-radius: 20px;
        }
        .sidebar .sidebar-content {
            background-color: #FFE4E1;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Authentication functions
def login_user(username, password):
    # In production, replace with secure database authentication
    return username == "demo" and password == "demo123"

def create_account(username, email, password):
    # In production, implement secure user creation
    return True

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

def main():
    load_css()
    
    if not st.session_state.logged_in:
        show_login_page()
    else:
        show_main_interface()

def show_login_page():
    st.title("🎗️ Welcome to Clairvoyant")
    
    tab1, tab2, tab3 = st.tabs(["Login", "Sign Up", "Forgot Password"])
    
    with tab1:
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if login_user(username, password):
                st.session_state.logged_in = True
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid credentials")

    with tab2:
        st.subheader("Create Account")
        new_username = st.text_input("Choose Username")
        new_email = st.text_input("Email")
        new_password = st.text_input("Choose Password", type="password")
        if st.button("Sign Up"):
            if create_account(new_username, new_email, new_password):
                st.success("Account created! Please login.")
            else:
                st.error("Error creating account")

    with tab3:
        st.subheader("Reset Password")
        reset_email = st.text_input("Enter Email")
        if st.button("Reset Password"):
            st.info("Password reset instructions sent to your email")

def show_main_interface():
    # Sidebar for user profile and settings
    with st.sidebar:
        st.title("User Profile")
        st.image("https://via.placeholder.com/150", width=150)
        st.write("Welcome, User!")
        
        if st.button("Profile Settings"):
            st.text_input("Name")
            st.text_input("Email")
        
        st.toggle("Dark Mode", key="dark_mode")
        
        if st.button("Voice Assistant 🎤"):
            st.info("Voice assistant activated")
        
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

    # Main navigation
    st.title("Breast Cancer Prediction Platform")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Predict", "Visualize", "Symptoms", "Nearby Hospitals", "Manual Prediction"
    ])
    
    with tab1:
        st.header("AI Prediction")
        uploaded_file = st.file_uploader(
            "Upload medical image (PDF, JPG, PNG)", 
            type=["pdf", "jpg", "jpeg", "png"]
        )
        if uploaded_file:
            st.image(uploaded_file)
            if st.button("Analyze Image"):
                with st.spinner("Analyzing..."):
                    time.sleep(2)  # Simulate processing
                    st.success("Analysis complete!")
                    st.write("Prediction: Benign (98% confidence)")
                    
                # Generate prescription
                if st.button("Generate Prescription"):
                    st.download_button(
                        "Download Prescription",
                        "Sample prescription content",
                        file_name="prescription.pdf"
                    )

    with tab2:
        st.header("Statistical Insights")
        # Add visualization charts here
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['Malignant', 'Benign', 'Inconclusive']
        )
        st.line_chart(chart_data)

    with tab3:
        st.header("Common Symptoms")
        st.write("""
        - Changes in breast size or shape
        - Lumps or thickening
        - Changes in skin texture
        - Changes in the nipple
        - Nipple discharge
        - Pain in the breast or armpit
        """)

    with tab4:
        st.header("Find Nearby Medical Centers")
        m = folium.Map(location=[40.7128, -74.0060], zoom_start=13)
        folium_static(m)

    with tab5:
        st.header("Manual Data Entry Prediction")
        # Add form fields for manual prediction

    # Chat assistant
    with st.container():
        st.write("---")
        if st.button("💬 Need Help? Chat with AI Assistant"):
            st.chat_message("assistant").write("Hello! How can I help you today?")

    # Footer
    st.markdown("---")
    st.markdown("*Developed for Women's Safety by Team D*")

if __name__ == "__main__":
    main()