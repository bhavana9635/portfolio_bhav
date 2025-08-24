import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Bhavana Talavar — Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Hide Streamlit menu, footer, and remove underline from links
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    body {background-color: #0b0f1a;}
    a {text-decoration: none !important;} /* Remove underlines from links */
    </style>
""", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.markdown("<h2 style='color:#8b5cf6'>Bhavana Talavar</h2>", unsafe_allow_html=True)
st.sidebar.markdown("""
- [Home](#home)
- [Projects](#projects)
- [Skills](#skills)
- [Experience](#experience)
- [Contact](#contact)
""", unsafe_allow_html=True)

# --- HTML content ---
html_content = """
<div id="home">
<h1 style="color:white; font-size:3rem;">Hi, I'm Bhavana Talavar</h1>
<p style="color:#d1d5db; font-size:1.1rem;">
Developer • Problem Solver | Building ML apps, dashboards, and full-stack solutions.
</p>
<div style="margin-top:10px;">
<a href='#projects' style='padding:10px 20px;background:#8b5cf6;color:white;border-radius:12px;'>See Projects</a>
<a href='#contact' style='padding:10px 20px;border:1px solid #fff;color:white;border-radius:12px;margin-left:10px;'>Contact Me</a>
</div>
</div>

<hr style='border:1px solid #333;'>

<div id="projects">
<h2 style='color:white; font-size:2rem;'>Projects</h2>
<p style='color:#d1d5db;'>Click to view on GitHub</p>
<div style='display:flex; flex-wrap:wrap; gap:20px;'>
  <div style='background:#111624; padding:20px; border-radius:15px; flex:1 1 300px; min-width:300px;'>
    <a href='https://github.com/bhavana9635/Inventory-Management-System' target='_blank' style='color:#8b5cf6; font-weight:bold;'>Inventory Management System</a>
    <p style='color:#d1d5db;'>Java + Spring Boot with H2 DB, CRUD catalog, dashboard, reminders.</p>
  </div>
  <div style='background:#111624; padding:20px; border-radius:15px; flex:1 1 300px; min-width:300px;'>
    <a href='https://github.com/bhavana9635/Blockchain-Voting-System' target='_blank' style='color:#8b5cf6; font-weight:bold;'>Blockchain Voting System</a>
    <p style='color:#d1d5db;'>Solidity smart contracts + Hardhat + MetaMask integration.</p>
  </div>
  <div style='background:#111624; padding:20px; border-radius:15px; flex:1 1 300px; min-width:300px;'>
    <a href='https://github.com/bhavana9635/Flood-Prediction-ML' target='_blank' style='color:#8b5cf6; font-weight:bold;'>Flood Prediction ML</a>
    <p style='color:#d1d5db;'>Random Forest + AI chatbot, Streamlit + OpenWeather API integration.</p>
  </div>
</div>
</div>

<hr style='border:1px solid #333;'>

<div id="skills">
  <h2 style='color:white; font-size:2rem;'>Skills</h2>
  <div style='display:flex; flex-wrap:wrap; gap:20px;'>

    <div style='background:#111624; padding:15px; border-radius:12px; flex:1 1 250px;'>
      <h3 style='color:#8b5cf6;'>Programming Languages</h3>
      <p style='color:#d1d5db;'>Java, C, Python, SQL</p>
    </div>

    <div style='background:#111624; padding:15px; border-radius:12px; flex:1 1 250px;'>
      <h3 style='color:#8b5cf6;'>Web Development</h3>
      <p style='color:#d1d5db;'>HTML, CSS, JavaScript, React, Node.js, Express.js, MongoDB, Spring Boot</p>
    </div>

    <div style='background:#111624; padding:15px; border-radius:12px; flex:1 1 250px;'>
      <h3 style='color:#8b5cf6;'>Machine Learning & AI</h3>
      <p style='color:#d1d5db;'>Scikit-learn, Pandas, NumPy, LLM basics, Prompt Engineering</p>
    </div>

    <div style='background:#111624; padding:15px; border-radius:12px; flex:1 1 250px;'>
      <h3 style='color:#8b5cf6;'>DevOps & Tools</h3>
      <p style='color:#d1d5db;'>Docker, Kubernetes, Git, GitHub</p>
    </div>

    <div style='background:#111624; padding:15px; border-radius:12px; flex:1 1 250px;'>
      <h3 style='color:#8b5cf6;'>Soft Skills</h3>
      <p style='color:#d1d5db;'>Teamwork, Collaborative Problem-Solving, Adaptability</p>
    </div>

  </div>
</div>

<hr style='border:1px solid #333;'>

<div id="experience">
<h2 style='color:white; font-size:2rem;'>Experience</h2>
<div style='display:flex; flex-direction:column; gap:15px;'>
  <div style='background:#111624; padding:15px; border-radius:12px;'>
    <h3 style='color:#8b5cf6;'>Data Scientist Intern — Oasis Infobyte</h3>
    <p style='color:#d1d5db;'>Nov 2024 – Dec 2024: Applied ML models on real-world datasets, analysis & model comparisons.</p>
  </div>
</div>
</div>

<hr style='border:1px solid #333;'>

<div id="contact">
<h2 style='color:white; font-size:2rem;'>Contact Me</h2>
<p style='color:#d1d5db;'>Open to internships & backend roles. Connect via email or LinkedIn.</p>
<div style='margin-top:10px;'>
  <a href='mailto:bhavana@example.com' style='padding:10px 20px;border:1px solid #fff;color:white;border-radius:12px;margin-right:10px;'>Email</a>
  <a href='https://www.linkedin.com/in/bhavana-talavar-62ba72328/' style='padding:10px 20px;background:#8b5cf6;color:white;border-radius:12px;'>LinkedIn</a>
</div>
</div>

<footer style='color:#777; text-align:center; margin-top:30px;'>
© Bhavana Talavar
</footer>
"""

# Render in Streamlit
st.markdown(html_content, unsafe_allow_html=True)
