# 🧾 Invoice Extractor using Gemini API

This is a Streamlit-based web app that uses **Google's Gemini Vision API (gemini-1.5-flash)** to extract and understand key information from **invoice images** based on user queries.

---

## 🚀 Features

* Upload an invoice image (`.jpg`, `.jpeg`, `.png`, `.webp`)
* Ask natural language questions like:

  * *"What is the total amount?"*
  * *"Who is the vendor?"*
  * *"What is the due date?"*
* Get answers powered by Google's **Gemini multimodal model**
* Simple and interactive UI built with **Streamlit**

---

## 📦 Tech Stack

* **Python 3.10+**
* **Streamlit** – Web UI
* **Google Generative AI (Gemini)** – Vision + Text model
* **PIL (Pillow)** – Image processing
* **dotenv** – API key management

---

## 🛠️ Setup Instructions

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/invoice-extractor.git
   cd invoice-extractor
   ```

2. **Install dependencies**

   It's recommended to use a virtual environment.

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment variables**

   Create a `.env` file in the root directory:

   ```env
   GOOGLE_API_KEY=your_google_generative_ai_api_key
   ```

4. **Run the app**

   ```bash
   streamlit run app.py
   ```

---

## 🧠 How It Works

1. The user uploads an invoice image.
2. The app converts the image into a Gemini-compatible format.
3. A prompt and the user’s query are sent to the **Gemini 1.5 Flash** model.
4. Gemini processes the image + text query and returns a detailed response.

---




## 🙏 Acknowledgments

* Powered by [Google Generative AI (Gemini)](https://ai.google.dev/)
* UI built with [Streamlit](https://streamlit.io/)

---

