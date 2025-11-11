import streamlit as st

st.set_page_config(page_title="FitMindMove 홈", layout="centered")

st.title("🏠 FitMindMove 홈")
st.markdown("환영합니다. 아래 메뉴를 통해 로그인 또는 챗봇 페이지로 이동하세요.")

col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/01_Login.py", label="🔐 로그인", icon="🔑")
with col2:
    st.page_link("pages/02_Chat.py", label="💬 채팅", icon="💬")

st.markdown("---")
st.caption("Streamlit 기반 데모 버전")
