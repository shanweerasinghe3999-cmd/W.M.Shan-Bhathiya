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

dark_mode = True

# Professional styling layer
st.markdown("""
<style>
    p, li, .stMarkdown, .stCaption { text-align: justify; }
    .bullet-plain { text-align: left !important; margin-bottom: 0.6em; line-height: 1.5; }

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
    h1, h2, h3 { font-weight: 800; letter-spacing: -0.3px; font-family: 'Times New Roman', Georgia, 'Cambria', serif; }
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
    div[data-testid="stVerticalBlockBorderWrapper"] p,
    div[data-testid="stVerticalBlockBorderWrapper"] li,
    div[data-testid="stVerticalBlockBorderWrapper"] .stMarkdown,
    div[data-testid="stVerticalBlockBorderWrapper"] .stCaption {
        text-align: left !important;
    }

    /* Sidebar polish */
    section[data-testid="stSidebar"] {
        border-right: 1px solid #CFE2F5;
        background: #F6FAFE;
    }
    section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2 { color: #1B4A7A !important; }
    .sidebar-name { color: #1B4A7A; }

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
    .skill-item { margin-bottom: 8px; }
    .skill-row {
        display: flex; justify-content: space-between; align-items: baseline;
        font-size: 14px; font-weight: 600; color: #1B4A7A; margin-bottom: 3px;
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
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(18px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes popIn {
        from { opacity: 0; transform: scale(0.85); }
        to   { opacity: 1; transform: scale(1); }
    }
    .landing-hero {
        display: flex; align-items: center; justify-content: space-between;
        gap: 30px; padding: 40px 34px 54px 34px; flex-wrap: wrap;
        background: #0b0f14;
        border-radius: 20px;
    }
    .landing-left { flex: 1 1 380px; min-width: 280px; }

    /* ---------- Code-editor style hero block ---------- */
    .code-editor {
        background: transparent;
        border-radius: 12px;
        overflow: hidden;
        opacity: 0; animation: fadeInUp 0.7s ease-out 0.1s forwards;
        max-width: 520px;
    }
    .code-editor-topbar {
        display: flex; align-items: center; gap: 7px;
        padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.10);
    }
    .code-dot { width: 11px; height: 11px; border-radius: 50%; display: inline-block; }
    .code-dot.red { background: #ff5f56; }
    .code-dot.yellow { background: #ffbd2e; }
    .code-dot.green { background: #27c93f; }
    .code-editor-filename {
        margin-left: 10px; color: #6e7681; font-size: 12.5px; font-family: 'Consolas','Monaco','Courier New',monospace;
    }
    .code-editor-body {
        padding: 22px 24px 26px 24px;
        font-family: 'Consolas','Monaco','Courier New',monospace;
        font-size: 15px; line-height: 1.85;
    }
    .code-line {
        display: block;
        overflow: hidden;
        white-space: pre;
        width: 0;
        border-right: 2px solid transparent;
        animation-name: typeLine;
        animation-fill-mode: forwards;
    }
    .code-line-blank { height: 14px; }
    .code-plain { color: #4AF626; }
    .code-comment { color: #6a9955; font-style: italic; }
    .code-string { color: #ce9178; }
    @keyframes typeLine {
        0%    { width: 0; border-color: #4AF626; }
        99.9% { border-color: #4AF626; }
        100%  { width: var(--chars); border-color: transparent; }
    }
    .landing-accent { color: #2E75B6; }
    .landing-cta-row {
        display: flex; align-items: center; gap: 22px; flex-wrap: wrap;
        margin: 24px 0 10px 0; padding: 0 10px;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to   { opacity: 1; }
    }
    .landing-right {
        opacity: 0; animation: popIn 1.2s ease-out 0.6s forwards;
    }
    .float-badge {
        opacity: 0; animation: fadeIn 0.8s ease-out 2s forwards;
    }
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
        flex: 1 1 340px; min-width: 340px; height: 360px;
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

    /* Certification card title - fixed height so cards align regardless of title length */
    .cert-body { min-height: 235px; display: flex; flex-direction: column; padding-top: 14px; }
    .cert-title { min-height: 50px; display: flex; align-items: flex-start; margin-bottom: 8px; }
    .cert-title h3 { margin: 0; border-bottom: none !important; line-height: 1.25; font-size: 17px; text-align: left !important; }
    .cert-dept { color: #8a97a8; font-size: 14px; line-height: 1.4; min-height: 40px; margin-bottom: 10px; }
    .cert-meta { font-size: 14.5px; font-weight: 600; margin-bottom: 6px; }
    .cert-no-verify {
        display: inline-block; margin-top: 6px; padding: 8px 16px;
        border-radius: 8px; font-size: 13.5px; font-weight: 600;
        background: rgba(255,255,255,0.06); color: #8a97a8;
    }

    /* Responsive: smaller screens */
    @media (max-width: 900px) {
        .landing-hero { flex-direction: column; text-align: center; }
        .code-editor { max-width: 100%; text-align: left; }
        .landing-cta-row { justify-content: center; }
        .landing-right { height: 360px; min-width: 340px; }
        .landing-photo { width: 150px; height: 150px; }
        .ring-1 { width: 190px; height: 190px; }
        .ring-2 { width: 230px; height: 230px; }
    }
</style>
""", unsafe_allow_html=True)

if dark_mode:
    st.markdown("""
    <style>
        .stApp { background-color: #0F1C2E !important; color: #EAF2FB !important; }
        section[data-testid="stSidebar"] { background: #16283F !important; border-right: 1px solid #263B54 !important; }
        section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3, section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] li, section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] div, section[data-testid="stSidebar"] label {
            color: #EAF2FB !important;
        }
        .sidebar-name { color: #EAF2FB !important; }
        h1, h2, h3, p, li, span, div, label { color: #EAF2FB; }
        h2, h3 { border-bottom: 3px solid #4A90D9 !important; color: #EAF2FB !important; }
        a, .stMarkdown a { color: #7FB3E8 !important; }

        div[data-testid="stMetric"] {
            background: #16283F !important; border: 1px solid #29405E !important;
        }
        div[data-testid="stMetricLabel"] { color: #B7CBE3 !important; }
        div[data-testid="stMetricValue"] { color: #7FB3E8 !important; }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            background: #16283F !important; border-color: #29405E !important;
        }

        .skill-row span:first-child { color: #EAF2FB !important; }
        .skill-bar-bg { background: #29405E !important; border-color: #3A5478 !important; }
        .skill-bar-fill { background: linear-gradient(90deg, #4A90D9, #7FB3E8) !important; }

        .cert-title h3 { color: #EAF2FB !important; }
        .stat-icon-item .label { color: #B7CBE3 !important; }
        .big-stat-item .label { color: #B7CBE3 !important; }
        .skill-pct { color: #7FB3E8 !important; }

        hr { border-color: #29405E !important; }

        .landing-cta-plain { color: #EAF2FB !important; }
        .landing-social a { color: #B7CBE3 !important; }
        .bullet-plain { color: #EAF2FB !important; }

        .float-badge { background: #EAF2FB !important; border-color: #29405E !important; }

        .stDownloadButton>button, .stLinkButton>a, .stButton>button {
            background-color: #4A90D9 !important; color: #0F1C2E !important;
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
            "<div class='sidebar-name' style='font-weight:800; font-size:16px; line-height:1.2;'>Shan Bhathiya Nawarathna</div>",
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
        ("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg", "HTML5"),
        ("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/firebase/firebase-plain.svg", "Firebase"),
        ("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg", "Git"),
        ("https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/microsoftoffice.svg", "Microsoft Office"),
        ("https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/powerbi.svg", "Power BI"),
        ("https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/tableau.svg", "Tableau"),
    ]
    _n = len(_skill_badges)
    _radius_px = 155  # pixels from center - clear of the ring
    badge_html = ""
    for _i, (_url, _alt) in enumerate(_skill_badges):
        _angle = (2 * math.pi * _i / _n) - (math.pi / 2)
        _x = _radius_px * math.cos(_angle)
        _y = _radius_px * math.sin(_angle)
        badge_html += (
            f'<div class="float-badge" title="{_alt}" style="left:calc(50% + {_x:.0f}px); top:calc(50% + {_y:.0f}px); '
            f'transform: translate(-50%,-50%);"><img src="{_url}" alt="{_alt}"></div>'
        )

    # Build the "code editor" typewriter block
    import html as _html
    CODE_LINES = [
        ("// Hello 👋", "comment"),
        ("const developer = {", "plain"),
        ('    name: "Shan Bhathiya",', "plain"),
        ('    role: "Web Developer",', "plain"),
        ("};", "plain"),
        None,  # blank spacer line
        ("/* Final-year Bachelor of Applied IT undergraduate,", "comment"),
        ("   comfortable across web development, networking,", "comment"),
        ("   cyber security, and embedded hardware. */", "comment"),
        None,
        ("run(developer);", "plain"),
    ]
    CHAR_SECONDS = 0.055   # typing speed per character (slow, deliberate)
    LINE_PAUSE = 0.28      # pause between lines
    _t = 0.4               # initial pause before typing starts

    code_lines_html = ""
    for _line in CODE_LINES:
        if _line is None:
            code_lines_html += '<div class="code-line-blank"></div>'
            _t += 0.2
            continue
        _text, _kind = _line
        _n = max(len(_text), 1)
        _dur = max(_n * CHAR_SECONDS, 0.25)
        _cls = "code-comment" if _kind == "comment" else "code-plain"
        _safe = _html.escape(_text)
        code_lines_html += (
            f'<div class="code-line {_cls}" style="--chars:{_n}ch; '
            f'animation-duration:{_dur:.2f}s; animation-delay:{_t:.2f}s; '
            f'animation-timing-function:steps({_n},end);">{_safe}</div>'
        )
        _t += _dur + LINE_PAUSE

    st.markdown(f"""
    <div class="landing-hero">
        <div class="landing-left">
            <div class="code-editor">
                <div class="code-editor-topbar">
                    <span class="code-dot red"></span>
                    <span class="code-dot yellow"></span>
                    <span class="code-dot green"></span>
                    <span class="code-editor-filename">shan.js</span>
                </div>
                <div class="code-editor-body">
                    {code_lines_html}
                </div>
            </div>
        </div>
        <div class="landing-right">
            <div class="deco-ring ring-1"></div>
            <div class="deco-ring ring-2"></div>
            {badge_html}
            {photo_html}
        </div>
    </div>
    <div class="landing-cta-row">
        <a href="javascript:void(0)" onclick="var el=document.getElementById('about-me'); if(el){{el.scrollIntoView({{behavior:'smooth'}});}}" class="landing-cta-plain">About Me</a>
        <span class="landing-social">
            <a href="https://www.linkedin.com/in/shan-bhathiya-1999283ab" target="_blank">LinkedIn</a>
            <a href="https://github.com/shanweerasinghe3999-cmd" target="_blank">GitHub</a>
            <a href="mailto:shanweerasinghe3999@gmail.com">Email</a>
        </span>
    </div>

    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="big-stat-row">
        <div class="big-stat-item"><div class="num">1</div><div class="label">Major Project</div></div>
        <div class="big-stat-item"><div class="num">4</div><div class="label">Certifications</div></div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2.4, 0.8], gap="small")

    # --- Column 1: Highlights + small Experience chart ---
    with col1:
        st.subheader("⭐ Highlights")
        st.markdown("""
        <div class="bullet-plain">• Built a full IoT-to-cloud energy system</div>
        <div class="bullet-plain">• Certified in Python &amp; Web Design</div>
        <div class="bullet-plain">• 5+ years combined work &amp; IT experience</div>
        """, unsafe_allow_html=True)

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
            "undergraduate at SLTC Research University. Before moving into IT, I worked in banking "
            "customer service and production data entry roles that built the attention to detail, "
            "problem-solving, and communication skills I now bring to software development."
        )
        st.write(
            "I'm focused on web development, with growing experience in Angular, JavaScript, "
            "TypeScript, Python, Java, HTML, CSS, SQL, Firebase, and Git. I'm also exploring "
            "Business Intelligence and data analytics (Power BI, Tableau) as a way to combine my "
            "interest in building applications with making sense of data."
        )
        st.write(
            "Through academic and personal projects, I've developed web applications, IoT-based "
            "systems, and data-driven solutions applying the same accuracy and follow-through I "
            "relied on when handling customer accounts and production records."
        )
        st.write(
            "I'm a motivated, continuous learner looking to start my career as a Web Developer, "
            "and to grow toward roles in software engineering or business intelligence over time."
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
                f'<div class="skill-row"><span>{name}</span></div>'
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
            st.caption("Feb 2019 – Dec 2020")
            st.write("• Worked with customers to find banking products for them like savings accounts, fixed deposits and credit cards based on what they needed.")
            st.write("• Made sure a number of credit cards and other banking products were sold every month, consistently hitting targets.")
            st.write("• Reviewed each customer's information to check credit eligibility and determine appropriate credit limits.")
            st.write("• Helped customers apply for credit cards, checked their documents, and followed up to ensure approvals were processed on time.")
        with st.container(border=True):
            st.write("**Reebonn Lanka Pvt Ltd.**")
            st.caption("May 2024 – Dec 2024")
            st.write("• Entered production data into the company system daily, ensuring accuracy and on-time reporting.")
            st.write("• Tracked raw materials, finished goods, and production volumes.")
            st.write("• Checked data for mistakes and fixed errors to keep records correct.")
            st.write("• Prepared simple production reports for supervisors and the management team.")

        st.markdown("---")
        st.subheader("🧰 Key Skills")
        with st.container(border=True):
            st.write("• Strong troubleshooting skills in hardware, software, and network systems")
            st.write("• Analytical & Problem-Solving Skills")
            st.write("• Strong Attention to Detail")
            st.write("• Customer Relationship Management")
            st.write("• Sales & Target Achievement")
            st.write("• Documentation & Reporting")

    with col_edu:
        st.subheader("🎓 Education")
        with st.container(border=True):
            st.write("**Bachelor's Degree in Applied Information Technology**")
            st.caption("SLTC Research University · 2023 – Present")
        with st.container(border=True):
            st.write("**Diploma in English**")
            st.caption("British Way English Academy · Dec 2022 – Feb 2023")
        with st.container(border=True):
            st.write("**Basic Computer Course**")
            st.caption("Zonal Information & Communication Technology Education Center, Sri Jayawardenepura Zone")
        with st.container(border=True):
            st.write("**Computer Literacy Course**")
            st.caption("Open University of Sri Lanka")

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
    st.caption("Online learning programmes, workshops, and courses completed")

    CERTS = [
        {
            "image": "cert_python_beginners.jpg",
            "title": "Python for Beginners",
            "dept": "Dept. of Computer Science &amp; Engineering, University of Moratuwa",
            "issued": "Jul 2025",
            "ref_label": "Code",
            "ref_value": "q1TNowBo5z",
            "verify_url": "https://open.uom.lk/verify",
        },
        {
            "image": "cert_python_programming.jpg",
            "title": "Python Programming",
            "dept": "Dept. of Computer Science &amp; Engineering, University of Moratuwa",
            "issued": "2025",
            "ref_label": "Code",
            "ref_value": "A7XtQFrrIF",
            "verify_url": "https://open.uom.lk/verify",
        },
        {
            "image": "cert_web_design.jpg",
            "title": "Web Design for Beginners",
            "dept": "Dept. of Information Technology, University of Moratuwa",
            "issued": "2025",
            "ref_label": "Code",
            "ref_value": "v6RIWfKclG",
            "verify_url": "https://open.uom.lk/verify",
        },
        {
            "image": "cert_frontend_webdev.jpg",
            "title": "Front-End Web Development",
            "dept": "Dept. of Information Technology, University of Moratuwa",
            "issued": "2025",
            "ref_label": "Code",
            "ref_value": "dRTkDGSG8K",
            "verify_url": "https://open.uom.lk/verify",
        },
        {
            "image": "cert_basic_computer.jpg",
            "title": "Basic Computer Course",
            "dept": "Zonal ICT Education Centre, Sri Jayawardhanapura Zone",
            "issued": "2016",
            "ref_label": "Reg. No.",
            "ref_value": "872487",
            "verify_url": None,
        },
        {
            "image": "cert_computer_literacy.jpg",
            "title": "Computer Literacy",
            "dept": "The Open University of Sri Lanka",
            "issued": "Dec 2020",
            "ref_label": "Serial No.",
            "ref_value": "CL2001070",
            "verify_url": None,
        },
    ]

    rows = [CERTS[i:i + 3] for i in range(0, len(CERTS), 3)]
    for row in rows:
        cols = st.columns(3)
        for col, cert in zip(cols, row):
            with col:
                with st.container(border=True):
                    cert_path = Path(__file__).parent / cert["image"]
                    if cert_path.exists():
                        st.image(str(cert_path), use_container_width=True)
                    st.markdown(f"""
                    <div class="cert-body">
                        <div class="cert-title"><h3>{cert['title']}</h3></div>
                        <div class="cert-dept">{cert['dept']}</div>
                        <div class="cert-meta">Issued: {cert['issued']}</div>
                        <div class="cert-meta">{cert['ref_label']}: {cert['ref_value']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    if cert["verify_url"]:
                        st.link_button("🔗 Verify", cert["verify_url"])
                    else:
                        st.markdown('<div class="cert-no-verify">📄 Physical certificate</div>', unsafe_allow_html=True)

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