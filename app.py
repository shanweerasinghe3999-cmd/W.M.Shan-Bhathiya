import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Shan Bhathiya Weerasinghe — Portfolio",
    page_icon="🧭",
    layout="wide",
)

# ---------- THEME ----------
st.markdown("""
<style>
    .stApp{ background-color:#0A1930; color:#EAF2FB; }
    section[data-testid="stSidebar"]{ background-color:#102A43; }
    h1,h2,h3,h4{ color:#EAF2FB !important; }
    p, li, span, div{ color:#EAF2FB; }
    hr{ border-color:#23405f; }
    .box{ background:#102A43; border:1px solid #23405f; border-radius:10px; padding:20px; margin-bottom:18px; }
    .stat-num{ font-size:28px; font-weight:700; color:#5EE6D0; }
    .stat-label{ font-size:12px; color:#7C93B3; }
    .tag{ display:inline-block; background:#0A1930; border:1px solid #23405f; color:#7C93B3;
          border-radius:20px; padding:3px 10px; font-size:12px; margin-right:6px; }
    .badge{ display:inline-block; background:rgba(94,230,208,0.15); color:#5EE6D0;
            border-radius:20px; padding:4px 10px; font-size:12px; }
    a{ color:#5EE6D0; }
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR: PROFILE ----------
with st.sidebar:
    st.markdown("### 🧭 My Profile")
    st.image("https://api.dicebear.com/7.x/initials/svg?seed=Shan%20Bhathiya&backgroundColor=102A43&textColor=EAF2FB", width=110)
    st.markdown("**Shan Bhathiya Weerasinghe**")
    st.caption("Versatile Tech Builder")
    st.markdown("---")
    st.markdown("#### Navigation")
    page = st.radio("", ["Home", "Projects", "Certifications", "Contact"], label_visibility="collapsed")
    st.markdown("---")
    st.markdown("#### Quick Links")
    st.markdown("- [LinkedIn](https://linkedin.com/in/your-profile)")
    st.markdown("- [GitHub](https://github.com/your-username)")
    st.markdown("- 📧 youremail@example.com")
    st.caption("edit these placeholders in app.py")

# ---------- HOME (matches reference layout: 3 columns) ----------
if page == "Home":
    st.title("Shan Bhathiya Weerasinghe")
    st.caption("Versatile Tech Builder — Web · Networking · Security · Hardware")
    st.markdown("---")

    col_left, col_mid, col_right = st.columns([1, 1.6, 1])

    # ---- LEFT: Quick Stats + Highlights ----
    with col_left:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.subheader("📊 Quick Stats")
        st.markdown('<div class="stat-label">Major Projects</div><div class="stat-num">4+</div>', unsafe_allow_html=True)
        st.write("")
        st.markdown('<div class="stat-label">VIVA Score</div><div class="stat-num">81.5/100</div>', unsafe_allow_html=True)
        st.write("")
        st.markdown('<div class="stat-label">Certifications</div><div class="stat-num">3</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.subheader("⭐ Highlights")
        st.markdown("""
- Led a 4-person team as Group Leader
- Built full IoT-to-cloud energy system
- Certified in Python & Web Design
- Hands-on with hardware & software both
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    # ---- MIDDLE: About, Timeline, Experience chart ----
    with col_mid:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.subheader("📋 About Me")
        st.write(
            "Final-year Bachelor of Applied IT undergraduate at SLTC School of Computing and IT. "
            "Rather than staying in one lane, I've built real, working projects across web development, "
            "programming, networking, cyber security, and embedded hardware — and I enjoy the range more "
            "than specializing narrowly. As Group Leader of a four-person final-year team, I led the "
            "design and delivery of a cloud-based IoT energy management system from sensor to dashboard, "
            "then defended it at VIVA."
        )
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.subheader("🕒 Timeline")
        st.markdown("""
- **2026-05** — IoT project kickoff: Firebase, React dashboard, ESP32 firmware for Week 14 PoC
- **2026-06** — Exam & project sprint: Cloud Computing, Enterprise Software Dev, UX/UI, Mobile Dev
- **2026-07 (early)** — Final academic report, presentation deck, system polish ahead of VIVA
- **2026-07-11** — VIVA defended as Group Leader — Cloud-Based AI Energy Management System
        """)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.subheader("📈 Experience Overview")
        st.caption("Projects completed per year")
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=["2023", "2024", "2025", "2026"],
            y=[1, 2, 3, 4],
            mode="lines+markers",
            line=dict(color="#2E75B6", width=3),
            marker=dict(size=9, color="#5EE6D0"),
        ))
        fig.update_layout(
            paper_bgcolor="#102A43", plot_bgcolor="#102A43",
            font_color="#EAF2FB", height=280,
            xaxis=dict(gridcolor="#23405f", title="Year"),
            yaxis=dict(title="Projects", gridcolor="#23405f"),
            margin=dict(l=10, r=10, t=10, b=10),
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ---- RIGHT: Skills + Contact ----
    with col_right:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.subheader("🛠️ Skills")
        skills = [
            ("Python", 85),
            ("React / Web Dev", 80),
            ("Networking", 78),
            ("Cyber Security", 75),
            ("IoT / Embedded", 80),
            ("Cloud (Firebase/AWS)", 72),
        ]
        for name, val in skills:
            st.write(name)
            st.progress(val / 100)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.subheader("📬 Contact")
        st.markdown("📧 [youremail@example.com](mailto:youremail@example.com)")
        st.markdown("🔗 [LinkedIn](https://linkedin.com/in/your-profile)")
        st.markdown("💻 [GitHub](https://github.com/your-username)")
        st.markdown('</div>', unsafe_allow_html=True)

# ---------- PROJECTS ----------
elif page == "Projects":
    st.title("💼 Projects")

    st.markdown("""
    <div class="box" style="border-color:#2E75B6;">
        <span class="badge">Final-Year Project — Group Leader</span>
        <h3>Cloud-Based AI Energy Management &amp; Smart Automation System</h3>
        <span class="tag">ESP32</span><span class="tag">Firebase</span><span class="tag">React</span>
        <span class="tag">Netlify</span><span class="tag">IoT</span>
        <p>An end-to-end IoT energy monitoring platform: ESP32 with ACS712 current and DHT11 sensors
        feeding live readings to Firebase, controlled through a 4-channel relay, surfaced in a React
        dashboard with a rule-based AI analysis engine and CEB billing at LKR 2.50/kWh.</p>
        <ul>
            <li>Customer registration &amp; persistent usage history</li>
            <li>Rule-based AI engine for anomaly &amp; usage insights</li>
            <li>Deployed dashboard on Netlify</li>
            <li>Defended at VIVA — July 11, 2026</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="box">
        <h3>Digital Forensics Investigation</h3>
        <span class="tag">Wireshark</span><span class="tag">NetworkMiner</span><span class="tag">Steganography</span>
        <p>Network traffic and file-based forensics assignment: captured and analyzed traffic, extracted
        artifacts with NetworkMiner, and recovered hidden data using OpenStego/Steghide.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="box">
        <h3>SONERA — Music Streaming App</h3>
        <span class="tag">Figma</span><span class="tag">UX/UI</span>
        <p>A music streaming app concept designed in Figma with a dark navy and blue-accent theme,
        including full screen flows and a written design report.</p>
    </div>
    """, unsafe_allow_html=True)

# ---------- CERTIFICATIONS ----------
elif page == "Certifications":
    st.title("🎓 Certifications")
    st.caption("Online learning programmes — Centre for Open & Distance Learning (CODL), University of Moratuwa")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="box">
            <h3>Python for Beginners</h3>
            <p style="color:#7C93B3; font-size:13px;">Dept. of Computer Science & Engineering</p>
            <p style="font-size:12px;">Issued Jul 2025<br>Code: q1TNowBo5z</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="box">
            <h3>Python Programming</h3>
            <p style="color:#7C93B3; font-size:13px;">Dept. of Computer Science & Engineering</p>
            <p style="font-size:12px;">Issued 2025<br>Code: A7XtQFrrIF</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="box">
            <h3>Web Design for Beginners</h3>
            <p style="color:#7C93B3; font-size:13px;">Dept. of Information Technology</p>
            <p style="font-size:12px;">Issued 2025<br>Code: v6RIWfKclG</p>
        </div>
        """, unsafe_allow_html=True)

# ---------- CONTACT ----------
elif page == "Contact":
    st.title("📬 Contact")
    st.write("Open to opportunities in web development, networking, cyber security, and hardware/IoT.")
    st.markdown("- 📧 [youremail@example.com](mailto:youremail@example.com)")
    st.markdown("- 🔗 [LinkedIn](https://linkedin.com/in/your-profile)")
    st.markdown("- 💻 [GitHub](https://github.com/your-username)")
    st.info("Edit the placeholder links/email above near the top of app.py before deploying.")

st.markdown("---")
st.caption("Built with Streamlit by Shan Bhathiya Weerasinghe · 2026")
