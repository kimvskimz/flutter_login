import streamlit as st
from datetime import datetime

st.set_page_config(page_title="FitMindMove Chat", layout="wide")
st.title("💬 FitMindMove 챗봇")

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 기존 대화 표시
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 사용자 입력
if prompt := st.chat_input("무엇이 고민이신가요?"):
    # 사용자 메시지 저장 및 표시
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 임시 LLM 응답 (테스트용)
    response = f"({datetime.now().strftime('%H:%M:%S')}) 제가 이해한 것은: '{prompt}' 입니다."
    with st.chat_message("assistant"):
        st.markdown(response)

    # 챗봇 응답 저장
    st.session_state.messages.append({"role": "assistant", "content": response})
