
import streamlit as st

params = st.experimental_get_query_params()
if "code" in params:
    st.session_state["auth_code"] = params["code"][0]
    st.write("✅ Google 인증 코드 받음!")
else:
    st.error("❌ 인증 코드가 없습니다.")
