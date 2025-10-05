import streamlit as st
import streamlit.components.v1 as components

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Valorant Scroll Site", layout="wide")

# ---- GLOBAL CSS ----
st.markdown("""
<style>
/* Fullscreen app */
.main, .block-container, .stApp {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
}
html, body {
    margin: 0 !important;
    padding: 0 !important;
    width: 100% !important;
    height: 100% !important;
    overflow-x: hidden !important;
    background: #000;
    font-family: 'Poppins', sans-serif;
    color: white;
}

/* Hero section */
.hero {
    background-image: url("https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/28157301013%20(1)-Picsart-AiImageEnhancer.png");
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover;
    background-attachment: fixed;
    width: 100vw;
    height: 170vh;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    padding-top: 120px;
    align-items: center;
    color: white;
    text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
    margin: 0 !important;
    padding: 0 !important;
}

.hero h1, .hero p, .hero .btn {
    position: relative;
    top: -350px;
}

/* Sections */
.section {
    width: 100vw;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 50px;
    opacity: 0;
    transform: translateY(50px);
    transition: all 1s ease-out;
    position: relative;
    overflow: hidden;
}
.section.visible {
    opacity: 1;
    transform: translateY(0);
}

.bg-purple {
    background: #784BBE;
}

/* Typography */
h1 {
    font-size: 4rem;
    margin-bottom: 20px;
}
p {
    font-size: 1.5rem;
    max-width: 800px;
}

/* Button */
.btn {
    background: #ff4655;
    padding: 15px 30px;
    border-radius: 8px;
    text-decoration: none;
    color: white;
    font-weight: bold;
    transition: all 0.3s ease;
}
.btn:hover {
    background: #ff5e6b;
    transform: scale(1.05);
}

/* Image grid */
.image-grid {
    display: flex;
    justify-content: center;
    gap: 40px;
    margin-top: 40px;
    flex-wrap: wrap;
}
.image-item {
    text-align: center;
    max-width: 320px;
    animation: fadeInUp 1s ease forwards;
}
.image-item img {
    width: 320px;
    height: 260px;
    border-radius: 16px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.6);
    transition: all 0.5s ease;
    object-fit: cover;
}

.image-item img:hover {
    transform: scale(1.08) rotateX(6deg) rotateY(-6deg);
    box-shadow: 0 15px 35px rgba(255,70,85,0.7), 0 8px 25px rgba(0,0,0,0.6);
}
.image-item p {
    margin-top: 15px;
    font-size: 1.2rem;
    font-weight: 600;
    color: #fff;
}

/* Entry animation */
@keyframes fadeInUp {
    0% { opacity: 0; transform: translateY(60px); }
    100% { opacity: 1; transform: translateY(0); }
}

/* Cleanup Streamlit wrappers */
div[data-testid="stComponent"] {
    margin: 0 !important;
    padding: 0 !important;
    background: #784BBE !important;
    display: block !important;
}
div[data-testid="stComponent"] iframe {
    display: block !important;
    background: #784BBE !important;
    border: none !important;
    margin: 0 !important;
    padding: 0 !important;
}
div.element-container, div[data-testid="stVerticalBlock"] > div {
    background: #784BBE !important;
    margin: 0 !important;
    padding: 0 !important;
    border: none !important;
}
section.main, .block-container, .stApp {
    background: #784BBE !important;
}

/* Slight upward shift of the next section */
.section.bg-purple:nth-of-type(4) {
    margin-top: -200px !important;
}

/* Pulse animation */
@keyframes pulse {
  0% {text-shadow:0 0 10px #f0f, 0 0 20px #0ff;}
  50% {text-shadow:0 0 25px #0ff, 0 0 45px #f0f;}
  100% {text-shadow:0 0 10px #f0f, 0 0 20px #0ff;}
}
/* === Dynamic Particle Animation === */
.particle {
  position: absolute;
  width: 90px;
  height: 90px;
  object-fit: contain;
  opacity: 0.85;
  z-index: 0;
  pointer-events: none;
  animation: floatParticle var(--duration, 18s) ease-in-out infinite;
  animation-delay: var(--delay, 0s);
}

@keyframes floatParticle {
  0%   { transform: translate(0px, 0px) rotate(0deg); opacity: 0.8; }
  25%  { transform: translate(80px, -120px) rotate(15deg); opacity: 1; }
  50%  { transform: translate(-100px, 60px) rotate(-10deg); opacity: 0.9; }
  75%  { transform: translate(120px, 100px) rotate(12deg); opacity: 0.8; }
  100% { transform: translate(0px, 0px) rotate(0deg); opacity: 0.85; }
}

</style>
""", unsafe_allow_html=True)

# ---- HERO SECTION ----
st.markdown("""
<div class="section hero visible">
  <h1>🎯 Lock In. Aim True. Claim Victory.</h1>
  <p>Step into the world of Valorant — a tactical 5v5 shooter where precision, strategy, and teamwork decide your fate.</p>
  <a href="#" class="btn">Play Now</a>
</div>
""", unsafe_allow_html=True)

# ---- SECOND SECTION WITH PARTICLES ----
st.markdown("""
<div class="section bg-purple visible" 
     style="padding-top:40px; padding-bottom:20px; min-height:auto; margin-top:-5px;">

  <!-- Particle Layer -->
  <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa1.png" class="particle" style="top:15%; left:10%;">
  <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa2.png" class="particle" style="top:40%; left:70%;">
  <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa3.png" class="particle" style="top:65%; left:25%;">
  <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa4.png" class="particle" style="top:80%; left:80%;">
  <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa3.png" class="particle" style="top:65%; left:25%;">
  <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa4.png" class="particle" style="top:80%; left:80%;">
  <h1 style="margin-top:0; margin-bottom:6px;">Choose Your Agent</h1>
  <p style="margin-top:0; margin-bottom:10px;">
    From stealthy duelists to tactical controllers — every agent brings a unique playstyle to the battlefield.
    Master their abilities, lead your team to glory.
  </p>
</div>
""", unsafe_allow_html=True)

# ---- AGENT CAROUSEL (unchanged) ----
base = "https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main"
agents = [
    ("ag0.avif", "Agent 0 — Stealth Specialist"),
    ("ag1.avif", "Agent 1 — Tactical Genius"),
    ("ag2.avif", "Agent 2 — Duelist Supreme"),
    ("ag3.avif", "Agent 3 — Controller of Chaos"),
    ("ag4.avif", "Agent 4 — Recon Master"),
    ("ag5.avif", "Agent 5 — Swift Duelist"),
    ("ag6.avif", "Agent 6 — Defensive Wall"),
    ("ag7.avif", "Agent 7 — Precision Sniper"),
    ("ag8.avif", "Agent 8 — Smoke & Shadows"),
    ("ag9.avif", "Agent 9 — Firestorm"),
]

cards_html = ""
for img, caption in agents:
    img_url = f"{base}/{img}"
    cards_html += f"""
    <div class="card">
      <div class="card-inner">
        <div class="card-front">
          <img src="{img_url}" alt="{caption}">
        </div>
        <div class="card-back">
          <p style="padding:10px; font-size:1.05rem; font-weight:600; text-align:center;">{caption}</p>
        </div>
      </div>
    </div>
    """

carousel_html_start = """<!doctype html>
<html>
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap" rel="stylesheet">
<style>
:root { --bg: #784BBE; --btn-bg: rgba(0,0,0,0.6); --btn-hover: rgba(255,70,85,0.9); color: #fff; }
html,body { margin:0; padding:0; background: var(--bg); font-family: 'Poppins', sans-serif; color:#fff; }
.carousel-container {
  position: relative;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0;
  overflow: hidden;
}
.carousel-viewport { overflow: hidden; width: 100%; padding: 0; }
.carousel-track { display:flex; transition: transform 0.5s ease-in-out; align-items:center; will-change: transform; padding: 0; }
.card { flex:0 0 auto; width:280px; margin:0 20px; perspective:1000px; }
.card-inner { position:relative; width:100%; height:380px; transform-style:preserve-3d; transition:transform 0.8s; }
.card-front, .card-back { position:absolute; width:100%; height:100%; border-radius:12px; backface-visibility:hidden; overflow:hidden; }
.card-front img { width:100%; height:100%; object-fit:cover; border-radius:12px; display:block; }
.card-back { background:rgba(0,0,0,0.6); color:#fff; display:flex; align-items:center; justify-content:center; padding:10px; transform:rotateY(180deg); }
.card:hover .card-inner { transform:rotateY(180deg); }
.carousel-btn { position:absolute; top:50%; transform:translateY(-50%); background:var(--btn-bg); color:white; font-size:1.8rem; border:none; cursor:pointer; padding:8px 12px; border-radius:50%; z-index:5; user-select:none; }
.carousel-btn:hover { background:var(--btn-hover); }
.carousel-btn.prev { left:8px; }
.carousel-btn.next { right:8px; }
@media (max-width:900px){ .card{width:180px; height:260px;} }
</style>
</head>
<body>
<div class="carousel-container" id="carousel-root">
<button class="carousel-btn prev" id="prevBtn">&#10094;</button>
<div class="carousel-viewport">
<div class="carousel-track" id="track">
"""

carousel_html_end = """
</div>
</div>
<button class="carousel-btn next" id="nextBtn">&#10095;</button>
</div>
<script>
(function(){
const track=document.getElementById('track');
const nextBtn=document.getElementById('nextBtn');
const prevBtn=document.getElementById('prevBtn');
const visible=4;
const originalCards=Array.from(track.children);
const originalCount=originalCards.length;
for(let i=originalCount-visible;i<originalCount;i++){const c=originalCards[i].cloneNode(true);c.classList.add('clone');track.insertBefore(c,track.firstChild);}
for(let i=0;i<visible;i++){const c=originalCards[i].cloneNode(true);c.classList.add('clone');track.appendChild(c);}
const allCards=Array.from(track.children);
let index=visible;
function getCardFullWidth(){const c=allCards[0];const style=window.getComputedStyle(c);const m=parseFloat(style.marginLeft)+parseFloat(style.marginRight);return c.offsetWidth+m;}
let cardWidth=getCardFullWidth();
function setTrackPosition(a=true){track.style.transition=a?'transform 0.5s ease-in-out':'none';track.style.transform='translateX('+(-index*cardWidth)+'px)';if(!a){void track.offsetWidth;track.style.transition='transform 0.5s ease-in-out';}}
setTimeout(()=>setTrackPosition(false),20);
nextBtn.addEventListener('click',()=>{index++;setTrackPosition(true);if(index>=originalCount+visible){track.addEventListener('transitionend',()=>{index=visible;setTrackPosition(false);},{once:true});}});
prevBtn.addEventListener('click',()=>{index--;setTrackPosition(true);if(index<visible){track.addEventListener('transitionend',()=>{index=originalCount+visible-1;setTrackPosition(false);},{once:true});}});
window.addEventListener('resize',()=>{cardWidth=getCardFullWidth();setTrackPosition(false);});
})();
</script>
</body>
</html>
"""

carousel_html = carousel_html_start + cards_html + carousel_html_end
components.html(carousel_html, height=400, scrolling=False)

# ---- NEXT SECTIONS WITH PARTICLES ----
st.markdown("""
<div class="section bg-purple visible">

  <!-- Particle Layer -->
  <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa1.png" class="particle" style="top:10%; left:15%;">
  <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa2.png" class="particle" style="top:35%; left:75%;">
  <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa3.png" class="particle" style="top:70%; left:30%;">
  <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa4.png" class="particle" style="top:85%; left:80%;">
<img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa3.png" class="particle" style="top:65%; left:25%;">
  <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa4.png" class="particle" style="top:80%; left:80%;">
  <h1>Master the Battlefield</h1>
  <p>Each map is a new playground for strategy. Will you dominate the tight corners of Split, hold the open grounds of Breeze, or sneak through the alleys of Ascent?</p>

  <div class="image-grid">
    <div class="image-item"><img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/img1 (2).png"><p>Haven</p></div>
    <div class="image-item"><img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/img2.png"><p>Breeze</p></div>
    <div class="image-item"><img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/img4.png"><p>Abyss</p></div>
    <div class="image-item"><img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/img3.png"><p>Pearl</p></div>
    <div class="image-item"><img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/img5.png"><p>Icebox</p></div>
    <div class="image-item"><img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/img6.png"><p>Corrode</p></div>
  </div>
</div>
""", unsafe_allow_html=True)

# ---- JOIN SECTION WITH PARTICLES ----
st.markdown("""
<div style="display:flex; justify-content:space-between; align-items:center; background:#784BBE; padding:60px 100px 80px 100px; gap:60px; position:relative; overflow:hidden;">

  <!-- Particle Layer -->
  <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa1.png" class="particle" style="top:20%; left:15%;">
  <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa2.png" class="particle" style="top:50%; left:60%;">
  <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa3.png" class="particle" style="top:80%; left:25%;">
  <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa4.png" class="particle" style="top:85%; left:80%;">
<img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa3.png" class="particle" style="top:65%; left:25%;">
  <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa4.png" class="particle" style="top:80%; left:80%;">
  <!-- Left 2x2 Image Grid -->
  <div style="display:grid; grid-template-columns:repeat(2, 1fr); gap:30px; width:50%;">
    <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/tour.png" style="width:100%; height:230px; border-radius:16px; box-shadow:0 10px 25px rgba(0,0,0,0.7); object-fit:cover;">
    <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/commu.png" style="width:100%; height:230px; border-radius:16px; box-shadow:0 10px 25px rgba(0,0,0,0.7); object-fit:cover;">
    <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/achi.png" style="width:100%; height:230px; border-radius:16px; box-shadow:0 10px 25px rgba(0,0,0,0.7); object-fit:cover;">
    <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/skill.png" style="width:100%; height:230px; border-radius:16px; box-shadow:0 10px 25px rgba(0,0,0,0.7); object-fit:cover;">
  </div>

  <!-- Right Text Section -->
  <div style="width:45%; padding-left:40px; transform:translateY(25px);">
    <h1 style="margin-bottom:15px; font-size:2.8rem;">Step into the Valorant Universe</h1>
    <p style="font-size:1.4rem; max-width:600px;">
      Valorant is more than a game — it’s a <b>global phenomenon</b>. From casual matches with friends to world-class esports tournaments, there’s always a place for you.
    </p>
    <a href="#" class="btn" style="margin-top:25px;">Join the Action</a>
  </div>
</div>

<!-- IMAGE SECTION -->
<div style="width:100vw; display:flex; justify-content:flex-end; align-items:center; background:#784BBE; padding:0 0 20px 0; margin-top:-40px; position:relative; overflow:visible;">

  <!-- Particle Layer -->
  <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa1.png" class="particle" style="top:10%; left:20%;">
  <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa2.png" class="particle" style="top:50%; left:70%;">
  <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa3.png" class="particle" style="top:75%; left:25%;">
  <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa4.png" class="particle" style="top:85%; left:80%;">
<img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa3.png" class="particle" style="top:65%; left:25%;">
  <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/pa4.png" class="particle" style="top:80%; left:80%;">
  <!-- FIXED: Image above background -->
  <div style="width:58%; border-radius:16px; transform:translate(-40px, 80px); z-index:2; position:relative;">
    <img src="https://raw.githubusercontent.com/sheri1820/valorant-scroll-site/main/Airbrush-Image-Enhancer-1759649222767-removebg-preview.png" 
         style="width:100%; height:auto; object-fit:contain; display:block; border-radius:16px;"/>
  </div>
</div>

<!-- TEXT SECTION -->
<div style="
    position: relative; 
    top: -200px; 
    left: 150px;
    text-align: left; 
    width: fit-content;
">
  <h2 style="
      color:#fff; 
      font-size:2.6rem; 
      line-height:1.4; 
      text-shadow:0 0 10px #f0f, 0 0 20px #0ff; 
      animation:pulse 2s infinite;
      font-weight:700;
      margin:0;
  ">
    Join the Agents.<br>
    Choose your side.<br>
    Make your mark.
  </h2>
</div>

""", unsafe_allow_html=True)
