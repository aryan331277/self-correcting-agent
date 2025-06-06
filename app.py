# streamlit_app.py

import streamlit as st
from agent import self_correcting_agent

st.set_page_config(page_title="Self-Correcting Reasoning Agent", layout="centered")

st.title("🧠 Self-Correcting Reasoning Agent")
st.markdown("Uses **Mistral/Mixtral models** via Ollama to solve problems with internal verification.")

question = st.text_area("Enter your question:", height=100, placeholder="E.g., A train leaves Station A at 60 km/h...")

if st.button("Solve"):
    if not question.strip():
        st.error("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            final_answer, steps = self_correcting_agent(question)

        st.markdown("---")
        st.subheader("🔍 Step-by-Step Process")

        for step in steps:
            st.markdown(f"**{step['step']}:**")
            st.code(step['content'])

        st.markdown("---")
        st.subheader("✅ Final Answer")
        st.markdown(final_answer)
