import os
import dotenv
import streamlit as st
from .menu import menu

dotenv.load_dotenv()


def init_page():
    DEV = os.getenv("dev")
    if DEV == "True":
        import subprocess

        try:
            subprocess.run(
                ["pipreqs", ".", "--force"], check=True, text=True, capture_output=True
            )
        except Exception as e:
            print(f"命令執行失敗：\n{e}")

    st.set_page_config(
        page_title="Dino's website", page_icon="images/tyrannosaurus.png", layout="wide"
    )
    st.logo("images/tyrannosaurus.png")
    menu()
