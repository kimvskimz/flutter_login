
import streamlit as st
st.write("🔥 secrets keys:", list(st.secrets.keys()))
import requests
import json


st.set_page_config(page_title="로그인", layout="centered")
st.title("🔐 Google 로그인 (Firebase REST API)")

API_KEY = st.secrets["FIREBASE"]["api_key"]

if "user" not in st.session_state:
    st.session_state["user"] = None

def google_sign_in():
    # Google OAuth endpoint (Firebase)
    redirect_uri = "https://fitmindmove.streamlit.app/pages/Login"  # 앱 주소로 변경
    provider = "google.com"
    params = {
        "providerId": provider,
        "requestUri": redirect_uri,
        "returnIdpCredential": True,
        "returnSecureToken": True
    }
    auth_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithIdp?key={API_KEY}"
    return auth_url, params

if st.session_state["user"]:
    st.success(f"환영합니다, {st.session_state['user']['displayName']}님!")
    if st.button("로그아웃"):
        st.session_state["user"] = None
        st.rerun()
    st.page_link("pages/02_Chat.py", label="💬 채팅으로 이동")

else:
    st.info("아래 버튼을 눌러 Google 계정으로 로그인하세요.")
    if st.button("🔑 Google 로그인"):
        st.write("⚙️ Firebase Google 로그인 흐름은 브라우저 리디렉션이 필요합니다.")
        st.markdown("[Google 로그인 바로가기](https://accounts.google.com/o/oauth2/v2/auth)")

    # 임시 테스트: REST API로 이메일/비밀번호 로그인 (테스트용)
    with st.expander("이메일 로그인 (테스트용)"):
        email = st.text_input("이메일")
        password = st.text_input("비밀번호", type="password")
        if st.button("로그인 시도"):
            payload = {
                "email": email,
                "password": password,
                "returnSecureToken": True
            }
            r = requests.post(
                f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}",
                json=payload
            )
            data = r.json()
            if "idToken" in data:
                st.session_state["user"] = {"email": data["email"], "idToken": data["idToken"]}
                st.success(f"로그인 성공: {data['email']}")
                st.rerun()
            else:
                st.error(f"로그인 실패: {data.get('error', {}).get('message', '알 수 없음')}")
