import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Bhavana Talavar — Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Hide Streamlit menu and footer
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    body {background-color: #0b0f1a;}
    hr {border: 1px solid #333;}
    a {text-decoration: none;}
    .card:hover {transform: scale(1.02); transition: all 0.3s ease-in-out;}
    .timeline {border-left: 2px solid #8b5cf6; margin-left:20px; padding-left:20px;}
    .timeline-item {margin-bottom:20px;}
    .timeline-item h3 {margin:0; color:#8b5cf6;}
    .timeline-item p {margin:5px 0; color:#d1d5db;}
    </style>
""", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.markdown("<h2 style='color:#8b5cf6'>Bhavana Talavar</h2>", unsafe_allow_html=True)
st.sidebar.markdown("""
- [Home](#home)
- [Education](#education)
- [Projects](#projects)
- [Skills](#skills)
- [Experience](#experience)
- [Certifications](#certifications)
- [Contact](#contact)
""", unsafe_allow_html=True)

# --- HTML content ---
html_content = """
<div id="home" style="text-align:center;">
  <img src="https://avatars.githubusercontent.com/u/000000?v=4" alt="Profile" style="width:150px;border-radius:50%;margin-bottom:15px;">
  <h1 style="color:white; font-size:3rem;">Hi, I'm <span style="color:#8b5cf6;">Bhavana Talavar</span></h1>
  <p style="color:#d1d5db; font-size:1.1rem;">Developer • Problem Solver | Building ML apps, dashboards, and full-stack solutions.</p>
  <div style="margin-top:10px;">
    <a href='#projects' style='padding:10px 20px;background:#8b5cf6;color:white;border-radius:12px;'>See Projects</a>
    <a href='#contact' style='padding:10px 20px;border:1px solid #fff;color:white;border-radius:12px;margin-left:10px;'>Contact Me</a>
  </div>
</div>

<hr>

<div id="education">
  <h2 style='color:white; font-size:2rem;'>Education</h2>
  <div style='display:flex; flex-direction:column; gap:15px;'>
    <div class="card" style='background:#111624; padding:15px; border-radius:12px;'>
      <h3 style='color:#8b5cf6;'>PES University — B.Tech, Computer Science</h3>
      <p style='color:#d1d5db;'>Expected Graduation: June 2026</p>
      <p style='color:#999;'>Coursework: Machine Intelligence, Data Analytics, Cloud Computing, DBMS, OS, DSA</p>
    </div>
    <div class="card" style='background:#111624; padding:15px; border-radius:12px;'>
      <h3 style='color:#8b5cf6;'>Excellent Science PU College</h3>
      <p style='color:#d1d5db;'>PUC (2022) — 90.3%</p>
    </div>
  </div>
</div>

<hr>

<div id="projects">
  <h2 style='color:white; font-size:2rem;'>Projects</h2>
  <p style='color:#d1d5db;'>Click to view on GitHub</p>
  <div style='display:flex; flex-wrap:wrap; gap:20px;'>
    <div class="card" style='background:#111624; padding:20px; border-radius:15px; flex:1 1 300px;'>
      <a href='https://github.com/bhavana9635/Inventory-Management-System' target='_blank' style='color:#8b5cf6; font-weight:bold;'>Inventory Management System</a>
      <p style='color:#d1d5db;'>Spring Boot + MySQL, role-based dashboards, authentication, CRUD operations.</p>
    </div>
    <div class="card" style='background:#111624; padding:20px; border-radius:15px; flex:1 1 300px;'>
      <a href='https://github.com/bhavana9635/Blockchain-Voting-System' target='_blank' style='color:#8b5cf6; font-weight:bold;'>Blockchain Voting System</a>
      <p style='color:#d1d5db;'>Solidity smart contracts + Hardhat + MetaMask integration.</p>
    </div>
    <div class="card" style='background:#111624; padding:20px; border-radius:15px; flex:1 1 300px;'>
      <a href='https://github.com/bhavana9635/Flood-Prediction-ML' target='_blank' style='color:#8b5cf6; font-weight:bold;'>Flood Prediction ML</a>
      <p style='color:#d1d5db;'>Random Forest + AI chatbot (Llama2 + Streamlit) with OpenWeather API.</p>
    </div>
  </div>
</div>

<hr>

<div id="skills">
  <h2 style='color:white; font-size:2rem;'>Skills & Tools</h2>
  <div style='display:flex; flex-wrap:wrap; gap:20px;'>
    <div class="card" style='background:#111624; padding:15px; border-radius:12px; flex:1 1 250px;'>
      <h3 style='color:#8b5cf6;'>Languages</h3>
      <ul style='color:#d1d5db;'><li>Python, Java, JavaScript/TypeScript, SQL</li><li>PHP (Laravel), Dart (Flutter)</li></ul>
    </div>
    <div class="card" style='background:#111624; padding:15px; border-radius:12px; flex:1 1 250px;'>
      <h3 style='color:#8b5cf6;'>Frameworks & Libraries</h3>
      <ul style='color:#d1d5db;'><li>Spring, Express, React, Streamlit</li><li>Kafka, Grafana, Docker</li></ul>
    </div>
    <div class="card" style='background:#111624; padding:15px; border-radius:12px; flex:1 1 250px;'>
      <h3 style='color:#8b5cf6;'>Data & ML</h3>
      <ul style='color:#d1d5db;'><li>Scikit-learn, XGBoost, NLP basics</li><li>PostgreSQL, MySQL, H2</li></ul>
    </div>
  </div>
</div>

<hr>

<div id="experience">
  <h2 style='color:white; font-size:2rem;'>Experience</h2>
  <div class="timeline">
    <div class="timeline-item">
      <h3>Teaching Assistant — PES University</h3>
      <p>Aug 2025 – Present | Bengaluru</p>
      <p style='color:#999;'>Part-time role in Web Development and Web Technologies.</p>
    </div>
    <div class="timeline-item">
      <h3>Data Scientist Intern — Oasis Infobyte</h3>
      <p>Nov 2024 – Dec 2024</p>
      <p style='color:#999;'>Applied ML models on datasets, delivered concise analysis & model comparisons.</p>
    </div>
  </div>
</div>

<hr>

<div id="certifications">
  <h2 style='color:white; font-size:2rem;'>Certifications</h2>
  <ul style='color:#d1d5db;'>
    <li>Data Analytics Job Simulation — Deloitte Australia</li>
    <li>Generative AI–Powered Data Analytics Simulation — Tata Group</li>
    <li>AICTE OIB-SIP Internship in Data Science</li>
  </ul>
</div>

<hr>

<div id="contact">
  <h2 style='color:white; font-size:2rem;'>Contact Me</h2>
  <p style='color:#d1d5db;'>Open to internships & backend roles. Connect via email or LinkedIn.</p>
  <div style='margin-top:10px;'>
    <a href='mailto:bhavanatalawar282@gmail.com' style='padding:10px 20px;border:1px solid #fff;color:white;border-radius:12px;margin-right:10px;'>Email</a>
    <a href='https://github.com/Bhavana' style='padding:10px 20px;background:#8b5cf6;color:white;border-radius:12px;margin-right:10px;'>GitHub</a>
    <a href='https://www.linkedin.com/in/bhavana-talavar-62ba72328/' style='padding:10px 20px;background:#8b5cf6;color:white;border-radius:12px;'>LinkedIn</a>
  </div>
</div>

<footer style='color:#777; text-align:center; margin-top:30px;'>© 2025 Bhavana Talavar</footer>
"""

# Render in Streamlit
st.markdown(html_content, unsafe_allow_html=True)
