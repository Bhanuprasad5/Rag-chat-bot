import streamlit as st
from langchain_chroma import Chroma
import genai

# Initialize ChromaDB
db = Chroma(collection_name="vector_database", embedding_function=embeddings_model, persist_directory="./chroma_db_")

# Initialize GenAI
f = open(r"C:\Users\chouk\OneDrive\Desktop\keys\key.txt")
key = "google api"
genai.configure(api_key=key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def generate_response(query):
    docs_chroma = db.similarity_search_with_score(query, k=4)
    context_text = "\n\n".join([doc.page_content for doc, _score in docs_chroma])
    model.system_instruction = context_text
    response = model.generate_content(query)
    return response.text

# Streamlit App
st.title("Document Q&A")

user_query = st.text_input("Ask your question:")

if user_query:
    response = generate_response(user_query)
    st.write(response)
