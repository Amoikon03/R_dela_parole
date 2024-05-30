import streamlit as st
import speech_recognition as sr
import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

# Étape 2 : Charger et prétraiter les données pour le chatbot
pairs = [
    [
        r"mon nom est (.*)",
        ["Bonjour %1, comment allez-vous aujourd'hui ?", "Enchanté de vous rencontrer, %1. Comment puis-je vous aider aujourd'hui ?",]
    ],
    [
        r"quel est ton nom ?",
        ["Mon nom est Chatbot.", "Je suis appelé Chatbot.",]
    ],
    [
        r"comment ça va ?",
        ["Je vais bien, merci. Et vous ?", "Tout va bien, merci. Comment vous sentez-vous ?",]
    ],
    [
        r"désolé (.*)",
        ["Ce n'est pas grave", "Ce n'est pas grave, ne vous inquiétez pas", "Pas de souci, tout va bien",]
    ],
    [
        r"je vais bien",
        ["Content de l'entendre", "Ravi de savoir que vous allez bien", "C'est super! Comment puis-je vous aider ?",]
    ],
    [
        r"salut|bonjour|coucou",
        ["Bonjour", "Salut", "Coucou, comment puis-je vous aider aujourd'hui ?",]
    ],
    [
        r"au revoir|quit",
        ["Au revoir pour l'instant. À bientôt :)", "C'était agréable de parler avec vous. À bientôt :)", "Prenez soin de vous, à la prochaine fois !"]
    ],
    [
        r"quelle heure est-il ?",
        ["Je suis désolé, je ne peux pas donner l'heure exacte. Veuillez vérifier votre appareil.", "Malheureusement, je ne peux pas indiquer l'heure. Regardez votre montre ou téléphone pour l'heure actuelle."]
    ],
    [
        r"parle-moi de toi",
        ["Je suis un chatbot créé pour vous aider avec diverses questions.", "Je suis un assistant virtuel conçu pour interagir avec vous et répondre à vos questions.", "Je suis un programme informatique conçu pour simuler une conversation avec des utilisateurs humains."]
    ],
    [
        r"qui t'a créé ?",
        ["Je suis créé par une équipe de développeurs passionnés.", "Des développeurs talentueux m'ont conçu pour vous aider.", "Je suis le produit de l'innovation et de la programmation."]
    ],
    [
        r"peux-tu m'aider avec (.*) ?",
        ["Je vais faire de mon mieux pour vous aider avec %1.", "Dites-m'en plus sur %1 et je verrai comment je peux aider.", "Je suis là pour ça, parlons de %1."]
    ],
    [
        r"qu'est-ce que tu sais faire ?",
        ["Je peux discuter avec vous, répondre à des questions simples, et vous aider avec des informations de base.", "Mon but est de vous aider avec vos questions et de rendre votre journée plus facile.", "Je suis conçu pour converser avec vous et fournir des informations utiles."]
    ]
]

chatbot = Chat(pairs, reflections)

# Étape 3 : Définir une fonction pour transcrire la parole en texte

def transcribe_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Parlez maintenant...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='fr-FR')
            return text
        except sr.UnknownValueError:
            st.error("Désolé, je n'ai pas compris.")
        except sr.RequestError as e:
            st.error(f"Erreur du service de reconnaissance vocale : {e}")
        return ""

# Étape 4 : Modifier la fonction chatbot

def get_chatbot_response(input_text):
    response = chatbot.respond(input_text)
    return response

# Étape 5 : Créer une application Streamlit

def main():
    st.title("Chatbot avec reconnaissance vocale")
    st.write("Entrez un texte ou utilisez le microphone pour parler avec le chatbot.")

    input_method = st.radio("Choisissez le mode d'entrée :", ('Texte', 'Voix'))

    user_input = ""
    if input_method == 'Texte':
        user_input = st.text_input("Vous : ", "")
    elif input_method == 'Voix':
        if st.button("Démarrer l'enregistrement"):
            user_input = transcribe_speech()
            st.write("Vous (transcrit) : ", user_input)

    if user_input:
        response = get_chatbot_response(user_input)
        st.write("Chatbot : ", response)


if __name__ == "__main__":
    main()

# Lien vers l'autre page ou section
st.subheader("Accéder à la page Acceuil")

# Liste de lien
st.write("""

- [Acceuil](http://localhost:8501/Chatbot)

""")
