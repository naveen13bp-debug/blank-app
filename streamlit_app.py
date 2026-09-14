import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="My AI Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 My AI Assistant")
st.caption("Tamil + English • Construction • Property • Business")

SYSTEM_PROMPT = """
You are my personal AI assistant.

Understand and reply in Tamil, English, or mixed Tamil-English.

Help me with:
- Construction calculations and planning
- Property buying and document checklists
- Business planning
- Quotations and estimates
- General daily work

For calculations, show the calculation steps.
For property/legal/structural matters, clearly say what needs
verification by a qualified professional.

Be practical, simple and helpful.
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if not st.session_state.messages:
    st.info("வணக்கம்! நான் உங்கள் Personal AI Assistant. என்ன செய்ய வேண்டும்?")

prompt = st.chat_input(
    "Type here... உதாரணம்: 1250 sqft roof concrete calculation"
)

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        try:
            client = OpenAI()

            response = client.responses.create(
                model="gpt-5.6",
                instructions=SYSTEM_PROMPT,
                input=st.session_state.messages
            )

            answer = response.output_text

        except Exception as e:
            answer = (
                "AI connection error.\n\n"
                "Please check the API key and app settings.\n\n"
                f"Error: {e}"
            )

        st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
