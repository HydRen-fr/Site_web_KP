import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Kangaroo Planet",
    page_icon="🦘",
    layout="wide"
)

logo = "logo.jpg"
screenshot_1 = "kang.png"
screenshot_2 = "lune.png"

# Titre principal et introduction
col1, col2 = st.columns([2, 3])
with col1:
    st.image(logo, use_column_width=True)
with col2:
    st.title("🌍 **Kangaroo Planet**")
    st.subheader("Piou piou piou")
    st.write("""
    **Kangaroo Planet** est un jeu d'action-survie-shooter immersif où vous incarnez un kangourou défendant sa planète d'une invasion humaine. 
    Préparez-vous à combattre des ennemis redoutables et méchants !
    """)

# Section : Un jeu captivant
st.header("🎮 **Un jeu captivant**")
st.markdown("""
- **Incarnez un kangourou et SHOOTEZ-LES TOUS**
- **Un jeu qui détend avant tout**
- **Profitez d'une bonne musique en fond tout en exterminant les bad guys**
""")

# Section : Captures d'écran
st.header("📸 **Aperçu du jeu**")
col1, col2 = st.columns(2)
with col1:
    st.image(screenshot_1, use_column_width=True, caption="Incarnez le meilleur des animaux : un kangourou")
with col2:
    st.image(screenshot_2, use_column_width=True, caption="Un univers magnifique et rigolo")

# Section : Développement
st.header("🚀 **Coulisses du développement**")
st.write("""
L'équipe derrière **Kangaroo Planet** a travaillé d'arrache-pied pour offrir une expérience de jeu fluide et captivante. Voici quelques faits marquants :
- **Scripts principaux :** Gestion des ennemis, armes, et spawn dynamique, optimisés pour une performance maximale.
- **Intelligence artificielle :** Un système de comportement complexe permettant aux ennemis de s'adapter aux actions du joueur.
- **Graphismes :** Univers visuel unique, inspiré des paysages extraterrestres et de l'Australie sauvage.
""")

# Section : Témoignages
st.header("💬 **Ce que disent les joueurs**")
testimonials = [
    "⭐️⭐️⭐️⭐️⭐️ 'Une expérience inoubliable, Kangaroo Planet est vraiment hors du commun !' - Alex",
    "⭐️⭐️⭐️⭐️ 'Des combats épiques et une exploration incroyable !' - Mia",
    "⭐️⭐️⭐️⭐️⭐️ 'Le jeu le plus immersif que j'ai joué cette année !' - Lucas"
    "⭐️⭐️⭐️⭐️⭐️ 'Un jeu crée par des goats pour les goats...' - Le grand-frère de Lucas"
]
for testimonial in testimonials:
    st.markdown(f"> {testimonial}")

# Section : Contact et liens
st.write("Nous n'avons pas de réseaux car nous sommes mystérieux mais nous sommes des élèves de la promo 2029 de l'EPITA !")

st.write("---")
st.markdown("© 2025 Kangaroo Planet Team. Tous droits réservés.")
