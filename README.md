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

