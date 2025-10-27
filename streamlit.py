# app.py
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json
import os
import time

st.set_page_config(page_title="Riley Chen — Portfolio", page_icon=":snake:", layout="wide")

# ========== Config & Assets ==========
ACCENT = "#00a6c6"   # pick a single accent for consistency
BG_LIGHT = "#f6fbfc"
BG_DARK = "#0f1720"
CARD_LIGHT = "#ffffff"
CARD_DARK = "#0b1114"
TEXT_LIGHT = "#0b1114"
TEXT_DARK = "#e8eef2"
FORMSUBMIT_EMAIL = "rchen92@buffalo.edu"  # contact destination (your existing one)

# Lottie loader helper
def load_lottie_url(url: str):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except Exception:
        return None
    return None

# remote lottie
lottie_coding = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# local lotties (these should exist in the project root)
def load_local_lottie(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return None

lottie_coding_local = load_local_lottie("coding.json")
lottie_food_local = load_local_lottie("food.json")

# ========== Theme detection ==========
# We'll provide a manual toggle that stores in localStorage via JS.
# The app will default to Streamlit's theme if available, otherwise light.
is_dark_default = False

# ========== Page CSS & JS ==========
page_css = f"""
<style>
/* Fonts */
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

:root{{
  --accent: {ACCENT};
  --bg-light: {BG_LIGHT};
  --bg-dark: {BG_DARK};
  --card-light: {CARD_LIGHT};
  --card-dark: {CARD_DARK};
  --text-light: {TEXT_LIGHT};
  --text-dark: {TEXT_DARK};
}}

html, body, [class*="css"] {{
  font-family: 'Roboto', sans-serif;
}}

/* Parallax animated background */
.bg-wrap {{
  position: fixed;
  inset: 0;
  z-index: -1;
  overflow: hidden;
  pointer-events: none;
  background: radial-gradient(circle at 10% 20%, rgba(0,166,198,0.06), transparent 10%),
              radial-gradient(circle at 80% 80%, rgba(0,166,198,0.04), transparent 8%),
              linear-gradient(120deg, rgba(0,166,198,0.02), transparent 40%, rgba(0,0,0,0.02));
  animation: bgFloat 20s infinite linear;
}

/* subtle floating motion */
@keyframes bgFloat {{
  0% {{ transform: translateY(0px) }}
  50% {{ transform: translateY(-20px) }}
  100% {{ transform: translateY(0px) }}
}}

/* container section */
.section {{
  border-radius: 14px;
  padding: 28px;
  margin-bottom: 28px;
  box-shadow: 0 8px 24px rgba(11,17,20,0.06);
  transition: transform 300ms ease, box-shadow 300ms ease, opacity 400ms ease;
  opacity: 0;
  transform: translateY(18px);
}}
.section.visible {{
  opacity: 1;
  transform: translateY(0);
}}

/* hover lift for project cards */
.card {{
  border-radius: 12px;
  padding: 18px;
  transition: transform 300ms cubic-bezier(.2,.9,.2,1), box-shadow 300ms ease;
  will-change: transform;
}}
.card:hover {{
  transform: translateY(-8px) scale(1.01);
  box-shadow: 0 18px 40px rgba(0,0,0,0.12);
}}

/* Lottie tilt effect */
.lottie-tilt {{
  transition: transform 300ms ease, filter 300ms ease;
  transform-origin: center;
}}
.lottie-tilt:hover {{
  transform: rotateZ(-3deg) scale(1.04);
  filter: drop-shadow(0 12px 20px rgba(0,0,0,0.12));
}}

/* project link */
.project-title a {{
  color: var(--accent);
  text-decoration: none;
}}
.project-title a:hover {{
  text-decoration: underline;
}}

/* tech badges */
.tech-badge {{
  display: inline-block;
  padding: 6px 10px;
  border-radius: 999px;
  font-weight: 600;
  margin: 4px 6px 4px 0;
  background: rgba(0,0,0,0.04);
}}

/* contact button */
.submit-btn {{
  background: var(--accent);
  color: white;
  border: none;
  padding: 10px 16px;
  border-radius: 10px;
  font-weight: 700;
  cursor: pointer;
}}
.submit-btn:hover {{
  transform: translateY(-3px);
  opacity: 0.95;
}}

/* small helper */
.small-muted {{
  color: rgba(0,0,0,0.55);
  font-size: 13px;
}}

/* scroll to top button */
#scrollTop {{
  position: fixed;
  right: 20px;
  bottom: 24px;
  z-index: 999;
  background: var(--accent);
  color: white;
  border: none;
  padding: 10px 12px;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.12);
  cursor: pointer;
  display: none;
}}
#scrollTop.show {{
  display: block;
}}

/* light/dark mode specifics (JS will toggle .dark on body) */
body.dark {{
  background: var(--bg-dark) !important;
  color: var(--text-dark) !important;
}}

/* inside cards text color */
.section, .card {{
  background: var(--card-light);
  color: var(--text-light);
}}
body.dark .section, body.dark .card {{
  background: var(--card-dark);
  color: var(--text-dark);
}}

/* nav */
.nav {{
  position: sticky;
  top: 14px;
  z-index: 50;
  padding: 16px 0;
  display:flex;
  gap:12px;
}}
.nav a {{
  color: inherit;
  text-decoration: none;
  padding: 8px 10px;
  border-radius: 8px;
  font-weight: 600;
}}
.nav a:hover {{
  background: rgba(0,0,0,0.04);
}}

/* responsive small screens adjustments */
@media (max-width: 768px) {{
  .section {{ padding: 18px; }}
}}
</style>

<div class="bg-wrap" aria-hidden="true"></div>

<script>
/* page-level JS: smooth reveal, smooth scroll, theme toggle, scroll to top */
function revealSections() {{
  const secs = document.querySelectorAll('.section');
  const obs = new IntersectionObserver((entries) => {{
    entries.forEach(e => {{
      if (e.isIntersecting) e.target.classList.add('visible');
    }});
  }}, {{threshold: 0.12}});
  secs.forEach(s => obs.observe(s));
}}

function showScrollTop() {{
  const btn = document.getElementById('scrollTop');
  window.addEventListener('scroll', () => {{
    if (window.scrollY > 400) btn.classList.add('show'); else btn.classList.remove('show');
  }});
}}

function setupThemeToggle() {{
  // read localStorage preference
  const preferred = localStorage.getItem('site-theme') || 'light';
  document.body.classList.toggle('dark', preferred === 'dark');
  const toggle = document.getElementById('themeToggle');
  if (toggle) toggle.checked = preferred === 'dark';
  if (toggle) toggle.addEventListener('change', (e) => {{
    const dark = e.target.checked;
    document.body.classList.toggle('dark', dark);
    localStorage.setItem('site-theme', dark ? 'dark' : 'light');
  }});
}}

function setupAnchors() {{
  // smooth anchors
  document.querySelectorAll('a[href^="#"]').forEach(a => {{
    a.addEventListener('click', (ev) => {{
      ev.preventDefault();
      const target = document.querySelector(a.getAttribute('href'));
      if (target) target.scrollIntoView({{behavior: "smooth", block: "start"}});
    }});
  }});
}}

window.addEventListener('load', () => {{
  revealSections();
  showScrollTop();
  setupThemeToggle();
  setupAnchors();
}});
</script>
"""

# ========== Render CSS/JS ==========
st.markdown(page_css, unsafe_allow_html=True)

# Add scroll-to-top button
st.markdown("""
<button id="scrollTop" title="Back to top" onclick="window.scrollTo({top:0,behavior:'smooth'})">↑ Top</button>
""", unsafe_allow_html=True)

# Top navbar row with theme toggle and quick links
nav_cols = st.columns([1, 2, 1])
with nav_cols[0]:
    st.markdown("<div style='display:flex; align-items:center; gap:10px'><h3 style='margin:0'>Riley Chen</h3><span class='small-muted' style='margin-left:8px'>Actuarial Math • UB</span></div>", unsafe_allow_html=True)
with nav_cols[1]:
    st.markdown("""
    <div class="nav" role="navigation" aria-label="Main">
      <a href="#about">About</a>
      <a href="#projects">Projects</a>
      <a href="#tech">Tech</a>
      <a href="#contact">Contact</a>
    </div>
    """, unsafe_allow_html=True)
with nav_cols[2]:
    st.markdown("""
    <div style="display:flex; justify-content:flex-end; align-items:center; gap:8px;">
      <label class="small-muted" for="themeToggle" style="margin-right:6px">Dark</label>
      <input type="checkbox" id="themeToggle" />
    </div>
    """, unsafe_allow_html=True)

# ---------- About Section ----------
st.markdown('<a id="about"></a>', unsafe_allow_html=True)
with st.container():
    cols = st.columns([1.2, 1, 0.8])
    with cols[0]:
        st.markdown('<div class="section card">', unsafe_allow_html=True)
        st.markdown("<h2 style='margin-top:6px'>Hello, I am Riley 👋</h2>", unsafe_allow_html=True)
        st.markdown("""
        <p class="small-muted">Actuarial mathematics student with a minor in statistics. I like building practical solutions and cleaner user experiences. Outside of code, I train BJJ and tinker with gadgets.</p>
        <ul>
          <li><strong>Study</strong>: Mathematics (Actuarial Science)</li>
          <li><strong>Location</strong>: Buffalo, NY</li>
          <li><strong>Interests</strong>: BJJ, Gym, Badminton, Soccer, Food</li>
        </ul>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with cols[1]:
        # Remote Lottie
        if lottie_coding:
            st.markdown('<div class="section card lottie-tilt">', unsafe_allow_html=True)
            st_lottie(lottie_coding, height=240, key="about_lottie_remote")
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.image("https://via.placeholder.com/320x220.png?text=Animation", width=320)

    with cols[2]:
        st.markdown('<div class="section card">', unsafe_allow_html=True)
        st.markdown("###### Quick links")
        st.markdown("- [LinkedIn](https://www.linkedin.com/in/riley-chen--)")
        st.markdown("- [Personal site] (this)")
        st.markdown("<hr/>", unsafe_allow_html=True)
        st.markdown("<h4 style='margin-bottom:6px'>Now</h4>", unsafe_allow_html=True)
        st.markdown('<div id="nowPlaying" class="small-muted">Loading...</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Small script to rotate fun facts
fun_facts = [
    "Training BJJ 🥋",
    "Studying for Exam P 📘",
    "Working on My Website 🍔",
    "Listening to Lo-fi while doing HW 🎧",
    "Tinkering with my PC build 🖥️"
]
# expose fun facts via a tiny JS that cycles them
st.markdown(f"""
<script>
const facts = {json.dumps(fun_facts)};
let i = 0;
const el = document.getElementById('nowPlaying');
if (el) {{
  el.textContent = facts[0];
  setInterval(()=> {{
    i = (i+1) % facts.length;
    el.textContent = facts[i];
  }}, 2800);
}}
</script>
""", unsafe_allow_html=True)

# ---------- Projects Section ----------
st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
st.header("What I have been building")
st.write("A few recent projects and why they matter.")

# Project 1 (personal site)
with st.container():
    row_cols = st.columns([1, 2])
    with row_cols[0]:
        st.markdown('<div class="section card lottie-tilt">', unsafe_allow_html=True)
        if lottie_coding_local:
            st_lottie(lottie_coding_local, height=200, key="proj1_local_lottie")
        else:
            st.image("https://via.placeholder.com/240x180.png?text=Project", width=240)
        st.markdown("</div>", unsafe_allow_html=True)
    with row_cols[1]:
        st.markdown('<div class="section card project-title">', unsafe_allow_html=True)
        st.markdown('<h3 class="project-title"><a href="https://rileychen.streamlit.app/" target="_blank">Personal Website</a></h3>', unsafe_allow_html=True)
        st.markdown("<p>I built this portfolio using Streamlit to prototype UI patterns quickly. It includes an interactive contact form and usage analytics that helped me improve engagement.</p>", unsafe_allow_html=True)
        st.markdown("<p class='small-muted'><strong>Impact:</strong> improved inbound messages and faster prototyping for course projects.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Project 2 (Campus Crumbs)
with st.container():
    row_cols = st.columns([1, 2])
    with row_cols[0]:
        st.markdown('<div class="section card lottie-tilt">', unsafe_allow_html=True)
        if lottie_food_local:
            st_lottie(lottie_food_local, height=200, key="proj2_local_lottie")
        else:
            st.image("https://via.placeholder.com/240x180.png?text=Food+App", width=240)
        st.markdown("</div>", unsafe_allow_html=True)
    with row_cols[1]:
        st.markdown('<div class="section card project-title">', unsafe_allow_html=True)
        st.markdown('<h3 class="project-title"><a href="https://campuscrumbs.streamlit.app/" target="_blank">Campus Crumbs</a></h3>', unsafe_allow_html=True)
        st.markdown("<p>A dorm food delivery platform for budget-conscious students using campus meal plans. Built to reduce friction and save time.</p>", unsafe_allow_html=True)
        st.markdown("<p class='small-muted'><strong>Note:</strong> prototype uses mock ordering; production would need campus integration and auth.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Optional: add a gallery or more projects in alternating layout
st.markdown("""
<div class="section card">
  <h4>More</h4>
  <p class="small-muted">I also prototype small utilities, data visualizations, and simulation demos for coursework.</p>
</div>
""", unsafe_allow_html=True)

# ---------- Tech stack ----------
st.markdown('<a id="tech"></a>', unsafe_allow_html=True)
st.header("Tech I use")
st.markdown('<div class="section card">', unsafe_allow_html=True)
st.markdown("""
<span class="tech-badge">Python</span>
<span class="tech-badge">Streamlit</span>
<span class="tech-badge">Pandas</span>
<span class="tech-badge">JavaScript</span>
<span class="tech-badge">Lottie</span>
<span class="tech-badge">HTML/CSS</span>
<span class="tech-badge">Git</span>
""", unsafe_allow_html=True)
st.markdown("<p class='small-muted'>I focus on tools that let me ship small, testable ideas quickly.</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ---------- Feedback widgets (emoji-based) ----------
st.markdown("<hr/>", unsafe_allow_html=True)
st.markdown('<div class="section card"><h4>Quick feedback</h4><p class="small-muted">Tap an emoji to give 1-second feedback. It sends your response to formsubmit.</p>', unsafe_allow_html=True)

feedback_col1, feedback_col2, feedback_col3 = st.columns([1,1,3])
with feedback_col1:
    if st.button("❤️ Love it"):
        # send to formsubmit via a simple request if available
        try:
            requests.post(f"https://formsubmit.co/{FORMSUBMIT_EMAIL}", data={
                "feedback": "love it",
                "source": "portfolio_quick_feedback"
            })
        except Exception:
            pass
        st.success("Thanks! noted.")
with feedback_col2:
    if st.button("😐 Meh"):
        try:
            requests.post(f"https://formsubmit.co/{FORMSUBMIT_EMAIL}", data={
                "feedback": "meh",
                "source": "portfolio_quick_feedback"
            })
        except Exception:
            pass
        st.info("Got it. thanks.")
with feedback_col3:
    if st.button("👎 Not for me"):
        try:
            requests.post(f"https://formsubmit.co/{FORMSUBMIT_EMAIL}", data={
                "feedback": "not for me",
                "source": "portfolio_quick_feedback"
            })
        except Exception:
            pass
        st.warning("Understood. appreciate it.")

st.markdown("</div>", unsafe_allow_html=True)

# ---------- Contact form ----------
st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
st.header("Contact Me")
st.markdown('<div class="section card">', unsafe_allow_html=True)

contact_left, contact_right = st.columns([2,1])
with contact_left:
    st.markdown("<h3>Say hi or propose a project</h3>", unsafe_allow_html=True)
    # Provide a friendly microcopy
    st.markdown("<p class='small-muted'>I read every message. If you want to chat about internships or projects, drop a note.</p>", unsafe_allow_html=True)

    # A Streamlit form that will also forward to FormSubmit as fallback
    with st.form(key="contact_form"):
        name = st.text_input("Your name", placeholder="First and last")
        email = st.text_input("Your email", placeholder="you@company.com")
        message = st.text_area("Your message", placeholder="Short note about who you are and why you're reaching out.")
        submit = st.form_submit_button("Send message")
        if submit:
            # local acknowledgment
            st.success("Message queued. I will get back to you.")
            # Post to formsubmit
            try:
                requests.post(f"https://formsubmit.co/{FORMSUBMIT_EMAIL}", data={
                    "name": name or "anonymous",
                    "email": email or "no-email",
                    "message": message or "(empty)",
                    "source": "portfolio_contact_form"
                })
            except Exception:
                # ignore network errors
                pass

with contact_right:
    st.markdown("<h4>Other ways</h4>", unsafe_allow_html=True)
    st.markdown("- LinkedIn: [Connect](https://www.linkedin.com/in/riley-chen--)")
    st.markdown("- Resume: attach a download link in your deployed app or mail me")
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.markdown("<h4>Availability</h4>", unsafe_allow_html=True)
    st.markdown("<p class='small-muted'>Most weekdays after 11:00 AM. I try to reply within 48 hours.</p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown("""
<footer style="margin-top:36px; padding:12px 0; text-align:center;">
  <span class="small-muted">Built with Streamlit • Designed for clarity • © Riley Chen</span>
</footer>
""", unsafe_allow_html=True)

# ================== End ==================
