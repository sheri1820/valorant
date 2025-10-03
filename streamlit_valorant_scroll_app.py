"""
streamlit_valorant_scroll_app.py
Single-file Streamlit app that renders a single-scroll Valorant-themed landing page.
Drop your BG1 image (bg1.jpg or bg1.png) in the same folder as this file and run:
    pip install -r requirements.txt
    streamlit run streamlit_valorant_scroll_app.py

The app injects a full custom HTML/CSS/JS page using components.html so animations run smoothly.
Customize text inside the HTML below or edit CSS variables for colors.
"""

import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(page_title="Valorant — Single Scroll", layout="wide")

# ------------------ helper: load image as base64 ------------------

def load_image_base64(paths):
    """Try multiple paths; return (b64, mime) or (None, None)."""
    for p in paths:
        if os.path.isfile(p):
            ext = os.path.splitext(p)[1].lower()
            mime = "image/png" if ext == ".png" else "image/jpeg"
            with open(p, "rb") as f:
                data = f.read()
            return base64.b64encode(data).decode("utf-8"), mime
    return None, None

# look for potential filenames
bg_b64, bg_mime = load_image_base64(["bg1.jpg", "bg1.png", "BG1.jpg", "BG1.png"]) 

# fallback SVG background (subtle abstract pattern) encoded as data URI
if not bg_b64:
    fallback_svg = """
    <svg xmlns='http://www.w3.org/2000/svg' width='1200' height='800' viewBox='0 0 1200 800'>
      <defs>
        <linearGradient id='g' x1='0' x2='1'>
          <stop offset='0' stop-color='#3b0d6f'/>
          <stop offset='1' stop-color='#784BBE'/>
        </linearGradient>
      </defs>
      <rect fill='url(#g)' x='0' y='0' width='1200' height='800' />
      <g opacity='0.08'>
        <circle cx='200' cy='200' r='300' fill='#fff'/>
        <circle cx='1050' cy='100' r='250' fill='#fff'/>
      </g>
    </svg>
    """
    bg_b64 = base64.b64encode(fallback_svg.encode('utf-8')).decode('utf-8')
    bg_mime = 'image/svg+xml'

bg_data_url = f"data:{bg_mime};base64,{bg_b64}"

# ------------------ HTML content ------------------
html = f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">
  <style>
    :root{{
      --main-purple: #784BBE;
      --accent: #e4d6ff;
      --glass: rgba(255,255,255,0.06);
      --text-1: #f5f6f8;
      --muted: rgba(245,246,248,0.75);
    }}
    html,body{{height:100%;margin:0;padding:0;font-family:Inter, system-ui, sans-serif;scroll-behavior:smooth;background:#0b0710;}}
    /* hide scrollbar in iframe-ish contexts for cleaner look (optional) */
    ::-webkit-scrollbar{{height:8px;width:8px}} 
    ::-webkit-scrollbar-thumb{{background:rgba(255,255,255,0.08);border-radius:10px}}

    .page{{width:100%;min-height:100vh;overflow-x:hidden}}

    .section{{min-height:100vh;display:flex;align-items:center;justify-content:center;padding:6vh 6vw;box-sizing:border-box}}

    /* HERO on BG1 */
    .hero{{
      background-image: url('{bg_data_url}');
      background-size:cover;background-position:center;position:relative;color:var(--text-1);
      display:flex;align-items:center;justify-content:center;flex-direction:column;text-align:center;gap:18px;padding-top:64px;padding-bottom:64px
    }}
    .hero::after{{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0.35),rgba(0,0,0,0.55));mix-blend-mode:overlay}}
    .hero-inner{{position:relative;z-index:2;max-width:1100px}}

    .kicker{{font-weight:600;letter-spacing:1px;color:var(--accent);text-transform:uppercase;font-size:14px}}
    .title{{font-size:48px;line-height:1.02;font-weight:800;margin:6px 0}}
    .subtitle{{font-size:18px;color:var(--muted);max-width:900px;margin:0 auto}}

    .cta-row{{display:flex;gap:14px;justify-content:center;margin-top:18px}}
    .btn{{padding:12px 22px;border-radius:10px;border:none;cursor:pointer;font-weight:600;text-decoration:none;display:inline-block}}
    .btn-cta{{background:linear-gradient(90deg,#ffd166,#ff6b6b);color:#111;box-shadow:0 8px 30px rgba(255,107,107,0.12);transform:translateZ(0);transition:transform .18s ease}}
    .btn-ghost{{background:transparent;border:1px solid rgba(255,255,255,0.14);color:var(--text-1)}}
    .btn-cta:hover{{transform:translateY(-4px);filter:brightness(1.02)}}

    /* sections 2-5 on solid / subtle gradient purple (user-specified) */
    .purple-section{{background:linear-gradient(180deg, rgba(120,75,190,0.95), var(--main-purple));color:var(--text-1);}}

    .card-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px;max-width:1200px;margin:30px auto}}
    .card{{background:rgba(255,255,255,0.03);padding:18px;border-radius:14px;backdrop-filter:blur(6px);box-shadow:0 6px 30px rgba(0,0,0,0.45);min-height:140px;display:flex;flex-direction:column;gap:8px}}
    .card h3{margin:0}

    /* animations */
    .animate{{opacity:0;transform:translateY(18px);transition:all 700ms cubic-bezier(.2,.9,.2,1);will-change:transform,opacity}}
    .in-view .animate{{opacity:1;transform:translateY(0)}}

    .slide-left{{opacity:0;transform:translateX(-40px);transition:all 850ms cubic-bezier(.2,.9,.2,1)}}
    .in-view .slide-left{{opacity:1;transform:translateX(0)}}

    .hero-visual{{width:360px;height:360px;border-radius:14px;background:linear-gradient(135deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));display:flex;align-items:center;justify-content:center;box-shadow:inset 0 1px 0 rgba(255,255,255,0.02), 0 10px 40px rgba(0,0,0,0.5);}}

    .muted{{color:var(--muted)}}

    footer{{padding:28px 6vw;text-align:center;color:var(--muted)}}

    /* responsiveness */
    @media (max-width:800px){{
      .title{{font-size:32px}}
      .hero-visual{{display:none}}
      .card-grid{{grid-template-columns:1fr}}
    }}

  </style>
</head>
<body>
  <div class="page">

    <!-- HERO (BG1) -->
    <section id="hero" class="section hero">
      <div class="hero-inner">
        <div class="kicker animate">Lock In • Team Play • Win</div>
        <h1 class="title slide-left">🎯 Lock In. Aim True. Claim Victory.</h1>
        <p class="subtitle animate">Step into the world of Valorant — a tactical 5v5 shooter where precision, strategy, and teamwork decide your fate.</p>
        <div class="cta-row animate">
          <a class="btn btn-cta" href="#agents">Play Now</a>
          <a class="btn btn-ghost" href="#about">Learn More</a>
        </div>
      </div>
    </section>

    <!-- About (purple) -->
    <section id="about" class="section purple-section" data-section="about">
      <div class="content animate">
        <h2 style="font-size:36px;margin:0 0 8px">What is Valorant?</h2>
        <p class="muted" style="max-width:900px">Valorant is not just another FPS — it’s a game of <strong>skill and creativity</strong>. With unique agents, mind-bending abilities, and razor-sharp gunplay, every round is a story waiting to unfold. Will you outsmart, outshoot, or outplay?</p>
      </div>
    </section>

    <!-- Agents (purple) -->
    <section id="agents" class="section purple-section">
      <div style="width:100%;max-width:1100px;margin:0 auto;">
        <h2 style="font-size:32px;margin:0">Choose Your Agent</h2>
        <p class="muted">From stealthy duelists to tactical controllers — every agent brings a unique playstyle to the battlefield.</p>
        <div class="card-grid animate">
          <div class="card">
            <h3>Duelist — Push & Frag</h3>
            <p class="muted">Fast, aggressive operatives built to get kills and open sites.</p>
          </div>
          <div class="card">
            <h3>Controller — Deny Vision</h3>
            <p class="muted">Map control masters who shape the battlefield with smokes and walls.</p>
          </div>
          <div class="card">
            <h3>Sentinel — Hold & Anchor</h3>
            <p class="muted">Strong defenders who lock down areas and protect teammates.</p>
          </div>
          <div class="card">
            <h3>Initiator — Set Plays</h3>
            <p class="muted">Create openings and gather intel to start the fight on your terms.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Maps (purple) -->
    <section id="maps" class="section purple-section">
      <div style="max-width:1100px;margin:0 auto;text-align:center">
        <h2 style="font-size:32px;margin:0">Master the Battlefield</h2>
        <p class="muted">Each map is a new playground for strategy. Learn every angle, every callout, every flank.</p>
        <div class="card-grid animate">
          <div class="card"><h3>Split</h3><p class="muted">Tight verticality, teamwork wins.</p></div>
          <div class="card"><h3>Breeze</h3><p class="muted">Open fights and long duels.</p></div>
          <div class="card"><h3>Ascent</h3><p class="muted">Control mid, control the round.</p></div>
        </div>
      </div>
    </section>

    <!-- Esports/Community (purple) -->
    <section id="esports" class="section purple-section">
      <div style="max-width:900px;margin:0 auto;text-align:center">
        <h2 style="font-size:32px;margin:0">Join the Valorant Universe</h2>
        <p class="muted">Valorant is more than a game — it’s a <strong>global phenomenon</strong>. From casual matches with friends to world-class esports tournaments, there’s always a place for you.</p>
        <div class="cta-row" style="justify-content:center;margin-top:18px">
          <a class="btn btn-ghost" href="#">Watch Tournaments</a>
          <a class="btn btn-ghost" href="#">Join the Community</a>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer>
      <div style="max-width:900px;margin:0 auto">
        <blockquote style="margin:0 0 10px;font-style:italic;color:var(--accent)">"It’s not just about pulling the trigger. It’s about who pulls it first."</blockquote>
        <div style="margin-top:12px;">🎮 <strong>Download Valorant.</strong> Step into the fight.</div>
      </div>
    </footer>

  </div>

  <script>
    // Simple intersection observer-based animation trigger
    const observer = new IntersectionObserver((entries)=>{
      entries.forEach(e=>{
        if(e.isIntersecting){
          e.target.classList.add('in-view');
        }
      });
    },{threshold:0.12});

    document.querySelectorAll('.section, .card, .hero-inner').forEach(el=>observer.observe(el));

    // Parallax effect for hero background
    const hero = document.getElementById('hero');
    window.addEventListener('scroll', ()=>{
      const rect = hero.getBoundingClientRect();
      const offset = Math.max(0, -rect.top);
      hero.style.backgroundPositionY = (offset * 0.25) + 'px';
    });

    // Smooth anchor handling inside the iframe/page
    document.querySelectorAll('a[href^="#"]').forEach(a=>{
      a.addEventListener('click', (ev)=>{
        ev.preventDefault();
        const id = a.getAttribute('href').substring(1);
        const el = document.getElementById(id);
        if(el) el.scrollIntoView({behavior:'smooth'});
      });
    });

    // Initial reveal of hero children
    window.addEventListener('load', ()=>{document.getElementById('hero').classList.add('in-view')});
  </script>
</body>
</html>
"""

# ------------------ render inside Streamlit ------------------

st.markdown("""

**Single-file Streamlit page loaded below.**

Put `bg1.jpg` or `bg1.png` in the same folder as this script to replace the hero background. If no image is present, a subtle purple SVG background is used.

""", unsafe_allow_html=True)

# set iframe height large so page scrolls inside it nicely; adjust as needed
components.html(html, height=1100, scrolling=True)

st.markdown("""
---
**Notes & quick customizations**

- To change the main purple color, update the `--main-purple` variable in the `<style>` section.
- To modify hero text, edit the content inside the `#hero` section of the HTML string.
- If your hero image is very large, consider replacing it with a web-optimized image (keep it ~1200–2500px wide).

""", unsafe_allow_html=True)
