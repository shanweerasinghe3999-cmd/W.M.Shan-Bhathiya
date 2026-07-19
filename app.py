import streamlit as st
from datetime import datetime
from pathlib import Path
import plotly.express as px

# -------------------- PAGE SETUP --------------------
st.set_page_config(
    page_title="Shan Bhathiya Nawarathna — Portfolio",
    page_icon="🧑🏾‍💻",
    layout="wide"
)

# Justify all text across the app
st.markdown("""
<style>
    p, li, div, span, .stMarkdown, .stCaption { text-align: justify; }
</style>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------
with st.sidebar:
    st.markdown("## 🧑🏾‍💻 My Profile")

    # Put your photo file in the same folder as this app.py and change the filename below
    img_path = Path(__file__).parent / "profile.jpg"
    if img_path.exists():
        st.image(str(img_path), width=150, caption="Bachelor of Applied IT")
    else:
        st.info("Add your photo as 'profile.jpg' in the same folder as app.py")

    st.markdown(
        "<h1 style='white-space: nowrap; text-align: justify;'>Shan Bhathiya Nawarathna</h1>",
        unsafe_allow_html=True
    )
    st.caption("Versatile Tech Builder — Web · Networking · Security · Hardware")

    st.markdown("---")
    st.write("🎓 **University:** SLTC Research University, Padukka")
    st.write("📘 **Degree:** Bachelor of Applied IT")
    st.write("📞 **Phone:** 0789728257")
    st.write("📍 **Address:** [194/5 B, Samanala Place, Paligedara, Pilliyandala](https://www.google.com/maps/search/?api=1&query=194%2F5+B%2C+Samanala+Place%2C+Paligedara%2C+Pilliyandala) 🗺️")

    st.markdown("---")

    # Page navigation
    page = st.radio("📂 Navigation", ["Home", "Projects", "Certifications", "Contact"], index=0)

    st.markdown("---")
    st.markdown("### 🔗 Quick Links")
    st.write("• [LinkedIn](https://www.linkedin.com/in/shan-bhathiya-1999283ab)")
    st.write("• [GitHub](https://github.com/shanweerasinghe3999-cmd)")
    st.write("• 📧 Email: shanweerasinghe3999@gmail.com")

# -------------------- HOME PAGE --------------------
if page == "Home":
    col1, col2, col3 = st.columns([1, 2, 1])

    # --- Column 1: Quick stats ---
    with col1:
        st.subheader("📊 Quick Stats")
        st.metric("Major Projects", "1")
        st.metric("Certifications", "3")
        st.metric("Role", "Group Leader")
        st.markdown("---")
        st.subheader("Highlights")
        st.write("• Built full IoT-to-cloud energy system")
        st.write("• Certified in Python & Web Design")
        st.write("• Hands-on with hardware & software both")

    # --- Column 2: Main Content ---
    with col2:
        st.header("👋 About Me")
        st.write(
            "Final-year Bachelor of Applied IT undergraduate at SLTC Research University, Padukka. "
            "Rather than staying in one lane, I've built real, working projects across web development, "
            "programming, networking, cyber security, and embedded hardware — and I enjoy the range more "
            "than specializing narrowly. As Group Leader of a four-person final-year team, I led the "
            "design and delivery of a cloud-based IoT energy management system from sensor to dashboard, "
            "then defended it at VIVA."
        )

        st.markdown("---")
        st.subheader("📈 Experience Overview")
        data = {
            "Year": ["2023", "2024", "2025", "2026"],
            "Projects": [1, 2, 3, 4],
        }
        fig = px.line(data, x="Year", y="Projects", markers=True, title="Projects Completed per Year")
        st.plotly_chart(fig, use_container_width=True)

    # --- Column 3: Skills ---
    with col3:
        st.subheader("Skills")
        skills = {
            "Python": 0.85,
            "React / Web Dev": 0.80,
            "Networking": 0.78,
            "Cyber Security": 0.75,
            "IoT / Embedded": 0.80,
            "Cloud (Firebase/AWS)": 0.72,
        }
        for name, val in skills.items():
            st.write(name)
            st.progress(val)

        st.markdown("---")
        st.subheader("📬 Contact")
        st.write("📧 shanweerasinghe3999@gmail.com")
        st.write("📞 0789728257")
        st.write("🌐 [LinkedIn](https://www.linkedin.com/in/shan-bhathiya-1999283ab)")
        st.write("💻 [GitHub](https://github.com/shanweerasinghe3999-cmd)")

# -------------------- PROJECTS PAGE --------------------
elif page == "Projects":
    st.title("🧩 Projects")

    with st.container():
        st.subheader("Cloud-Based AI Energy Management & Smart Automation System")
        st.caption("Final-Year Project — Group Leader")
        st.write(
            "An end-to-end IoT energy monitoring platform: ESP32 with ACS712 current and DHT11 sensors "
            "feeding live readings to Firebase, controlled through a 4-channel relay, surfaced in a React "
            "dashboard with a rule-based AI analysis engine and CEB billing at LKR 2.50/kWh."
        )
        st.write("• Customer registration & persistent usage history")
        st.write("• Rule-based AI engine for anomaly & usage insights")
        st.write("• Deployed dashboard on Netlify")
        st.write("• Defended at VIVA — July 11, 2026")
        st.write("Tech: ESP32, Firebase, React, Netlify, IoT")
        st.markdown("---")

# -------------------- CERTIFICATIONS PAGE --------------------
elif page == "Certifications":
    st.title("🎓 Certifications")
    st.caption("Online learning programmes — Centre for Open & Distance Learning (CODL), University of Moratuwa")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("Python for Beginners")
        st.caption("Dept. of Computer Science & Engineering")
        st.write("Issued: Jul 2025")
        st.write("Code: q1TNowBo5z")
    with c2:
        st.subheader("Python Programming")
        st.caption("Dept. of Computer Science & Engineering")
        st.write("Issued: 2025")
        st.write("Code: A7XtQFrrIF")
    with c3:
        st.subheader("Web Design for Beginners")
        st.caption("Dept. of Information Technology")
        st.write("Issued: 2025")
        st.write("Code: v6RIWfKclG")

# -------------------- CONTACT PAGE --------------------
elif page == "Contact":
    st.title("📩 Contact Me")
    st.write("Feel free to send a message — I'll reply as soon as I can!")

    st.markdown("---")
    st.write("📧 **Email:** shanweerasinghe3999@gmail.com")
    st.write("📞 **Phone:** 0789728257")
    st.write("📍 **Address:** [194/5 B, Samanala Place, Paligedara, Pilliyandala](https://www.google.com/maps/search/?api=1&query=194%2F5+B%2C+Samanala+Place%2C+Paligedara%2C+Pilliyandala) 🗺️")
    st.write("🌐 **LinkedIn:** [shan-bhathiya-1999283ab](https://www.linkedin.com/in/shan-bhathiya-1999283ab)")
    st.write("💻 **GitHub:** [shanweerasinghe3999-cmd](https://github.com/shanweerasinghe3999-cmd)")
    st.markdown("---")

    with st.form("contact_form"):
        name = st.text_input("Your name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send message")
        if submitted:
            st.success("✅ Thanks for your message! I'll get back to you soon.")
            st.write("---")
            st.write(f"**Name:** {name}")
            st.write(f"**Email:** {email}")
            st.write(f"**Message:** {message}")

# -------------------- FOOTER --------------------
st.markdown("---")
st.caption(f"Built with 🧑🏾‍💻 by Shan Bhathiya Nawarathna • {datetime.now().year}")