# agents/llm.py

# Make sure you installed langchain-ollama first:
# python3 -m pip install -U langchain-ollama

from langchain_ollama import ChatOllama

# Initialize your local Llama3 model
llm = ChatOllama(
    model="phi3",  # faster model available locally
    temperature=0.7,
    verbose=True
)
