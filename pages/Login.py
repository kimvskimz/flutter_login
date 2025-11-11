import streamlit as st
import requests
import json

# ------------------- 필수 설정 -------------------
st.set_page_config(page_title="로그인", layout="centered")

# ------------------- Firebase API -------------------
st.title("🔐 Google 로그인 (Firebase REST API)")

# Firebase secrets 확인
if "FIREBASE" not in st.secrets:
    st.error("❌ Firebase API key가 설정되지 않았습니다.")
    st.stop()

API_KEY = st.secrets["FIREBASE"]["api_key"]

# ------------------- 세션 초기화 -------------------
if "user" not in st.session_state:
    st.session_state["user"] = None


# ------------------- Google 로그인 버튼 -------------------
if st.session_state["user"]:
    st.success(f"환영합니다, {st.session_state['user'].get('email', '사용자')}님!")
    if st.button("로그아웃", key="logout_btn"):
        st.session_state["user"] = None
        st.rerun()
    st.page_link("pages/Chat.py", label="💬 채팅으로 이동")

else:
    st.info("아래 버튼을 눌러 Google 계정으로 로그인하세요.")

    if st.button("🔑 Google 로그인", key="google_login_btn"):
    GOOGLE_CLIENT_ID = "801950083850-nd7a45hvtcokrrnc435v8g8g9mbnih3f.apps.googleusercontent.com"
    REDIRECT_URI = "https://fitmindmove.streamlit.app/pages/Login"
    SCOPE = "email profile openid"

    auth_url = (
        "https://accounts.google.com/o/oauth2/v2/auth"
        f"?client_id={GOOGLE_CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&response_type=code"
        f"&scope={SCOPE}"
        f"&access_type=online"
    )

    # ✅ 즉시 브라우저 리디렉션
    st.write("🔁 Google 로그인 페이지로 이동 중입니다...")
    st.markdown(
        f"""
        <meta http-equiv="refresh" content="0; url={auth_url}">
        """,
        unsafe_allow_html=True,
    )


    # ------------------- 이메일 로그인 (테스트용) -------------------
    with st.expander("📧 이메일 로그인 (테스트용)"):
        email = st.text_input("이메일", key="email_input")
        password = st.text_input("비밀번호", type="password", key="password_input")
        if st.button("로그인 시도", key="email_login_btn"):
            payload = {
                "email": email,
                "password": password,
                "returnSecureToken": True,
            }
            r = requests.post(
                f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}",
                json=payload,
            )
            data = r.json()
            if "idToken" in data:
                st.session_state["user"] = {
                    "email": data["email"],
                    "idToken": data["idToken"],
                }
                st.success(f"로그인 성공: {data['email']}")
                st.rerun()
            else:
                err = data.get("error", {}).get("message", "알 수 없는 오류")
                st.error(f"로그인 실패: {err}")
