import requests
import streamlit as st

API_BASE = "https://fitmindmove.atozsoftware.net/api"  # 나중에 실제 백엔드 주소로 교체

def query(text: str) -> str:
    """백엔드에 질문 전송. 현재는 모의응답"""
    try:
        # 실제 연결 시 아래 주석 해제
        # r = requests.post(f"{API_BASE}/query", json={"text": text}, timeout=10)
        # return r.json().get("answer", "응답 없음")
        return f"백엔드 연결 준비 중: '{text}' 에 대한 모의응답입니다."
    except Exception as e:
        return f"API 오류: {e}"
