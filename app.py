from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Process user prompt + image and return Gemini output
def get_gemini_response(input_text, image_parts, prompt):
    response = model.generate_content([input_text, image_parts[0], prompt])
    return response.text

# Process uploaded image into Gemini-compatible format
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data,
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit UI
st.set_page_config(page_title="Invoice Extracter", page_icon=":money_with_wings:", layout="wide")
st.header("Invoice Extracter :money_with_wings:")

input_query = st.text_input("Enter your query", placeholder="What is the total amount?", key="input")
uploaded_file = st.file_uploader("Upload an image of the invoice", type=["jpg", "jpeg", "png", "webp"], key="image")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice", use_column_width=True)

submit = st.button("Tell me about the invoice")

input_prompt = """
You are an expert in understanding invoices. You will be provided with an invoice image and a user query. Your task is to analyze the image and answer the question as accurately as possible.
"""

if submit:
    if uploaded_file is not None:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_prompt, image_data, input_query)
        st.write("🧠 Response from Gemini:")
        st.write(response)
    else:
        st.error("❗ Please upload an invoice image before submitting your query.")