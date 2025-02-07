import streamlit as st
import requests

API_KEY = "Text Geration API_KEY "  # Bäst att lagra detta säkert i en .env-fil

st.title("Text Generation med Deepseek R1-7b")

# Välj funktion: Generera text eller ladda upp PDF
option = st.sidebar.selectbox("Välj åtgärd", ["Generera text", "Ladda upp PDF", "Återställ modell"])

if option == "Generera text":
    prompt = st.text_area("Ange prompt:")
    if st.button("Generera"):
        response = requests.post(
            "http://127.0.0.1:8000/generate_text",
            json={"prompt": prompt},
            params={"api_key": API_KEY}
        )
        if response.status_code == 200:
            st.write("Svar från modellen:")
            st.write(response.json().get("result"))
        else:
            st.error("Fel vid anrop: " + response.text)

elif option == "Ladda upp PDF":
    uploaded_file = st.file_uploader("Välj en PDF-fil", type="pdf")
    if uploaded_file is not None:
        files = {"file": uploaded_file}
        response = requests.post(
            "http://127.0.0.1:8000/upload_pdf",
            files=files,
            params={"api_key": API_KEY}
        )
        if response.status_code == 200:
            st.write("PDF-innehåll:")
            st.write(response.json().get("pdf_text"))
        else:
            st.error("Fel vid filuppladdning: " + response.text)

elif option == "Återställ modell":
    st.write("Här implementerar du logik för att rensa minnet eller återställa modellen.")
    # Du kan lägga till en API-endpoint i backend för att återställa modellen
