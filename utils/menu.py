import streamlit as st


def menu():
    st.sidebar.page_link(
        page="main.py", label="首頁", icon="🏠"
    )  # 在側邊欄添加首頁連結
    st.sidebar.markdown("---")  # 添加分隔線
    st.sidebar.page_link(
        page="pages/announcement.py", label="公告", icon="📢"
    )  # 在側邊欄添加公告連結
    st.sidebar.markdown("---")  # 添加分隔線
