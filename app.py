import streamlit as st
import base64

st.set_page_config(page_title="Lavender Blossom Daycare", layout="centered")

# ---- BACKGROUND IMAGE FUNCTION ----
def set_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
        page_bg = f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500&display=swap');

        html, body, [class*="css"] {{
            font-family: 'Quicksand', sans-serif;
            scroll-behavior: smooth;
        }}

        .stApp {{
            background-image: 
                linear-gradient(rgba(255, 255, 255, 0.4), rgba(255, 255, 255, 0.4)),
                url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

        .block-container {{
            animation: fadeIn 1.3s ease-in;
            padding: 2.5rem 3rem;
            background: rgba(255, 255, 255, 0.35);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 1.5rem;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            color: #111;
            max-width: 820px;
            margin: 2rem auto;
        }}

        h1 {{
            color: #8e44ad !important;
            font-size: 3rem;
            text-align: center;
            margin-bottom: 0.4em;
        }}

        h2, h3 {{
            color: #333 !important;
            margin-top: 2rem;
            font-size: 1.5rem;
        }}

        a {{
            color: #8e44ad !important;
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}

        hr {{
            border: none;
            border-top: 1px solid rgba(0, 0, 0, 0.1);
            margin: 2rem 0;
        }}

        .contact-grid {{
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            gap: 1.5rem;
            margin-top: 1rem;
            margin-bottom: 2rem;
        }}

        .card {{
            flex: 1 1 200px;
            background: rgba(255,255,255,0.75);
            border-radius: 1rem;
            padding: 1rem;
            box-shadow: 0 4px 16px rgba(0,0,0,0.1);
            text-align: center;
        }}

        .card-icon {{
            font-size: 2rem;
            margin-bottom: 0.5rem;
            color: #8e44ad;
        }}

        .footer {{
            text-align: center;
            font-size: 0.9rem;
            margin-top: 2rem;
            color: #555;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        </style>
        """
        st.markdown(page_bg, unsafe_allow_html=True)

# ---- SET BACKGROUND ----
set_bg_from_local("ChatGPT Image May 12, 2025, 02_00_46 PM.png")

# ---- PAGE CONTENT ----
st.title("Lavender Blossom Daycare")
st.subheader("A loving and safe place for your child to grow and blossom 💜🌿")

# ---- CONTACT GRID ----
st.markdown("### 📬 Contact & Location")
st.markdown("""
<div class="contact-grid">
  <div class="card">
    <div class="card-icon">📍</div>
    <strong>Location</strong><br>
    13352 SW 157th Ave<br>Tigard, OR 97223
  </div>
  <div class="card">
    <div class="card-icon">📞</div>
    <strong>Phone</strong><br>
    <a href="tel:5646541493">564-654-1493</a>
  </div>
  <div class="card">
    <div class="card-icon">📧</div>
    <strong>Email</strong><br>
    <a href="mailto:lavenderblossomdaycare@gmail.com">lavenderblossomdaycare@gmail.com</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ---- HOURS ----
st.markdown("### 🕕 Hours of Operation")
st.write("**Monday to Friday:** 6:00 AM – 6:00 PM")

st.markdown("<hr />", unsafe_allow_html=True)

# ---- ABOUT SECTION ----
st.markdown("### 💜 About Us 🌿")
st.write("""
At Lavender Blossom Daycare, we provide a nurturing, creative, and secure environment
where children thrive. Our certified caregivers offer structured learning, fun activities,
and healthy meals throughout the day.

Let your child grow with us — where every little blossom is cared for with love. 💜🌿
""")

st.markdown("<hr />", unsafe_allow_html=True)

# ---- FOOTER ----
st.markdown('<div class="footer">© 2025 Lavender Blossom Daycare</div>', unsafe_allow_html=True)
