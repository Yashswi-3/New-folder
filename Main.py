import streamlit as st
from PIL import Image

# Configure page
st.set_page_config(
    page_title="Story Visualizer - Yashswi Shukla",
    layout="centered"
)

# Header
st.title("Misty Hill School Story Visualizer")
st.subheader("PlanCover AI Internship Submission by Yashswi Shukla")
st.markdown("---")

# Poster 1
st.header("1️⃣ Pema's Dawn Walk")
st.image("ChatGPT Image Jun 15, 2025, 01_18_36 AM.png", use_container_width=True)
st.markdown("""
**Why this scene?**  
- Establishes Pema as the protagonist  
- Creates atmosphere with mist and dawn light  
- Shows solitude before friendships form  
- Visualizes key sensory detail: paw prints in dew
""")
st.markdown("---")

# Poster 2
st.header("2️⃣ Turning Toward School with Kunu")
st.image("ChatGPT Image Jun 15, 2025, 01_14_00 AM.png", use_container_width=True)
st.markdown("""
**Why this scene?**  
- First group moment showing friendships  
- Prayer flags add cultural authenticity  
- School reveal creates narrative anticipation  
- Kunu's arrival completes the circle
""")
st.markdown("---")

# Poster 3
st.header("3️⃣ Kunu Points - Group's Shared Awe")
st.image("ChatGPT Image Jun 15, 2025, 01_14_14 AM.png", use_container_width=True)
st.markdown("""
**Why this scene?**  
- Emotional climax of the story  
- Nature becomes the sixth character  
- Silhouettes focus on mountain reveal  
- Shows transition from mist to sunlight
""")
st.markdown("---")

# Poster 4
st.header("4️⃣ Final Dash to the Gate")
st.image("ChatGPT Image Jun 15, 2025, 02_18_44 AM.png", use_container_width=True)
st.markdown("""
**Why this scene?**  
- Perfect narrative conclusion  
- Shows character personalities through movement  
- Bell visualization represents new beginnings  
- Contrasts with opening's solitude
""")

# Footer
st.markdown("---")
st.caption("Created with Streamlit for PlanCover AI Internship | Images generated with Midjourney AI")