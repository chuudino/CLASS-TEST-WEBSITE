import streamlit as st
from utils import init_page

init_page()  # 初始化頁面配置

st.title("公告")  # 設定頁面標題
st.write("這是一則公告。")  # 顯示公告內容
