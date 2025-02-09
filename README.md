# TechyDocsGPT

TechyDocsGPT is an AI-powered document indexing and retrieval system that enables users to upload documents and interact with them through an intelligent chatbot. The system utilizes Groq LLMs, HuggingFace embeddings, and Streamlit for an intuitive user experience.

## Features
- **Document Upload & Processing**: Supports PDF, TXT, and DOCX formats.
- **Vector-Based Indexing**: Uses `VectorStoreIndex` for efficient document search.
- **Multiple AI Models**: Choose from Mixtral, Llama3, and Gemma2 models.
- **Chatbot Interface**: Ask questions and receive AI-generated responses.
- **Streaming Responses**: Displays responses in real-time.

<p align="center">
  <img src="https://github.com/user-attachments/assets/966cb5d4-7e99-4fb7-b54f-b6d2acfb239e" width="45%"> 
  <img src="https://github.com/user-attachments/assets/c043c8e2-e74c-4519-b138-8c49e9732a0d" width="45%">
</p>

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Soumit2003/TechyDocsGPT.git
   cd TechyDocsGPT
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add your Groq API key:
     ```plaintext
     GROQ_API_KEY=your_api_key_here
     ```

## Usage
Run the Streamlit application:
```bash
streamlit run app.py
```

## Technologies Used
- **Python**
- **Streamlit**
- **LlamaIndex**
- **HuggingFace Embeddings**
- **Groq AI Models**
- **Tempfile for document handling**

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License
No official license has been applied to this project yet.

## Author
Developed by [Your Name](https://github.com/Soumit2003) 🚀

