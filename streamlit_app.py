import streamlit as st
from datetime import datetime

# Titre de la page
st.set_page_config(page_title="Projet Web", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Accédez aux sections :", ["Accueil", "Présentation du Projet", "Liens", "Téléchargements"])

# Accueil
if menu == "Accueil":
    st.title("Bienvenue sur le site du projet !")
    st.markdown(
        """
        Ce site vous permettra de découvrir notre projet, d'accéder à des ressources utiles, 
        et de télécharger les documents associés. Utilisez le menu à gauche pour naviguer entre les sections.
        """
    )

# Présentation du Projet
elif menu == "Présentation du Projet":
    st.title("Présentation du Projet")

    # Historique
    st.header("Historique")
    st.markdown(
        """
        Le projet a débuté en [année de début]. Initialement, notre objectif était de [objectif initial].
        Voici un aperçu de l'évolution du projet :
        """
    )

    # Chronologie
    st.header("Chronologie de Réalisation")
    timeline = {
        "Janvier 2023": "Début du projet",
        "Mars 2023": "Finalisation des spécifications",
        "Juillet 2023": "Phase de test",
        "Décembre 2023": "Lancement final",
    }
    for date, event in timeline.items():
        st.write(f"**{date}:** {event}")

    # Membres
    st.header("Membres")
    st.markdown(
        """
        Voici les membres de notre équipe :
        - **Alice** : Responsable du développement.
        - **Bob** : Chef de projet.
        - **Charlie** : Designer.
        """
    )

    # Problèmes rencontrés et solutions
    st.header("Problèmes et Solutions")
    st.markdown(
        """
        **Problèmes rencontrés** :
        - Délais imprévus.
        - Difficultés techniques.

        **Solutions envisagées** :
        - Réorganisation des priorités.
        - Assistance d'experts techniques.
        """
    )

# Liens
elif menu == "Liens":
    st.title("Liens Utiles")

    links = {
        "Site d'Alice": "https://site-alice.com",
        "Site de Bob": "https://site-bob.com",
        "Bibliothèque utilisée": "https://streamlit.io",
    }

    for name, url in links.items():
        st.markdown(f"- [{name}]({url})")

# Téléchargements
elif menu == "Téléchargements":
    st.title("Téléchargements")

    st.markdown("Téléchargez les fichiers associés au projet :")

    with open("rapport_complet.pdf", "rb") as file:
        st.download_button("Télécharger le rapport complet", file, "rapport_complet.pdf")

    with open("projet_complet.zip", "rb") as file:
        st.download_button("Télécharger le projet complet", file, "projet_complet.zip")

    with open("version_allegee.zip", "rb") as file:
        st.download_button("Télécharger la version allégée", file, "version_allegee.zip")
