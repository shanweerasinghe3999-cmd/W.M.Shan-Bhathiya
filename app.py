import streamlit as st
from datetime import datetime
from pathlib import Path
import plotly.express as px
import base64
import math

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

    /* Sidebar text: left-align + proper wrapping (justify stretches badly in narrow sidebar) */
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] li,
    section[data-testid="stSidebar"] .stMarkdown,
    section[data-testid="stSidebar"] .stCaption {
        text-align: left !important;
        word-break: break-word;
        overflow-wrap: break-word;
        line-height: 1.6;
    }

    html, body, [class*="css"] { font-family: 'Segoe UI', 'Inter', sans-serif; }

    /* Headers with accent underline */
    h1, h2, h3 { font-weight: 800; letter-spacing: -0.3px; }
    h2, h3 { border-bottom: 3px solid #4A90D9; padding-bottom: 6px; margin-top: 4px; color: #1B4A7A !important; }

    /* Links */
    a, .stMarkdown a { color: #2E75B6 !important; font-weight: 600; }

    /* Metric cards */
    div[data-testid="stMetric"] {
        background: #EEF5FC;
        border: 1px solid #CFE2F5;
        border-radius: 10px;
        padding: 14px 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    div[data-testid="stMetricLabel"] { color: #1B4A7A; font-weight: 600; }
    div[data-testid="stMetricValue"] { color: #2E75B6; font-weight: 800; }

    /* Containers / cards used for projects & certifications */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 12px !important;
        border-color: #CFE2F5 !important;
        box-shadow: 0 2px 6px rgba(46,117,182,0.10);
    }

    /* Sidebar polish */
    section[data-testid="stSidebar"] {
        border-right: 1px solid #CFE2F5;
        background: #F6FAFE;
    }
    section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2 { color: #1B4A7A !important; }

    /* Sidebar profile photo - plain rounded corners, not circular */
    section[data-testid="stSidebar"] img {
        border-radius: 10px !important;
        border: 3px solid #4A90D9;
        box-shadow: 0 4px 12px rgba(74,144,217,0.20);
        object-fit: cover;
    }

    /* Buttons */
    button[kind="secondaryFormSubmit"], .stButton>button, .stDownloadButton>button, .stLinkButton>a {
        background-color: #2E75B6 !important; color: white !important;
        border-radius: 8px !important; border: none !important; font-weight: 700 !important;
    }

    /* Progress bars */
    div[data-testid="stProgress"] > div > div { background-color: #4A90D9 !important; }

    /* Divider spacing */
    hr { margin: 18px 0; border-color: #CFE2F5; }

    /* Hero gradient banner */
    .hero-banner {
        background: linear-gradient(135deg, #1B4A7A 0%, #2E75B6 55%, #7FB3E8 100%);
        border-radius: 18px;
        padding: 46px 44px 60px 44px;
        position: relative;
        margin-bottom: 46px;
        color: #ffffff;
        overflow: visible;
    }
    .hero-banner h1 {
        font-size: 36px; margin: 0 0 8px 0; color: #ffffff !important;
        border-bottom: none; padding-bottom: 0; line-height: 1.15; font-weight: 800;
    }
    .hero-banner p {
        font-size: 16px; opacity: 0.95; margin: 0; text-align: left;
        max-width: 560px; font-weight: 500;
    }
    .hero-tags { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 16px; }
    .hero-tag {
        background: rgba(255,255,255,0.16);
        border: 1px solid rgba(255,255,255,0.35);
        color: #ffffff; font-size: 12.5px; font-weight: 600;
        padding: 5px 14px; border-radius: 20px;
    }
    .hero-photo {
        position: absolute; bottom: -36px; right: 48px;
        width: 96px; height: 96px; border-radius: 10px;
        object-fit: cover; border: 4px solid #ffffff;
        box-shadow: 0 6px 16px rgba(0,0,0,0.18);
    }
    .stat-icon-row {
        display: flex; gap: 44px; margin: 10px 0 36px 4px; flex-wrap: wrap;
    }
    .stat-icon-item { text-align: center; min-width: 70px; }
    .stat-icon-item .icon { font-size: 26px; }
    .stat-icon-item .label { font-size: 12px; color: #1B4A7A; font-weight: 700; margin-top: 4px; }
    .big-stat-row { display: flex; gap: 50px; margin: 4px 0 30px 4px; flex-wrap: wrap; }
    .big-stat-item .num { font-size: 34px; font-weight: 800; color: #2E75B6; line-height: 1; }
    .big-stat-item .label { font-size: 13px; color: #1B4A7A; font-weight: 700; margin-top: 4px; }

    /* Custom skill bars (replacing default st.progress look) */
    .skill-list { margin-top: 4px; }
    .skill-item { margin-bottom: 16px; }
    .skill-row {
        display: flex; justify-content: space-between; align-items: baseline;
        font-size: 14px; font-weight: 600; color: #1B4A7A; margin-bottom: 6px;
    }
    .skill-pct { color: #2E75B6; font-weight: 700; font-size: 13px; }
    .skill-bar-bg {
        background: #C8DCF0; border: 1px solid #AFC9E8; border-radius: 8px; height: 9px; overflow: hidden;
    }
    .skill-bar-fill {
        background: linear-gradient(90deg, #1B4A7A, #2E75B6);
        height: 100%; border-radius: 8px;
    }

    /* ---------- Landing-page style hero ---------- */
    .landing-hero {
        display: flex; align-items: center; justify-content: space-between;
        gap: 30px; padding: 30px 10px 60px 10px; flex-wrap: wrap;
    }
    .landing-left { flex: 1 1 380px; min-width: 280px; }
    .landing-hello { color: #2E75B6; font-weight: 700; font-size: 16px; margin-bottom: 6px; }
    .landing-title { font-size: 40px; font-weight: 800; color: #12233D; margin: 0 0 4px 0; border-bottom: none !important; }
    .landing-role { font-size: 22px; font-weight: 600; color: #12233D; margin-bottom: 16px; }
    .landing-accent { color: #2E75B6; }
    .landing-desc { color: #4c6b8a; font-size: 15px; max-width: 460px; margin-bottom: 22px; }
    .landing-cta-row { display: flex; align-items: center; gap: 22px; flex-wrap: wrap; }
    .landing-cta-plain {
        color: #12233D !important; font-weight: 700; font-size: 15px;
        text-decoration: none !important; border-bottom: 2px solid #2E75B6; padding-bottom: 2px;
    }
    .landing-social a {
        margin-right: 16px; color: #12233D !important; font-weight: 600; font-size: 13px;
        text-decoration: none !important; border-bottom: 1px solid transparent;
    }
    .landing-social a:hover { border-bottom: 1px solid #2E75B6; }

    .landing-right {
        flex: 1 1 380px; min-width: 380px; height: 400px;
        display: flex; align-items: center; justify-content: center;
        position: relative;
    }
    .landing-photo {
        width: 190px; height: 190px; border-radius: 50%; object-fit: cover;
        border: 6px solid #ffffff; box-shadow: 0 10px 30px rgba(46,117,182,0.25);
        position: relative; z-index: 2;
    }
    .landing-photo-placeholder {
        display: flex; align-items: center; justify-content: center;
        font-size: 60px; background: #EEF5FC;
    }
    .deco-ring {
        position: absolute; border: 1.5px dashed #9FC4EA; border-radius: 50%;
        top: 50%; left: 50%; z-index: 1;
    }
    .ring-1 { width: 230px; height: 230px; transform: translate(-50%, -50%); }
    .ring-2 { width: 270px; height: 270px; transform: translate(-50%, -50%) rotate(20deg); }
    .float-badge {
        position: absolute; z-index: 3;
        background: #ffffff; border-radius: 50%;
        width: 38px; height: 38px;
        display: flex; align-items: center; justify-content: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.16);
        border: 1px solid #E4EEF9;
    }
    .float-badge img { width: 20px; height: 20px; object-fit: contain; }

    /* Responsive: smaller screens */
    @media (max-width: 900px) {
        .landing-hero { flex-direction: column; text-align: center; }
        .landing-desc { max-width: 100%; }
        .landing-cta-row { justify-content: center; }
        .landing-right { height: 360px; min-width: 340px; }
        .landing-photo { width: 150px; height: 150px; }
        .ring-1 { width: 190px; height: 190px; }
        .ring-2 { width: 230px; height: 230px; }
    }
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
    col_pic, col_info = st.columns([1, 2])
    with col_pic:
        img_path = Path(__file__).parent / "profile.jpg"
        if img_path.exists():
            st.image(str(img_path), width=80)
        else:
            st.caption("Add profile.jpg")
    with col_info:
        st.markdown(
            "<div style='font-weight:800; font-size:16px; line-height:1.2; color:#1B4A7A;'>Shan Bhathiya Nawarathna</div>",
            unsafe_allow_html=True
        )
        st.caption("Bachelor of Applied IT")

    st.write("🎓 SLTC Research University, Padukka")
    st.write("📞 0789728257")
    st.write("📍 [194/5 B, Samanala Place, Paligedara, Pilliyandala](https://www.google.com/maps/search/?api=1&query=194%2F5+B%2C+Samanala+Place%2C+Paligedara%2C+Pilliyandala) 🗺️")

    st.markdown("---")

    # Page navigation
    page = st.radio("Navigation", ["Home", "Experience", "Projects", "Certifications", "Contact"], index=0, label_visibility="collapsed")

    st.markdown("---")
    st.markdown("##### 🔗 Quick Links")
    st.write("[LinkedIn](https://www.linkedin.com/in/shan-bhathiya-1999283ab) · [GitHub](https://github.com/shanweerasinghe3999-cmd)")
    st.write("📧 shanweerasinghe3999@gmail.com")

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
    photo_html = f'<img src="data:image/jpeg;base64,{_profile_b64}" class="landing-photo">' if _profile_b64 else '<div class="landing-photo landing-photo-placeholder">📷</div>'

    _skill_badges = [
        ("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg", "Python"),
        ("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg", "JavaScript"),
        ("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg", "TypeScript"),
        ("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/angularjs/angularjs-original.svg", "Angular"),
        ("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg", "Java"),
        ("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg", "HTML5"),
        ("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg", "Git"),
        ("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/firebase/firebase-plain.svg", "Firebase"),
        ("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg", "Figma"),
    ]
    # Text-badge fallback for tools without a reliable free icon CDN
    _text_badges = [
        ("PBI", "#F2C811", "#3a2f00", "Power BI"),
        ("TAB", "#E97627", "#ffffff", "Tableau"),
        ("W", "#2B579A", "#ffffff", "Word"),
        ("X", "#217346", "#ffffff", "Excel"),
        ("P", "#B7472A", "#ffffff", "PowerPoint"),
    ]
    _n = len(_skill_badges) + len(_text_badges)
    _radius_px = 175  # pixels from center - clear of the ring
    badge_html = ""
    _i = 0
    for _url, _alt in _skill_badges:
        _angle = (2 * math.pi * _i / _n) - (math.pi / 2)
        _x = _radius_px * math.cos(_angle)
        _y = _radius_px * math.sin(_angle)
        badge_html += (
            f'<div class="float-badge" style="left:calc(50% + {_x:.0f}px); top:calc(50% + {_y:.0f}px); '
            f'transform: translate(-50%,-50%);"><img src="{_url}" alt="{_alt}"></div>'
        )
        _i += 1
    for _label, _bg, _fg, _alt in _text_badges:
        _angle = (2 * math.pi * _i / _n) - (math.pi / 2)
        _x = _radius_px * math.cos(_angle)
        _y = _radius_px * math.sin(_angle)
        badge_html += (
            f'<div class="float-badge" title="{_alt}" style="left:calc(50% + {_x:.0f}px); top:calc(50% + {_y:.0f}px); '
            f'transform: translate(-50%,-50%); background:{_bg}; color:{_fg}; '
            f'font-weight:800; font-size:11px;">{_label}</div>'
        )
        _i += 1

    st.markdown(f"""
    <div class="landing-hero">
        <div class="landing-left">
            <div class="landing-hello">Hello</div>
            <h1 class="landing-title">I'm <span class="landing-accent">Shan Bhathiya</span></h1>
            <div class="landing-role">Versatile <span class="landing-accent">Tech Builder</span></div>
            <p class="landing-desc">
                Final-year Bachelor of Applied IT undergraduate, comfortable across
                web development, networking, cyber security, and embedded hardware.
            </p>
            <div class="landing-cta-row">
                <a href="#about-me" class="landing-cta-plain">About Me</a>
                <span class="landing-social">
                    <a href="https://www.linkedin.com/in/shan-bhathiya-1999283ab" target="_blank">LinkedIn</a>
                    <a href="https://github.com/shanweerasinghe3999-cmd" target="_blank">GitHub</a>
                    <a href="mailto:shanweerasinghe3999@gmail.com">Email</a>
                </span>
            </div>
        </div>
        <div class="landing-right">
            <div class="deco-ring ring-1"></div>
            <div class="deco-ring ring-2"></div>
            {badge_html}
            {photo_html}
        </div>
    </div>

    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="big-stat-row">
        <div class="big-stat-item"><div class="num">1</div><div class="label">Major Project</div></div>
        <div class="big-stat-item"><div class="num">3</div><div class="label">Certifications</div></div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    # --- Column 1: Highlights + small Experience chart ---
    with col1:
        st.subheader("⭐ Highlights")
        st.write("• Built full IoT-to-cloud energy system")
        st.write("• Certified in Python & Web Design")
        st.write("• Hands-on with hardware & software both")

        st.markdown("---")
        st.markdown('<h3 style="white-space: nowrap; font-size: 19px;">📈 Experience Overview</h3>', unsafe_allow_html=True)
        data = {
            "Year": ["2023", "2024", "2025", "2026"],
            "Achievements": [0, 0, 3, 1],
        }
        fig = px.bar(data, x="Year", y="Achievements", title="Certifications & Major Projects by Year",
                     color_discrete_sequence=["#2E75B6"])
        fig.update_layout(height=280, margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig, use_container_width=True)
        st.caption("2025: 3 certifications completed · 2026: final-year IoT project completed")

    # --- Column 2: Main Content ---
    with col2:
        st.subheader("👋 About Me")
        st.write(
            "Hello! I'm Shan Bhathiya Nawarthna, a Bachelor of Applied Information Technology (DAIT) "
            "undergraduate at SLTC Research University with a passion for developing innovative "
            "software solutions and transforming data into meaningful insights."
        )
        st.write(
            "My interests include Software Engineering, Web Development, Business Intelligence (BI), "
            "Data Science, Data Analytics, Artificial Intelligence (AI), and the Internet of Things "
            "(IoT). I enjoy designing applications, analyzing data, and creating interactive "
            "dashboards that help organizations make better data-driven decisions."
        )
        st.write(
            "I have experience working with Angular, JavaScript, TypeScript, Python, Java, HTML, CSS, "
            "SQL, Firebase, Git, Power BI, and Tableau. I am familiar with data analysis, data "
            "visualization, dashboard development, database management, and business intelligence "
            "concepts, allowing me to transform complex datasets into valuable insights."
        )
        st.write(
            "Through academic and personal projects, I have developed web applications, IoT-based "
            "systems, cloud solutions, and data-driven applications while improving my skills in "
            "software development, problem-solving, analytical thinking, and teamwork."
        )
        st.write(
            "I am a motivated and continuous learner who is always eager to explore emerging "
            "technologies and enhance my technical skills. My career goal is to become a Software "
            "Engineer, Data Analyst, Business Intelligence Developer, or Data Scientist and "
            "contribute to creating innovative technology solutions that deliver real-world value."
        )

    # --- Column 3: Skills ---
    with col3:
        st.subheader("Skills")
        skills = {
            "Angular": 76,
            "JavaScript": 82,
            "TypeScript": 75,
            "Python": 84,
            "Java": 75,
            "HTML / CSS": 80,
            "Firebase": 77,
            "SQL": 78,
            "Git": 81,
            "Power BI": 75,
            "Tableau": 72,
            "UI/UX Design": 70,
        }
        skill_html = '<div class="skill-list">'
        for name, val in skills.items():
            skill_html += (
                f'<div class="skill-item">'
                f'<div class="skill-row"><span>{name}</span><span class="skill-pct">{val}%</span></div>'
                f'<div class="skill-bar-bg"><div class="skill-bar-fill" style="width:{val}%;"></div></div>'
                f'</div>'
            )
        skill_html += "</div>"
        st.markdown(skill_html, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📬 Contact")
    st.write("📧 shanweerasinghe3999@gmail.com")
    st.write("📞 0789728257")
    st.write("🌐 [LinkedIn](https://www.linkedin.com/in/shan-bhathiya-1999283ab)")
    st.write("💻 [GitHub](https://github.com/shanweerasinghe3999-cmd)")

# -------------------- EXPERIENCE PAGE --------------------
elif page == "Experience":
    st.title("🧳 Experience & Education")

    col_exp, col_edu = st.columns(2)

    with col_exp:
        st.subheader("💼 Work Experience")
        with st.container(border=True):
            st.write("**Union Bank** | Pettah")
            st.caption("2019 – 2020")
            st.write("Personal Banking Advisor at the sales & credit card unit.")
        with st.container(border=True):
            st.write("**Reebonn Lanka Pvt Ltd.** | Malabe")
            st.caption("May 2024 – December 2024")
            st.write("Data Entry Operator at the Production Department.")

        st.markdown("---")
        st.subheader("🧰 Additional Skills")
        with st.container(border=True):
            st.write("• Microsoft Office (Word, Excel, PowerPoint)")
            st.write("• SAP software experience")
            st.write("• Data entry with high accuracy")
            st.write("• Good communication skills")
            st.write("• Basic IT knowledge")

    with col_edu:
        st.subheader("🎓 Education")
        with st.container(border=True):
            st.write("**Bachelor of Applied IT**")
            st.caption("SLTC Research University, Padukka · 2023 – Present")
        with st.container(border=True):
            st.write("**GCE Advanced Level** (2021)")
            st.caption("History of Sri Lanka & India: B · Geography: C · Buddhist Civilization: C")
        with st.container(border=True):
            st.write("**GCE Advanced Level** (2019) — Dharmapala College, Pannipitiya")
            st.caption("Chemistry: S · English: S")
        with st.container(border=True):
            st.write("**GCE Ordinary Level** (2015) — President College, Maharagama")
            st.caption("7 A's & 2 C's")
        with st.container(border=True):
            st.write("**Diploma in English** — British Way English Academy")
            st.caption("December 2022 – February 2023")
        with st.container(border=True):
            st.write("Basic Computer Course — Zonal ICT Education Center, Sri Jayawardhanapura Zone")
            st.write("Computer Literacy Course — Open University of Sri Lanka")

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
        st.link_button("🔗 View Live Project (Demo Version)", "https://thunderous-pastelito-6b0907.netlify.app/login")
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