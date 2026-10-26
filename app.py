import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


st.set_page_config(
    page_title="ToneShift AI",
    page_icon="✨",
    layout="wide",
)

st.title("✨ ToneShift AI")
st.write("Say it your way. Just better.")
st.write("Transform your messages while preserving their meaning.")
left, right = st.columns(2, gap="large")

with left:
    st.subheader("✍️ Your message")

    message = st.text_area(
        "Original message",
        placeholder=(
            "Example: hey, i can't finish this today. "
            "can i send it tomorrow?"
        ),
        height=190,
        max_chars=5000,
    )

    tone = st.selectbox(
        "Choose your tone",
        ["Professional", "Friendly", "Polite", "Confident", "Concise"],
    )

    length = st.selectbox(
        "Preferred length",
        [
            "Keep roughly the same length",
            "Make it shorter",
            "Add a little detail",
        ],
    )

    generate = st.button(
        "✨ Transform my message",
        type="primary",
        use_container_width=True,
    )

with right:
    st.subheader("🪄 How it works")
    st.markdown("""
    **1. Your input**  
    Enter a message and choose a tone.

    **2. Generation**  
    Gemini generates a rewritten message.
    """)

if generate:
    api_key = os.getenv("GEMINI_API_KEY")
    model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    if not message.strip():
        st.warning("Please enter a message first.")
    elif not api_key:
        st.error("API key missing. Add GEMINI_API_KEY to your .env file.")
    else:
        prompt = f"""
Rewrite the following message in a {tone.lower()} tone.
Return only the rewritten message.

{message}
"""
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
        )
        st.subheader("✨ Your transformed message")
        st.write(response.text)