import streamlit as st

# Page config
st.set_page_config(
    page_title="Bhavana Talavar — Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Hide Streamlit UI
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    body {background-color: #0b0f1a;}
    hr {border: 1px solid #333;}
    a {text-decoration: none;}
    .card:hover {transform: scale(1.02); transition: all 0.3s ease-in-out;}
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
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

# --- HTML Content ---
html_content = """
<div id="home">
  <h1 style="color:white; font-size:3rem;">Hi, I'm <span style="color:#8b5cf6;">Bhavana Talavar</span></h1>
  <p style="color:#d1d5db; font-size:1.1rem;">
  Developer • Problem Solver | Building ML apps, dashboards, and full-stack solutions.
  </p>
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
      <p style='color:#999;'>Relevant Coursework: Software Engineering, Data Analytics, ML, Big Data, Cloud Computing.</p>
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
  <p style='color:#d1d5db;'>Explore my GitHub repositories</p>
  <div style='display:flex; flex-wrap:wrap; gap:20px;'>

    <div class="card" style='background:#111624; padding:20px; border-radius:15px; flex:1 1 300px;'>
      <a href='https://github.com/bhavana9635/Inventory-Management-System' target='_blank' style='color:#8b5cf6; font-weight:bold;'>Inventory Management System</a>
      <p style='color:#d1d5db;'>Spring Boot + MySQL app with role-based dashboards, authentication, reminders, and CRUD operations.</p>
    </div>

    <div class="card" style='background:#111624; padding:20px; border-radius:15px; flex:1 1 300px;'>
      <a href='https://github.com/bhavana9635/Flood-Prediction-ML' target='_blank' style='color:#8b5cf6; font-weight:bold;'>Flood Prediction ML</a>
      <p style='color:#d1d5db;'>Random Forest + AI chatbot (Llama2 + Streamlit) integrated with OpenWeather API.</p>
    </div>

    <div class="card" style='background:#111624; padding:20px; border-radius:15px; flex:1 1 300px;'>
      <a href='#' target='_blank' style='color:#8b5cf6; font-weight:bold;'>Application Monitoring Dashboards</a>
      <p style='color:#d1d5db;'>Kafka + PostgreSQL + Grafana dashboards for real-time monitoring of 10K+ logs/min.</p>
    </div>

  </div>
</div>

<hr>

<div id="skills">
  <h2 style='color:white; font-size:2rem;'>Skills</h2>
  <div style='display:flex; flex-wrap:wrap; gap:20px;'>

    <div class="card" style='background:#111624; padding:15px; border-radius:12px; flex:1 1 250px;'>
      <h3 style='color:#8b5cf6;'>Languages</h3>
      <p style='color:#d1d5db;'>Python, Java, C, JavaScript, SQL</p>
    </div>

    <div class="card" style='background:#111624; padding:15px; border-radius:12px; flex:1 1 250px;'>
      <h3 style='color:#8b5cf6;'>Web Development</h3>
      <p style='color:#d1d5db;'>React, Node.js, Express, Spring Boot, MongoDB, MySQL</p>
    </div>

    <div class="card" style='background:#111624; padding:15px; border-radius:12px; flex:1 1 250px;'>
      <h3 style='color:#8b5cf6;'>Machine Learning</h3>
      <p style='color:#d1d5db;'>Scikit-learn, Pandas, NumPy, LLM basics</p>
    </div>

    <div class="card" style='background:#111624; padding:15px; border-radius:12px; flex:1 1 250px;'>
      <h3 style='color:#8b5cf6;'>DevOps & Tools</h3>
      <p style='color:#d1d5db;'>Docker, Kubernetes, Git, Grafana, Kafka</p>
    </div>

  </div>
</div>

<hr>

<div id="experience">
  <h2 style='color:white; font-size:2rem;'>Experience</h2>
  <div style='display:flex; flex-direction:column; gap:15px;'>
    <div class="card" style='background:#111624; padding:15px; border-radius:12px;'>
      <h3 style='color:#8b5cf6;'>Teaching Assistant — PES University</h3>
      <p style='color:#d1d5db;'>Aug 2025 – Present | Bengaluru</p>
      <p style='color:#999;'>Part-time role in Web Development and Web Technologies.</p>
    </div>
    <div class="card" style='background:#111624; padding:15px; border-radius:12px;'>
      <h3 style='color:#8b5cf6;'>Data Scientist Intern — Oasis Infobyte</h3>
      <p style='color:#d1d5db;'>Nov 2024 – Dec 2024</p>
      <p style='color:#999;'>Applied ML models on datasets, delivered model comparisons & analysis.</p>
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
  <h2 style='color:white; font-size:2rem;'>Contact</h2>
  <p style='color:#d1d5db;'>Let’s connect for internships, backend roles, or ML projects 🚀</p>
  <div style='margin-top:10px;'>
    <a href='mailto:bhavanatalawar282@gmail.com' style='padding:10px 20px;border:1px solid #fff;color:white;border-radius:12px;margin-right:10px;'>Email</a>
    <a href='https://github.com/Bhavana' style='padding:10px 20px;background:#8b5cf6;color:white;border-radius:12px;margin-right:10px;'>GitHub</a>
    <a href='https://www.linkedin.com/in/bhavana-talavar-62ba72328/' style='padding:10px 20px;background:#8b5cf6;color:white;border-radius:12px;'>LinkedIn</a>
  </div>
</div>

<footer style='color:#777; text-align:center; margin-top:30px;'>© 2025 Bhavana Talavar</footer>
"""

st.markdown(html_content, unsafe_allow_html=True)
