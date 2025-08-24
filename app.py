import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Bhavana Talavar — Portfolio",
    layout="wide",
    initial_sidebar_state="auto"
)

# Hide Streamlit menu and footer
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- HTML content ---
html_content = """
<!doctype html>
<html lang="en" class="scroll-smooth">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Bhavana Talavar — Portfolio</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>
<script>
  tailwind.config = {
    theme: {
      extend: {
        fontFamily: { sans: ['Inter', 'ui-sans-serif', 'system-ui'] },
        colors: { bg: { DEFAULT: '#0b0f1a', soft: '#111624' }, acc: { DEFAULT: '#8b5cf6', soft: '#a78bfa' } },
        boxShadow: { soft: '0 10px 30px rgba(0,0,0,0.35)' }
      }
    }
  }
</script>
<style>
html, body { background: #0b0f1a; color: #e5e7eb; }
.glass { backdrop-filter: blur(10px); background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); }
</style>
</head>
<body class="font-sans antialiased">
<!-- Header -->
<header class="sticky top-0 z-50 bg-bg/80 backdrop-blur border-b border-white/10">
  <div class="mx-auto max-w-7xl px-4 py-4 flex items-center justify-between">
    <a href="#home" class="text-lg font-bold tracking-tight">Bhavana<span class="text-acc">.</span></a>
    <nav class="hidden md:flex gap-6 text-sm text-gray-300">
      <a href="#projects" class="hover:text-white">Projects</a>
      <a href="#skills" class="hover:text-white">Skills</a>
      <a href="#experience" class="hover:text-white">Experience</a>
      <a href="#contact" class="hover:text-white">Contact</a>
    </nav>
    <div class="flex items-center gap-3">
      <a href="https://github.com/bhavana9635" target="_blank" class="px-3 py-1.5 rounded-xl glass hover:bg-white/10 transition">GitHub</a>
      <a href="https://www.linkedin.com/in/bhavana-talavar-62ba72328/" target="_blank" class="px-3 py-1.5 rounded-xl bg-acc hover:bg-acc-soft text-white transition">LinkedIn</a>
    </div>
  </div>
</header>

<!-- Hero -->
<section id="home" class="relative overflow-hidden">
  <div class="absolute inset-0 -z-10" aria-hidden="true">
    <div class="absolute -top-24 -left-24 h-72 w-72 rounded-full bg-acc blur-3xl opacity-20"></div>
    <div class="absolute -bottom-24 -right-24 h-72 w-72 rounded-full bg-acc-soft blur-3xl opacity-20"></div>
  </div>
  <div class="mx-auto max-w-7xl px-4 pt-16 pb-12 grid md:grid-cols-2 gap-6 items-center">
    <div>
      <p class="text-acc-soft font-semibold mb-2">Developer • Problem Solver</p>
      <h1 class="text-4xl md:text-6xl font-extrabold leading-tight">Hi, I'm Bhavana Talavar</h1>
      <p class="mt-4 text-gray-300 max-w-xl">I build practical software—from ML prototypes and data dashboards to full‑stack web apps and system integrations. Currently exploring backend engineering, cloud, and AI‑assisted products.</p>
      <div class="mt-6 flex flex-wrap gap-3">
        <a href="#projects" class="px-4 py-2 rounded-2xl bg-acc hover:bg-acc-soft text-white shadow-soft transition">See Projects</a>
        <a href="#contact" class="px-4 py-2 rounded-2xl glass hover:bg-white/10 transition">Contact</a>
      </div>
    </div>
    <div class="md:justify-self-end">
      <div class="glass rounded-3xl p-6 md:p-8">
        <h3 class="text-lg font-semibold mb-3">Quick Stats</h3>
        <div id="stats" class="grid grid-cols-3 gap-4 text-center"></div>
      </div>
    </div>
  </div>
</section>

<!-- Projects -->
<section id="projects" class="mx-auto max-w-7xl px-4 py-12">
  <div class="flex items-end justify-between mb-6">
    <h2 class="text-2xl md:text-3xl font-bold">Projects</h2>
    <div class="flex items-center gap-2 text-sm">
      <label for="projectFilter" class="text-gray-400">Sort:</label>
      <select id="projectFilter" class="bg-transparent border border-white/10 rounded-xl px-3 py-1.5">
        <option value="stars">Most stars</option>
        <option value="updated">Recently updated</option>
        <option value="name">Name A→Z</option>
      </select>
    </div>
  </div>
  <div id="projectGrid" class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6"></div>
</section>

<!-- Skills -->
<section id="skills" class="mx-auto max-w-7xl px-4 py-12">
  <h2 class="text-2xl md:text-3xl font-bold mb-6">Skills & Tools</h2>
  <div class="glass rounded-3xl p-6">
    <div class="grid md:grid-cols-3 gap-6 text-sm">
      <div>
        <h3 class="font-semibold text-white mb-2">Languages</h3>
        <ul class="text-gray-300 space-y-1 list-disc list-inside">
          <li>Python, Java, JavaScript/TypeScript, SQL</li>
          <li>PHP (Laravel), Dart (Flutter)</li>
        </ul>
      </div>
      <div>
        <h3 class="font-semibold text-white mb-2">Frameworks & Libraries</h3>
        <ul class="text-gray-300 space-y-1 list-disc list-inside">
          <li>Spring, Express, React, Streamlit</li>
          <li>Kafka, Grafana, Docker</li>
        </ul>
      </div>
      <div>
        <h3 class="font-semibold text-white mb-2">Data & ML</h3>
        <ul class="text-gray-300 space-y-1 list-disc list-inside">
          <li>Scikit‑learn, XGBoost, NLP basics</li>
          <li>PostgreSQL, MySQL, H2</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- Contact -->
<section id="contact" class="mx-auto max-w-7xl px-4 py-12">
  <div class="glass rounded-3xl p-6 md:p-8">
    <h2 class="text-2xl md:text-3xl font-bold mb-3">Get in touch</h2>
    <p class="text-gray-300 mb-4">Open to internships and entry‑level backend roles. Connect via email or LinkedIn.</p>
    <div class="flex flex-wrap gap-3">
      <a href="mailto:bhavana@example.com" class="px-4 py-2 rounded-2xl glass hover:bg-white/10">Email</a>
      <a href="https://www.linkedin.com/in/bhavana-talavar-62ba72328/" class="px-4 py-2 rounded-2xl bg-acc hover:bg-acc-soft text-white">LinkedIn</a>
    </div>
  </div>
</section>

<footer class="mx-auto max-w-7xl px-4 py-8 text-sm text-gray-400 text-center">
  © <span id="year"></span> Bhavana Talavar
</footer>

<!-- JS to load GitHub repos dynamically -->
<script>
const GH_USERNAME = 'bhavana9635';
const projectGrid = document.getElementById('projectGrid');

async function fetchRepos() {
  let page = 1;
  let allRepos = [];
  while(true) {
    const res = await fetch(`https://api.github.com/users/${GH_USERNAME}/repos?per_page=100&page=${page}`);
    const repos = await res.json();
    if (!repos || repos.length === 0) break;
    allRepos = allRepos.concat(repos.filter(r => !r.fork));
    page++;
  }
  return allRepos;
}

function renderRepos(repos) {
  projectGrid.innerHTML = repos.map(r => `
    <article class="glass rounded-3xl p-5 flex flex-col">
      <a href="${r.html_url}" target="_blank" class="text-lg font-semibold hover:underline">${r.name}</a>
      <p class="mt-2 text-sm text-gray-300">${r.description || ''}</p>
      <div class="mt-3 flex gap-3 text-sm">
        <a href="${r.html_url}" class="px-3 py-1.5 rounded-xl bg-acc hover:bg-acc-soft text-white">Code</a>
      </div>
    </article>
  `).join('');
}

document.addEventListener('DOMContentLoaded', async () => {
  const repos = await fetchRepos();
  renderRepos(repos);
  document.getElementById('year').textContent = new Date().getFullYear();
});
</script>
</body>
</html>
"""

# Render the portfolio in Streamlit
st.markdown(html_content, unsafe_allow_html=True)
