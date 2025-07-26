# **Personalized Bengali Tutor – A RAG Agent with Long-Term Memory**  
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)  
![LangChain](https://img.shields.io/badge/LangChain-⚡-green.svg)  
![FastAPI](https://img.shields.io/badge/FastAPI-🚀-purple.svg)  
![Streamlit](https://img.shields.io/badge/Streamlit-🎈-orange.svg)  

## **📖 Overview**  
This project demonstrates the evolution of a **Retrieval-Augmented Generation (RAG)** chatbot into a **personalized intelligent tutor** named **“সহায়ক বাংলা শিক্ষক”** (Helpful Bengali Tutor). The system answers questions based on **Bengali literature and English texts**, remembers user details across sessions, and provides a highly interactive learning experience.

Key innovation: It combines **RAG**, **long-term memory**, and **agentic decision-making** with a modern UI and scalable backend.

---

## **✨ Core Features**
- ✅ **Retrieval-Augmented Generation (RAG):** Uses a Pinecone vector database to retrieve context from Bengali and English texts, ensuring accurate and grounded answers.  
- ✅ **Agentic Workflow with LangGraph:** A **state machine** that evaluates retrieved information and dynamically decides the next step.  
- ✅ **Web Search Fallback:** If the knowledge base lacks the answer, it performs **autonomous web search** using **Serper API**.  
- ✅ **Persistent Long-Term Memory:** Stores **user-specific details** (name, class, interests) across sessions for a personalized experience.  
- ✅ **Interactive Web UI (Streamlit):** Includes a **real-time memory visualization sidebar** and an intuitive chat interface.  
- ✅ **Scalable API Backend (FastAPI):** Decoupled architecture for **independent scaling of frontend and backend**.  

---

## **📐 System Architecture**
```
+--------------+      +------------------+      +---------------------+
|  Streamlit   | <--> |   FastAPI API    | <--> |   LangGraph Agent    |
|   (UI)       |      |  (main.py)       |      |  (agent_graph.py)    |
+--------------+      +------------------+      +----------+----------+
                                                          |
                                           +--------------+--------------+
                                           |                             |
                                   [Is context relevant?]               |
                                           |                             |
                                     (Routing Node)                      |
                                           |                             |
                     +----------------------+----------------------+     
                     |                                             |
                  (Yes)                                         (No)
                     |                                             |
+-------------------+      +-------------------+      +-------------------+
| Pinecone          | <--> | Retrieve Node     |      | Web Search Node   |
| (Vector DB)       |      | (RAG Context)     |      | (Fallback)        |
+-------------------+      +-------------------+      +-------------------+
```

---

## **🛠️ Tech Stack**
- **Backend:** FastAPI  
- **Frontend:** Streamlit  
- **LLM Orchestration:** LangChain, LangGraph  
- **LLM Provider:** Groq (LLaMA 3)  
- **Vector DB:** Pinecone  
- **Embeddings:** Hugging Face `sentence-transformers/all-mpnet-base-v2`  
- **Web Search:** Serper API  

---

## **🚀 Setup & Installation**
### **1. Prerequisites**
- Python 3.9+  
- API Keys for:  
  - Groq  
  - Pinecone  
  - Hugging Face  
  - Serper  

---

### **2. Clone the Repository**
```bash
git clone https://github.com/myself-nahid/bengali-tutor-chatbot.git
cd bengali-tutor-chatbot
```

---

### **3. Create Virtual Environment**
```bash
python -m venv venv
# Activate:
# macOS/Linux
source venv/bin/activate
# Windows
.venv\Scripts\activate
```

---

### **4. Install Dependencies**
```bash
pip install -U fastapi uvicorn[standard] streamlit requests langchain langgraph langchain-groq langchain-huggingface langchain-pinecone pinecone-client pydantic>=2.0 python-dotenv sentence-transformers langchain-community google-search-results wikipedia langchain-tavily
```

---

### **5. Configure Environment Variables**
Create a `.env` file in the project root:
```
# API Keys
GROQ_API_KEY="gsk_..."
HF_TOKEN="hf_..."
PINECONE_API_KEY="..."
SERPAPI_API_KEY="..."

# Optional (LangSmith tracing)
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_PROJECT="Personalized Bengali Tutor"

# Model & Index Config
LLAMA_MODEL="llama3-8b-8192"
PINECONE_INDEX_NAME="10ms-db-bangla-book"
EMBEDDING_MODEL_NAME="sentence-transformers/all-mpnet-base-v2"
```

