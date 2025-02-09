import os
import streamlit as st
from dotenv import load_dotenv
import time
import tempfile

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq  

load_dotenv()

def stream_data(text):
    for word in text.split():
        yield word + " "
        time.sleep(0.04)
models = {
    'Mixtral🌪️': 'mixtral-8x7b-32768',
    'Llama3🦙': 'llama3-70b-8192',
    'Gemma2 💎 ': 'gemma2-9b-it'
}

selected_model_name = st.selectbox("Choose your model", list(models.keys()))

Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Groq(
    model=models[selected_model_name], 
    api_key=os.getenv("GROQ_API_KEY"),
    request_timeout=360.0
)

tab_docs, tab_chat = st.tabs(["Documents", "Chat"])

with tab_docs:
    st.header("Document Section")
    st.write("Upload your documents here. Supported formats: PDF, TXT, DOCX.")
    
    uploaded_files = st.file_uploader("Upload documents", type=["pdf", "txt", "docx"], accept_multiple_files=True)
    
    if uploaded_files:
        with st.spinner("Uploading and processing documents..."):
            temp_dir = tempfile.TemporaryDirectory()
            for uploaded_file in uploaded_files:
                file_path = os.path.join(temp_dir.name, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
            
            documents = SimpleDirectoryReader(temp_dir.name).load_data()
            st.write(f"Loaded {len(documents)} document(s).")
            
            index = VectorStoreIndex.from_documents(documents)
            st.session_state.index = index
            st.success("Documents processed and index created!")
    else:
        st.info("Please upload some documents to create the index.")

with tab_chat:
    st.header("Chat Section")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("img.jpeg", width=300)
        st.markdown("<h2 style='text-align: center;'>Hi, I'm your Friendly Bot Techy 🤖</h2>", unsafe_allow_html=True)
    
    if "index" not in st.session_state:
        st.warning("No document index found. Please upload documents in the Documents tab first.")
    else:
        with st.chat_message("user"):
            user_query = st.chat_input("Hello! You can ask me anything:")
        
        if user_query:
            with st.spinner("Thinking ..."):
                query_engine = st.session_state.index.as_query_engine()
                result = query_engine.query(user_query)
                response = result.response
                st.markdown("### 🤖 Techy's Response:")
                st.write(stream_data(response))
