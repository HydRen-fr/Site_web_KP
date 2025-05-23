import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Kangaroo Planet",
    page_icon="🦘",
    layout="wide"
)

# File paths
logo = "logo.jpg"
screenshot_1 = "gameplay.png"
screenshot_2 = "menu.png"

# Simple custom CSS styling
st.markdown("""
    <style>
        .title-container {
            background: linear-gradient(135deg, #3f87a6, #ebf8e1, #f69d3c);
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            color: #000000;
        }
        .title-container h1 {
            font-size: 48px;
            margin-bottom: 10px;
        }
        .title-container p {
            font-size: 18px;
        }
        .section-title {
            font-size: 30px;
            margin-top: 40px;
            color: #444;
        }
        .testimonial {
            font-style: italic;
            color: #555;
            margin-bottom: 10px;
        }
        .resource-link {
            font-size: 18px;
            padding: 5px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Logo + Introduction
col1, col2 = st.columns([2, 3])
with col1:
    st.image(logo, use_container_width=True)
with col2:
    st.markdown("""
        <div style='margin-top: 200px;' class='title-container'>
            <h1>🌍 Kangaroo Planet</h1>
            <h3>Piou piou piou</h3>
            <p><strong>Kangaroo Planet</strong> is an immersive action-survival-shooter game where you play as a kangaroo defending its planet from a human invasion. 
            Get ready to fight off fierce and nasty enemies!</p>
        </div>
    """, unsafe_allow_html=True)

# 📄 Download the game
st.markdown("<div class='section-title'>📄 Download the game and its manual</div>", unsafe_allow_html=True)
resources = [
    "🔗 [Game](https://drive.google.com/drive/folders/1MUrsS8FjkAjS2-CChNxKrlC-_n_yICsu?usp=sharing)",
    "🔗 [Manual](https://github.com/HydRen-fr/Kangaroo-Planet)",
]
for r in resources:
    st.markdown(r)

# Footer
st.markdown("<br><hr>", unsafe_allow_html=True)

# 🎮 A captivating game
st.markdown("<div class='section-title'>🎮 A captivating game</div>", unsafe_allow_html=True)
st.markdown("""
- 🦘 **Play as a kangaroo and SHOOT THEM ALL**
- 😌 **A game that's all about relaxation**
- 🎶 **Enjoy great music while eliminating the bad guys**
- 🔊 **Soundtrack: Veridis Quo**
""")

# 📸 Game Preview
st.markdown("<div class='section-title'>📸 Game Preview</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.image(screenshot_1, use_container_width=True, caption="Play as the greatest animal: the kangaroo")
with col2:
    st.image(screenshot_2, use_container_width=True, caption="Lots of different game modes")

# 🛠️ Tools used
st.markdown("<div class='section-title'>🛠️ Tools Used</div>", unsafe_allow_html=True)
st.markdown("""
- 🎨 **Blender**: for 3D modeling and animations.
- 🕹️ **Unity**: for gameplay, physics, and rendering.
""")

# 🚀 Behind the scenes
st.markdown("<div class='section-title'>🚀 Behind the Scenes</div>", unsafe_allow_html=True)
st.markdown("""
- 🧠 **Enemy AI**: dynamic and adaptive behaviors.
- 🧱 **Scripts**: wave management, weapons, scoring.
""")

# 💬 Player testimonials
st.markdown("<div class='section-title'>💬 What players say</div>", unsafe_allow_html=True)
testimonials = [
    "'An unforgettable experience, Kangaroo Planet is truly out of this world!' – Alex",
    "'Epic battles and incredible exploration!' – Mia",
    "'The most immersive game I’ve played this year!' – Lucas",
    "'Crazy stuff' – Lucas' dad",
]
for t in testimonials:
    st.markdown(f"<div class='testimonial'>⭐️⭐️⭐️⭐️⭐️ {t}</div>", unsafe_allow_html=True)

# 📄 Defense report
st.markdown("<div class='section-title'>📄 Download our final defense report</div>", unsafe_allow_html=True)
st.markdown("""
This report details the development process, technical decisions, and main features of **Kangaroo Planet**.
""")
with open("Final_defense_report.pdf", "rb") as file:
    st.download_button(
        label="📥 Download the report", 
        data=file, 
        file_name="Final_defense_report.pdf", 
        mime="application/pdf"
    )

# 📁 Resources used
st.markdown("<div class='section-title'>📁 Resources Used</div>", unsafe_allow_html=True)
resources = [
    "🔗 [Blender](https://www.blender.org/download/)",
    "🔗 [Unity](https://www.unity.com)",
    "🔗 Music: [Veridis Quo – Daft Punk](https://www.youtube.com/watch?v=TCd6PfxOy0Y)"
]
for r in resources:
    st.markdown(r)

# Footer
st.markdown("<br><hr>", unsafe_allow_html=True)

st.header("👥 **The Kangaroo Planet Team**")
st.markdown("""
- 🟩 **Eliott - The Energetic One**: A disciplined athlete who turned effort into mental strength. Switched from Windows to Linux in high school.
- 🟪 **Nicolas - The Inventor**: Minecraft lover and world creator. Experienced in moderating Discord servers.
- 🟥 **Hélios - The Coder**: Coding since 6th grade, specialized in web development. Handles the entire technical structure of the game.
- 🟧 **Tanguy - The Strategist**: Loves math and chess, explored AI programming to dominate the board.
""")

st.subheader("📧 **Team Contact Info**")
st.markdown("""
- Tanguy: [tanguy.de-jerphanion@epita.fr](mailto:tanguy.de-jerphanion@epita.fr)
- Hélios: [helios.bringuet@epita.fr](mailto:helios.bringuet@epita.fr)
- Eliott: [eliott.caquelot@epita.fr](mailto:eliott.caquelot@epita.fr)
- Nicolas: [nicolas.delisle@epita.fr](mailto:nicolas.delisle@epita.fr)
""")
st.write("---")

st.markdown("<center>© 2025 Kangaroo Planet Team. All rights reserved.</center>", unsafe_allow_html=True)
