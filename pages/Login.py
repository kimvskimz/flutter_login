import streamlit as st

st.set_page_config(page_title="로그인", layout="centered")
st.title("🔐 로그인")

# --- 세션 안전 초기화 ---
if "user" not in st.session_state:
    st.session_state["user"] = None

user = st.session_state["user"]

# --- 로그인 상태 확인 ---
if user:
    st.success(f"환영합니다, {user['name']}님!")
    if st.button("로그아웃"):
        st.session_state["user"] = None
        st.rerun()
    st.page_link("pages/Chat.py", label="💬 채팅으로 이동")

else:
    with st.form("login_form"):
        name = st.text_input("이름 (테스트용)")
        email = st.text_input("이메일 (형식 자유)")
        submit = st.form_submit_button("로그인")

    if submit:
        if not name:
            st.warning("이름을 입력하세요.")
        else:
            st.session_state["user"] = {"name": name, "email": email}
            st.success(f"로그인 성공: {name}")
            st.rerun()

st.divider()
st.button("🍎 Apple 로그인 (준비 중)", disabled=True)
st.page_link("streamlit_app.py", label="🏠 홈으로 돌아가기")
