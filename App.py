import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Anti-Rappel", page_icon="🧠")

st.title("🧠 Anti-Rappel – Assistant de vie intelligent")

st.markdown("Cette application vous aide à ne rien oublier dans votre quotidien. Choisissez vos rappels essentiels :")

# Choix du profil utilisateur
profil = st.selectbox("Quel est votre profil ?", [
    "Parent",
    "Étudiant",
    "Jeune actif",
    "Auto-entrepreneur",
    "Célibataire",
    "Couple",
    "Sénior",
    "Autre"
])

# Rappels proposés
st.subheader("📌 Sélectionnez vos rappels")
choix = st.multiselect(
    "Que souhaitez-vous que l'application vous rappelle ?",
    [
        "Contrôle technique voiture",
        "Paiement loyer",
        "CAF : actualisation trimestrielle",
        "Renouvellement pièce d'identité",
        "Vaccins et rendez-vous médicaux",
        "Anniversaires",
        "Rendez-vous administratifs",
        "Dates d’examens ou concours",
        "Changement de mutuelle / banque",
        "Inscription Pôle emploi ou renouvellement",
        "Date limite impôts ou URSSAF"
    ]
)

# Planification
st.subheader("🕓 Planifier un rappel précis")
libelle = st.text_input("Nom du rappel")
date_rappel = st.date_input("Date souhaitée", min_value=datetime.today())
heure = st.time_input("Heure du rappel", value=datetime.now().time())

# Confirmation
if st.button("✅ Ajouter le rappel"):
    if libelle:
        rappel_str = f"📅 Rappel « {libelle} » programmé pour le {date_rappel.strftime('%d/%m/%Y')} à {heure.strftime('%Hh%M')}"
        st.success(rappel_str)
    else:
        st.error("Veuillez donner un nom à votre rappel")

# Résumé
if choix:
    st.info("🧾 Rappels sélectionnés :")
    for c in choix:
        st.write(f"🔔 {c}")
