import streamlit as st
import requests
import uuid

st.set_page_config(
    page_title="সহায়ক বাংলা শিক্ষক",
    page_icon="📚",
    layout="wide"
)

BASE_API_URL = "http://127.0.0.1:8000"
CHAT_URL = f"{BASE_API_URL}/chat"
MEMORY_URL = f"{BASE_API_URL}/memory"

# Session State Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []
if "user_id" not in st.session_state:
    st.session_state.user_id = "student_" + str(uuid.uuid4())
if "show_memory" not in st.session_state:
    st.session_state.show_memory = True

# Sidebar: Long-Term Memory Display
def display_memory_sidebar():
    """Displays long-term memory from backend."""
    st.sidebar.title("🧠 শিক্ষার্থীর স্মৃতি")
    st.sidebar.markdown(f"**User ID:** `{st.session_state.user_id}`")

    # Toggle to show/hide memory
    toggle = st.sidebar.checkbox("স্মৃতি দেখান", value=st.session_state.show_memory)
    st.session_state.show_memory = toggle

    if not toggle:
        st.sidebar.info("স্মৃতি গোপন রাখা হয়েছে।")
        return

    try:
        response = requests.get(f"{MEMORY_URL}/{st.session_state.user_id}", timeout=10)
        response.raise_for_status()
        memory_data = response.json().get("memory")

        if memory_data:
            st.sidebar.success("বর্তমান শিক্ষার্থীর প্রোফাইল:")
            st.sidebar.json(memory_data, expanded=False)
        else:
            st.sidebar.info("এখনও কোনো স্মৃতি তৈরি হয়নি। প্রশ্ন করুন এবং স্মৃতি তৈরি হতে দিন।")

    except requests.exceptions.RequestException as e:
        st.sidebar.error(f"স্মৃতি API-র সাথে সংযোগ ব্যর্থ হয়েছে।\n\n🔌 Error: {e}")

# --- Main UI Layout ---
st.title("📚 সহায়ক বাংলা শিক্ষক")
st.caption("🤖 আপনার ব্যক্তিগত শিক্ষক। প্রশ্ন করুন এবং AI উত্তর দেবে।")

st.markdown("""
<div style='padding: 10px; background-color: #f9f9f9; border-left: 5px solid #4CAF50; border-radius: 5px;'>
    এই চ্যাটবটটি আপনার পূর্ববর্তী কথোপকথন মনে রাখে এবং আপনার প্রোফাইল তৈরি করে। ডানপাশে সাইডবারে স্মৃতি দেখুন।
</div>
""", unsafe_allow_html=True)

# --- Display Sidebar Memory ---
display_memory_sidebar()

# --- Chat History Display ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Chat Input & API Call ---
if prompt := st.chat_input("আপনার প্রশ্নটি এখানে লিখুন..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("চিন্তা করছি..."):
            try:
                thread_id = "chat_session_" + str(uuid.uuid4())
                payload = {
                    "query": prompt,
                    "user_id": st.session_state.user_id,
                    "thread_id": thread_id
                }

                response = requests.post(CHAT_URL, json=payload, timeout=120)
                response.raise_for_status()

                bot_response = response.json().get("response", "দুঃখিত, একটি সমস্যা হয়েছে।")
                st.markdown(bot_response)

                st.session_state.messages.append({"role": "assistant", "content": bot_response})

                # Refresh sidebar memory
                st.rerun()

            except requests.exceptions.RequestException as e:
                st.error(f"❌ API-র সাথে সংযোগ করতে ব্যর্থ।\n\n🔌 Error: {e}")
