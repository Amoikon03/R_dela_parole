import streamlit as st

# Titre et description de l'application avec options de style
st.sidebar.title("Options de Style")

# Options de style pour le titre
title_text_size = st.sidebar.slider("Taille du texte", 40, 100, 40)
title_text_color = st.sidebar.color_picker("Couleur du texte", "#FFFFFF")
title_bg_color = st.sidebar.color_picker("Couleur de fond du texte", "#0C0F0A")

# Options de style pour la description
desc_text_size = st.sidebar.slider("Taille du texte de la description", 12, 30, 16)
desc_text_color = st.sidebar.color_picker("Couleur du texte de la description", "#FFFFFF")
desc_bg_color = st.sidebar.color_picker("Couleur de fond de la description", "#0C0F0A")

# Options de style pour la légende de l'image
caption_text_color = st.sidebar.color_picker("Couleur du texte de la légende", "#232826")

# Titre de l'application
title_style = f"""
<div style="background-color: {title_bg_color}; padding: 10px; border-radius: 5px; text-align: center;">
<h1 style="color: {title_text_color}; font-size: {title_text_size}px;">Améliorer l'application de reconnaissance du discours</h1>
</div>
"""
st.markdown(title_style, unsafe_allow_html=True)

st.write(" ")
st.write(" ")

# Description de l'application
description = """
**Il s'agit d'améliorer une application de reconnaissance de la parole en ajoutant de nouvelles fonctionnalités pour augmenter sa fonctionnalité. Cela signifie probablement que l'application de base existe déjà et qu'elle est capable de convertir la parole en texte, mais qu'il y a des opportunités pour la rendre plus robuste, utile et conviviale.**
"""

desc_style = f"""
<div style="background-color: {desc_bg_color}; color: {desc_text_color}; padding: 10px; border-radius: 5px; font-size: {desc_text_size}px; text-align: justify;">
{description}
</div>
"""

# Utilisation des colonnes de Streamlit pour organiser le texte et l'image côte à côte
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(desc_style, unsafe_allow_html=True)

with col2:
    st.image("images.jpg", use_column_width=True)
    st.markdown(f"<div style='color: {caption_text_color}; font-weight: bold; text-align: center;'>Interaction Homme-Robot</div>", unsafe_allow_html=True)

# Lien vers l'autre page ou section
st.subheader("Accéder à la page Chatbot")

# Liste de lien
st.write("""

- [Chatbot](http://localhost:8502/)

""")

