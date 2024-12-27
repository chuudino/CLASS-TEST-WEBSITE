import os
import dotenv
import streamlit as st
from .menu import menu

dotenv.load_dotenv()  # 載入 .env 檔案中的環境變數


def init_page():
    DEV = os.getenv("dev")  # 從環境變數中取得 "dev" 的值
    if DEV == "True":
        import subprocess

        try:
            subprocess.run(
                ["pipreqs", ".", "--force"], check=True, text=True, capture_output=True
            )  # 執行 pipreqs 命令來生成 requirements.txt 檔案
        except Exception as e:
            print(f"命令執行失敗：\n{e}")  # 如果命令執行失敗，打印錯誤訊息

    st.set_page_config(
        page_title="Dino's website", page_icon="images/tyrannosaurus.png", layout="wide"
    )  # 設定 Streamlit 頁面的配置
    st.logo("images/tyrannosaurus.png")  # 設定頁面的 logo
    menu()  # 顯示側邊欄選單
