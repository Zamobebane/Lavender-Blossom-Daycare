import streamlit as st

# Page config
st.set_page_config(page_title="Lavender Blossom Daycare", page_icon="🌸")

# Title and Header
st.title("Lavender Blossom Daycare")
st.header("A Safe, Loving, and Educational Environment for Your Child")

# Daycare Information
st.subheader("Contact Information")
st.markdown("""
**Location:** 13352 SW 157th Ave, Tigard, OR 97223  
**Phone:** [564-654-1493](tel:5646541493)  
**Email:** [lavenderblossomdaycare@gmail.com](mailto:lavenderblossomdaycare@gmail.com)  
**Hours:** Monday – Friday, 6:00 AM – 6:00 PM
""")

# Image (optional)
st.image("https://cdn.pixabay.com/photo/2017/08/10/07/32/children-2616844_1280.jpg", use_column_width=True, caption="Where little blossoms grow with love")

# Mission or About
st.subheader("Our Mission")
st.write("""
At Lavender Blossom Daycare, we provide a nurturing and creative learning environment 
for children aged 6 months to 5 years. We focus on emotional growth, early education, 
and safe, joyful play.

We believe every child is unique and should be treated with care, love, and respect.
""")

# Optional form (for parent inquiries)
st.subheader("Send Us a Message")
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")
    if submitted:
        st.success("Thank you for your message! We'll get back to you shortly.")
