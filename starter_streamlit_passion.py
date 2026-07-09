import streamlit as st

st.title("Ma passion : La découverte du monde")
st.header("Bienvenue sur mon app de voyage")
st.write("Cette page présente un de mes centres d'intérêt.")

# Menu déroulant principal
choix = st.selectbox(
    "Choisis une catégorie :",
    ["Pays", "Lieux à visiter", "Culture"]
)

# --- Contenu différent selon la catégorie ---

if choix == "Pays":
    pays = st.selectbox(
        "Quel pays t'intéresse ?",
        ["Japon", "Italie", "Maroc", "Brésil", "Islande"]
    )
    st.write(f"Tu as choisi : **{pays}**")
    note = st.slider(f"Ta note pour {pays}", 0, 10, 8)
    st.write(f"Ta note : {note}/10")
    if st.checkbox(f"Je recommande {pays}"):
        st.success(f"Merci de recommander {pays} ! 👍")

elif choix == "Lieux à visiter":
    lieu = st.selectbox(
        "Quel type de lieu préfères-tu ?",
        ["Plages", "Montagnes", "Villes historiques", "Parcs naturels"]
    )
    st.write(f"Tu préfères : **{lieu}**")
    commentaire = st.text_input("Décris ton lieu de rêve :")
    if commentaire:
        st.write(f"Ton lieu de rêve : {commentaire}")

elif choix == "Culture":
    culture = st.selectbox(
        "Qu'est-ce qui t'attire le plus ?",
        ["Gastronomie", "Musées", "Traditions", "Langues"]
    )
    st.write(f"Tu as choisi : **{culture}**")
    nb = st.slider("Combien de pays as-tu visités ?", 0, 50, 5)
    st.write(f"Tu as visité {nb} pays !")

# Bouton final (commun à toutes les catégories)
if st.button("Valider"):
    st.success("Bravo, ton app Streamlit tourne ! 🎉")
else:
    st.info("Clique sur le bouton pour valider.")

commentaire = st.text_input("Ton commentaire sur ce voyage :")
if commentaire:
    st.write(f"Tu as écrit : {commentaire}")
st.image("https://vivreenmalaisie.com/wp-content/uploads/2020/12/Kuala-Lumpur-Skyline.jpeg")