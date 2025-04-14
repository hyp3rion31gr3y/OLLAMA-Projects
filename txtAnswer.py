import streamlit as st
import ollama

def read_txt_file(file):
    return file.read().decode("utf-8")

def ask_question_with_ollama(context, question, model="mistral"):
    full_prompt = (
        f"Use the following content to answer the question:\n\n"
        f"{context}\n\n"
        f"Question: {question}"
    )
    response = ollama.chat(model=model, messages=[{"role": "user", "content": full_prompt}])
    return response["message"]["content"]

# Streamlit UI
st.set_page_config(page_title="Ask Your Text File!", layout="centered")
st.title("📄🧠 Ask Questions from Your Text File")

uploaded_file = st.file_uploader("Upload a `.txt` file", type=["txt"])

if uploaded_file:
    txt_content = read_txt_file(uploaded_file)
    st.success("✅ Text file loaded. Ask your questions below!")

    user_question = st.text_input("❓ Ask a question about the file:")
    if user_question:
        with st.spinner("Thinking..."):
            answer = ask_question_with_ollama(txt_content, user_question)
        st.markdown("### 🧾 Answer:")
        st.write(answer)
