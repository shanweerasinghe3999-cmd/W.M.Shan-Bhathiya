import streamlit as st
from datetime import datetime
from pathlib import Path
import plotly.express as px
import base64

# -------------------- PAGE SETUP --------------------
st.set_page_config(
    page_title="Shan Bhathiya Nawarathna — Portfolio",
    page_icon="🧑🏾‍💻",
    layout="wide"
)

# Professional styling layer
st.markdown("""
<style>
    p, li, .stMarkdown, .stCaption { text-align: justify; }

    html, body, [class*="css"] { font-family: 'Segoe UI', 'Inter', sans-serif; }

    /* Headers with accent underline */
    h1, h2, h3 { font-weight: 700; letter-spacing: -0.3px; }
    h2, h3 { border-bottom: 2px solid #2E75B6; padding-bottom: 6px; margin-top: 4px; }

    /* Metric cards */
    div[data-testid="stMetric"] {
        background: #f5f8fc;
        border: 1px solid #dbe6f2;
        border-radius: 10px;
        padding: 14px 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    div[data-testid="stMetricLabel"] { color: #4c6b8a; }
    div[data-testid="stMetricValue"] { color: #2E75B6; font-weight: 700; }

    /* Containers / cards used for projects & certifications */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 10px !important;
        box-shadow: 0 1px 4px rgba(0,0,0,0.05);
    }

    /* Sidebar polish */
    section[data-testid="stSidebar"] { border-right: 1px solid #dbe6f2; }

    /* Buttons */
    button[kind="secondaryFormSubmit"], .stButton>button {
        background-color: #2E75B6; color: white; border-radius: 8px; border: none;
    }

    /* Divider spacing */
    hr { margin: 18px 0; border-color: #dbe6f2; }

    /* Hero gradient banner */
    .hero-banner {
        background: linear-gradient(135deg, #16327a 0%, #2E75B6 55%, #5EA6E6 100%);
        border-radius: 18px;
        padding: 46px 44px 60px 44px;
        position: relative;
        margin-bottom: 46px;
        color: #ffffff;
        overflow: visible;
    }
    .hero-banner h1 {
        font-size: 36px; margin: 0 0 8px 0; color: #ffffff !important;
        border-bottom: none; padding-bottom: 0; line-height: 1.15;
    }
    .hero-banner p {
        font-size: 16px; opacity: 0.92; margin: 0; text-align: left;
        max-width: 560px;
    }
    .hero-photo {
        position: absolute; bottom: -36px; right: 48px;
        width: 96px; height: 96px; border-radius: 50%;
        object-fit: cover; border: 4px solid #ffffff;
        box-shadow: 0 6px 16px rgba(0,0,0,0.18);
    }
    .stat-icon-row {
        display: flex; gap: 44px; margin: 10px 0 36px 4px; flex-wrap: wrap;
    }
    .stat-icon-item { text-align: center; min-width: 70px; }
    .stat-icon-item .icon { font-size: 26px; }
    .stat-icon-item .label { font-size: 12px; color: #4c6b8a; margin-top: 4px; }
    .big-stat-row { display: flex; gap: 50px; margin: 4px 0 30px 4px; flex-wrap: wrap; }
    .big-stat-item .num { font-size: 32px; font-weight: 800; color: #16327a; line-height: 1; }
    .big-stat-item .label { font-size: 13px; color: #4c6b8a; margin-top: 4px; }
</style>
""", unsafe_allow_html=True)

def _img_b64(path):
    if path.exists():
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

_profile_b64 = _img_b64(Path(__file__).parent / "profile.jpg")

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

    st.markdown("---")
    cv_path = Path(__file__).parent / "Shan_CV.pdf"
    if cv_path.exists():
        with open(cv_path, "rb") as f:
            st.download_button(
                label="⬇️ Download CV",
                data=f,
                file_name="Shan_Bhathiya_Nawarathna_Weerasinghe_CV.pdf",
                mime="application/pdf",
            )
    else:
        st.caption("Add 'Shan_CV.pdf' in the app folder to enable CV download")

# -------------------- HOME PAGE --------------------
if page == "Home":
    photo_html = f'<img src="data:image/jpeg;base64,{_profile_b64}" class="hero-photo">' if _profile_b64 else ""
    st.markdown(f"""
    <div class="hero-banner">
        <h1>W.M. Shan Bhathiya<br>Nawarathna Weerasinghe</h1>
        <p>Versatile Tech Builder — Web · Networking · Security · Hardware</p>
        {photo_html}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="big-stat-row">
        <div class="big-stat-item"><div class="num">1</div><div class="label">Major Project</div></div>
        <div class="big-stat-item"><div class="num">3</div><div class="label">Certifications</div></div>
    </div>
    <div class="stat-icon-row">
        <div class="stat-icon-item"><div class="icon">🌐</div><div class="label">Web Dev</div></div>
        <div class="stat-icon-item"><div class="icon">📡</div><div class="label">Networking</div></div>
        <div class="stat-icon-item"><div class="icon">🔒</div><div class="label">Security</div></div>
        <div class="stat-icon-item"><div class="icon">🔧</div><div class="label">Hardware / IoT</div></div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    # --- Column 1: Highlights ---
    with col1:
        st.subheader("⭐ Highlights")
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

    with st.container(border=True):
        st.subheader("Cloud-Based AI Energy Management & Smart Automation System")
        st.caption("Final-Year Project — Group Leader")
        st.write(
            "An end-to-end IoT energy monitoring platform: ESP32 with ACS712 current and DHT11 sensors "
            "feeding live readings to Firebase, controlled through a 4-channel relay, surfaced in a React "
            "dashboard with a rule-based AI analysis engine that estimates the monthly bill."
        )
        st.write("• Customer registration & persistent usage history")
        st.write("• Rule-based AI engine for anomaly & usage insights")
        st.write("• Deployed dashboard on Netlify")
        st.write("**Tech:** ESP32, Firebase, React, Netlify, IoT")
        st.link_button("🔗 View Live Project (Demo Version)", "https://thunderous-pastelito-6b0907.netlify.app/")
        st.caption("Note: this is a demo version of the project.")

# -------------------- CERTIFICATIONS PAGE --------------------
elif page == "Certifications":
    st.title("🎓 Certifications")
    st.caption("Online learning programmes — Centre for Open & Distance Learning (CODL), University of Moratuwa")

    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            st.subheader("Python for Beginners")
            st.caption("Dept. of Computer Science & Engineering")
            st.write("Issued: Jul 2025")
            st.write("Code: q1TNowBo5z")
            st.link_button("🔗 Verify", "https://open.uom.lk/verify")
    with c2:
        with st.container(border=True):
            st.subheader("Python Programming")
            st.caption("Dept. of Computer Science & Engineering")
            st.write("Issued: 2025")
            st.write("Code: A7XtQFrrIF")
            st.link_button("🔗 Verify", "https://open.uom.lk/verify")
    with c3:
        with st.container(border=True):
            st.subheader("Web Design for Beginners")
            st.caption("Dept. of Information Technology")
            st.write("Issued: 2025")
            st.write("Code: v6RIWfKclG")
            st.link_button("🔗 Verify", "https://open.uom.lk/verify")

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

    cv_path = Path(__file__).parent / "Shan_CV.pdf"
    if cv_path.exists():
        with open(cv_path, "rb") as f:
            st.download_button(
                label="⬇️ Download My CV",
                data=f,
                file_name="Shan_Bhathiya_Nawarathna_Weerasinghe_CV.pdf",
                mime="application/pdf",
            )
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