import os

import streamlit as st
from genai import GenerativeModel
from langchain_chroma import Chroma

# App Title
st.title("AI-Powered Chatbot with ChromaDB and Google GenAI")

# Initialize ChromaDB
def initialize_chroma_db():
    embeddings_model = None  # Replace with your actual embedding model
    return Chroma(collection_name="vector_database", 
                  embedding_function=embeddings_model, 
                  persist_directory=r"C:\Users\chouk\backup\Gen AI Langchain\chroma_db_")

# Query the database
def query_chroma_db(db, user_query, k=4):
    docs_chroma = db.similarity_search_with_score(user_query, k=k)
    context_text = "\n\n".join([doc.page_content for doc, _score in docs_chroma])
    return context_text

# Generate response using GenAI
def generate_response(context_text, query):
    key_path = r"C:\Users\chouk\OneDrive\Desktop\keys\key.txt"  # Update with your key file path
    with open(key_path, 'r') as f:
        api_key = f.read().strip()
    genai.configure(api_key=api_key)
    model = GenerativeModel(model_name="gemini-1.5-flash", system_instruction=context_text)
    response = model.generate_content(query)
    return response.text

# Streamlit UI
st.sidebar.header("Chatbot Settings")
user_query = st.text_input("Enter your query:", placeholder="Ask a question...")
submit_button = st.button("Get Answer")

if submit_button and user_query:
    try:
        st.write("Fetching data from ChromaDB...")
        db = initialize_chroma_db()
        context = query_chroma_db(db, user_query)
        st.write("Context retrieved successfully!")
        
        st.write("Generating response using GenAI...")
        response = generate_response(context, user_query)
        st.success("Response:")
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")
