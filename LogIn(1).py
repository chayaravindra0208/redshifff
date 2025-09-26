import streamlit as st


IMAGE_ADDRESS = "https://img.freepik.com/free-photo/galaxy-wallpaper-warm-colors_23-2151769515.jpg?semt=ais_hybrid&w=740&q=80"

# Custom CSS for better styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }
    .stButton>button {
        background: linear-gradient(90deg, #ff6b6b, #ff8e53);
        color: white;
        font-weight: bold;
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# Home page
st.title("🌌 Galaxy Redshift Predictor")
st.subheader("Unlock the Secrets of the Cosmos")
st.write("""
Welcome to the Galaxy Redshift Prediction Platform. Explore the mysteries of the universe by analyzing 
and predicting galaxy redshifts. Our advanced algorithms help astronomers and researchers 
understand the expansion of the universe through the study of galaxy spectra.
""")

# Add a space-themed image
st.image(IMAGE_ADDRESS, 
         caption="Redshift")

if not st.user.is_logged_in:
    if st.sidebar.button("Log in with Google", type="primary", icon=":material/login:"):
        st.login()
else:
    if st.sidebar.button("Log out", type="secondary", icon=":material/logout:"):
        st.logout()
        st.stop()
