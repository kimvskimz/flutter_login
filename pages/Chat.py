import streamlit as st
from datetime import datetime

st.set_page_config(page_title="FitMindMove 채팅", layout="wide")

st.title("💬 FitMindMove 챗봇")

if not st.user:
    st.warning("로그인 후 이용할 수 있습니다.")
    st.page_link("pages/Login.py", label="로그인으로 이동")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("무엇이 고민이신가요?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 임시 챗봇 응답
    response = f"[{datetime.now().strftime('%H:%M:%S')}] '{prompt}'에 대한 더미 응답입니다."
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
