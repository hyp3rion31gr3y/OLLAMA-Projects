"""
To install streamlit: pip install streamlit
To install OLLAMA: curl -fsSL https://ollama.com/install.sh | sh
model required: mistral (ollama run mistral)

HOW TO RUN:
streamlit run word-dictionary.py
"""

import streamlit as st
import requests

OLLAMA_URL = "http://3.109.155.162:11434/api/generate"  # Replace with your actual Streamlit app URL
MODEL_NAME = "mistral"

def query_ollama(word):
    prompt = (
        f"Give the dictionary entry for the word: {word}.\n\n"
        "Definition: Write one short sentence in simple English (max 30 words).\n"
        "Example Sentence: Use the word in a natural sentence.\n\n"
        "Only return the definition and example in that format. No explanations, tags, or extra text."
    )

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.2, "num_predict": 100},
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        if response.status_code == 200:  # Check that the response is successful
            data = response.json()
            if 'error' in data.keys():  # Check for error messages
                return data['error']
            else:
                return data.get("response", "No response received.")
        else:
            return f"⚠️ Error querying model: {response.reason}"
    except Exception as e:
        return f"⚠️ Error querying model: {e}"



# Streamlit UI
st.set_page_config(page_title="LLM Dictionary", page_icon="📚")
st.title("📚 LLM-Powered Dictionary")
st.write("Enter a word to get its meaning and an example sentence.")

word = st.text_input("Word").strip()

if st.button("Get Meaning"):
    if word:
        st.info("Querying the local model...")
        result = query_ollama(word.lower())
        st.markdown("### 📘 Definition and Example")
        st.code(result.strip(), language="markdown")

    else:
        st.warning("Please enter a word.")
