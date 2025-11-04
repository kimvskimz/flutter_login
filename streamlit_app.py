import streamlit as st
import requests

st.title("FitMindMove Prototype")
st.write("스트림릿 연결 테스트입니다.")

name = st.text_input("이름을 입력하세요")
if st.button("확인"):
    st.success(f"환영합니다, {name}님!")

