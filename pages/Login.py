import streamlit as st

st.set_page_config(page_title="로그인", layout="centered")

st.title("🔐 로그인")

if not st.user:
    st.write("Google 계정으로 로그인해주세요.")
    st.login("oidc", provider="google")  # 실제 로그인 작동
else:
    st.success(f"환영합니다, {st.user.name}님!")
    st.page_link("pages/02_Chat.py", label="💬 채팅으로 이동")

st.divider()
st.button("🍎 Apple 로그인 (준비 중)", disabled=True)
st.page_link("app.py", label="🏠 홈으로 돌아가기")
