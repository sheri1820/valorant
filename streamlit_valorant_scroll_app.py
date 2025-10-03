import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Valorant Scroll Site",
    layout="wide"
)

# ---- CUSTOM CSS ----
st.markdown("""
<style>
/* Reset body and hide default Streamlit stuff */
body {
    margin: 0;
    font-family: 'Poppins', sans-serif;
    background: #000;
    color: white;
}

/* Section styling */
.section {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 50px;
    opacity: 0;
    transform: translateY(50px);
    transition: all 1s ease-out;
}

.section.visible {
    opacity: 1;
    transform: translateY(0);
}

/* Hero section (BG1 image) */
.hero {
    background: url("https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltf22f52c61c621c25/5f4d91b68da9f30f70f3d5cf/VALORANT_2020_EP1_KeyArt.jpg") no-repeat center center;
    background-size: cover;
    height: 100vh;
    color: white;
    text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
}

/* Gradient background for other sections */
.bg-purple {
    background: #784BBE;
}

/* Headline + Sub */
h1 {
    font-size: 4rem;
    margin-bottom: 20px;
}

p {
    font-size: 1.5rem;
    max-width: 800px;
}

/* CTA button */
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
</style>
""", unsafe_allow_html=True)

# ---- CUSTOM JS (Intersection Observer for fade-in) ----
st.markdown("""
<script>
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add("visible");
    }
  });
});
document.querySelectorAll('.section').forEach((sec) => {
  observer.observe(sec);
});
</script>
""", unsafe_allow_html=True)

# ---- WEBSITE CONTENT ----
st.markdown("""
<div class="section hero">
    <h1>🎯 Lock In. Aim True. Claim Victory.</h1>
    <p>Step into the world of Valorant — a tactical 5v5 shooter where precision, strategy, and teamwork decide your fate.</p>
    <a href="#" class="btn">Play Now</a>
</div>

<div class="section bg-purple">
    <h1>What is Valorant?</h1>
    <p>Valorant is not just another FPS — it’s a game of <b>skill and creativity</b>. With unique agents, mind-bending abilities, and razor-sharp gunplay, every round is a story waiting to unfold.</p>
</div>

<div class="section bg-purple">
    <h1>Choose Your Agent</h1>
    <p>From stealthy duelists to tactical controllers — every agent brings a unique playstyle to the battlefield. Master their abilities, lead your team to glory.</p>
    <a href="#" class="btn">Meet the Agents</a>
</div>

<div class="section bg-purple">
    <h1>Master the Battlefield</h1>
    <p>Each map is a new playground for strategy. Will you dominate the tight corners of Split, hold the open grounds of Breeze, or sneak through the alleys of Ascent?</p>
</div>

<div class="section bg-purple">
    <h1>Join the Valorant Universe</h1>
    <p>Valorant is more than a game — it’s a <b>global phenomenon</b>. From casual matches with friends to world-class esports tournaments, there’s always a place for you.</p>
    <a href="#" class="btn">Watch Tournaments</a>
</div>
""", unsafe_allow_html=True)

