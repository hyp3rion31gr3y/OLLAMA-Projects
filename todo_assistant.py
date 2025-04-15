# todo_assistant.py

from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

llm = OllamaLLM(model="phi")  # You can change to "mistral", "llama2", etc.

template = """
You are a helpful assistant. Convert the following sentence into a bullet point to-do list:

"{task_input}"

Respond with just the list.
"""

prompt = PromptTemplate.from_template(template)
chain = prompt | llm  # New way to "chain" the prompt and model

def main():
    print("🤖 Welcome to your AI To-Do Assistant (modern LangChain style)!")
    while True:
        user_input = input("\n📝 Enter your task (or type 'exit'): ")
        if user_input.lower() in ['exit', 'quit']:
            print("👋 Bye!")
            break

        result = chain.invoke({"task_input": user_input})
        print("\n✅ Here's your To-Do List:")
        print(result)

if __name__ == "__main__":
    main()
