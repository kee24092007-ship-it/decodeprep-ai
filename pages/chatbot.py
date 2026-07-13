import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Decode Labs AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# ==========================================
# LOAD ENV
# ==========================================

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("Google API Key not found!")
    st.stop()

client = genai.Client(api_key=API_KEY)

# ==========================================
# LOGIN CHECK
# ==========================================

if "user" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

# ==========================================
# LOAD KNOWLEDGE BASE
# ==========================================

KNOWLEDGE_FILE = "decode_knowledge_base.txt"

@st.cache_data
def load_knowledge():
    with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as file:
        return file.read()

knowledge = load_knowledge()

# ==========================================
# CSS
# ==========================================

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0F172A,#111827,#1E293B);
}

.title{
font-size:42px;
font-weight:bold;
color:#FFD700;
}

.subtitle{
font-size:18px;
color:#D1D5DB;
margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

st.markdown(
    '<div class="title">🤖 Decode Labs AI Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    Welcome! 👋<br><br>
    Ask me anything about Decode Labs' courses,
    internships, technologies, services,
    or company details.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("Decode Labs")

    
    
    st.caption(f"👤 Welcome, {st.session_state['user']}")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ==========================================
# SESSION
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================================
# DISPLAY CHAT
# ==========================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==========================================
# CHAT INPUT
# ==========================================

prompt = st.chat_input("Ask anything about Decode Labs...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):

        try:

            response = client.models.generate_content(

                model="gemini-2.5-flash",

                contents=f"""
You are Decode Labs AI Assistant.

If the user greets you with words like Hi, Hello, Hey, Good Morning or Good Evening,
reply with:

Hello! 👋 Welcome to Decode Labs AI Assistant.
How can I help you today?

If the user exit you with words like bye, thank you, 
reply with:

For all Decode Labs related questions,
answer ONLY using the knowledge base below.

Knowledge Base:

{knowledge}

User Question:

{prompt}

If the answer is not available in the knowledge base, reply:

Sorry, I couldn't find that information in the Decode Labs knowledge base.
"""
            )

            answer = response.text

        except Exception as e:

            answer = f"❌ Error: {e}"

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )