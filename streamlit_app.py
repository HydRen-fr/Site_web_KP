import streamlit as st

# Titre du site
st.title("Kangaroo Planet - Projet de Jeu Vidéo")

# Page d'accueil
st.header("Bienvenue sur le site du projet Kangaroo Planet")
st.write("""
Ce site est dédié au projet **Kangaroo Planet**, un jeu vidéo développé dans le cadre de notre cursus à l’EPITA. Vous y trouverez toutes les informations relatives à l’historique du projet, les membres de l’équipe, les étapes de réalisation, ainsi que les ressources utilisées.
""")

# Section de présentation du projet
st.header("Présentation du Projet")
st.subheader("Historique et Objectifs")
st.write("""
**Kangaroo Planet** est un jeu de tir à la troisième personne, dans lequel un kangourou défend sa planète contre des envahisseurs. Ce jeu a été développé à l'aide du moteur **Unity** et du langage **C#**. Nous avons mis l'accent sur des mécaniques de gameplay dynamiques et des éléments de génération procédurale pour offrir une expérience unique à chaque joueur.

L'objectif principal était d'apprendre à créer des jeux vidéo, d'expérimenter avec la génération procédurale des niveaux et d'améliorer nos compétences en travail d'équipe et en développement logiciel.
""")

st.subheader("Équipe")
st.write("""
L'équipe du projet Kangaroo Planet est composée de quatre étudiants :

- **Membre 1** : Responsable du développement C# et de la logique du jeu.
- **Membre 2** : Responsable des aspects visuels et de l'intégration Unity.
- **Membre 3** : Responsable de la génération procédurale des niveaux.
- **Membre 4** : Responsable de l'intégration des éléments narratifs et des sons.

Les rôles étaient attribués en fonction des compétences et de l'expertise de chaque membre dans les domaines spécifiques.
""")

st.subheader("Chronologie de réalisation")
st.write("""
Le projet a été réalisé sur plusieurs mois avec une répartition en différentes phases :

1. **Phase de conception** (1 mois) : Définition des mécaniques du jeu, de l'histoire et des ressources nécessaires.
2. **Phase de développement initial** (2 mois) : Développement des premières fonctionnalités de base, comme les contrôles du joueur et la génération procédurale.
3. **Phase de tests et amélioration** (1 mois) : Tests des fonctionnalités, correction des bugs et ajout des fonctionnalités supplémentaires.
4. **Phase de finalisation** (1 mois) : Préparation de la soutenance et documentation du projet.

Nous avons également rencontré plusieurs défis techniques, notamment liés à la génération procédurale des niveaux, ce qui a nécessité de nombreuses itérations pour obtenir des résultats satisfaisants.
""")

st.subheader("Problèmes rencontrés et solutions")
st.write("""
Lors du développement de **Kangaroo Planet**, nous avons rencontré plusieurs défis techniques :

- **Problème de génération procédurale** : Les algorithmes de génération de niveaux initialement implémentés étaient trop simples et produisaient des résultats peu intéressants. Nous avons résolu cela en optimisant l'algorithme pour ajouter de la variété dans les niveaux et rendre le jeu plus dynamique.
- **Optimisation des performances** : Le jeu souffrait de ralentissements lors de la création de nouveaux niveaux. Nous avons mis en place des solutions de gestion des ressources et d'optimisation des objets générés pour améliorer la fluidité.
""")

# Section des ressources et liens
st.header("Ressources et Liens")
st.subheader("Liens des membres de l'équipe")
st.write("""
- **Membre 1** : [Lien vers profil GitHub](https://github.com/membre1)
- **Membre 2** : [Lien vers profil GitHub](https://github.com/membre2)
- **Membre 3** : [Lien vers profil GitHub](https://github.com/membre3)
- **Membre 4** : [Lien vers profil GitHub](https://github.com/membre4)
""")

st.subheader("Logiciels et Bibliothèques utilisées")
st.write("""
- **Unity** : Moteur de jeu utilisé pour le développement du projet.
- **C#** : Langage de programmation utilisé pour la logique du jeu.
- **Blender** : Utilisé pour la création des modèles 3D.
- **Audacity** : Utilisé pour le montage des effets sonores et de la musique.

Tous les assets, images et sons utilisés sont libres de droits ou créés spécifiquement pour ce projet.
""")

# Section de téléchargement
st.header("Téléchargement du projet")
st.write("""
Vous pouvez télécharger les fichiers relatifs à ce projet ci-dessous. Cela inclut le rapport final, le projet complet, ainsi qu'une version allégée sans les éléments non nécessaires à l'exécution du jeu.
""")

# Téléchargement des fichiers
st.subheader("Téléchargement du Rapport et du Projet")
st.download_button(
    label="Télécharger le Rapport Complet",
    data=open('rapport_complet.pdf', 'rb').read(),
    file_name='rapport_complet.pdf',
    mime='application/pdf'
)

st.download_button(
    label="Télécharger le Projet Complet",
    data=open('projet_complet.zip', 'rb').read(),
    file_name='projet_complet.zip',
    mime='application/zip'
)

st.download_button(
    label="Télécharger la Version Allégée",
    data=open('projet_allege.zip', 'rb').read(),
    file_name='projet_allege.zip',
    mime='application/zip'
)

# Footer
st.markdown("""
---
**Kangaroo Planet** | Projet EPITA - 2025 | Développement avec Unity et C#
""")
