import streamlit as st
import os
import runpy
st.set_page_config(layout="wide", page_title="My Multi-Page App")
def set_env_variable(key, value):
    os.environ[key] = value
def home_page():
    st.header("欢迎来到首页")
    # 设置输入框为隐私状态
    token = st.text_input("请输入浦语token:", type="password", key="token")
    weather_token = st.text_input("请输入和风天气token:", type="password", key="weather_token")
    if st.button("保存并体验agent"):
        if token and weather_token:
            set_env_variable("token", token)  # 设置环境变量为 'token'
            set_env_variable("weather_token", weather_token)  # 设置环境变量为 'weather_token'
            st.session_state.token_entered = True
            st.rerun()
        else:
            st.error("请输入所有token")
if 'token_entered' not in st.session_state:
    st.session_state.token_entered = False
if not st.session_state.token_entered:
    home_page()
else:
    # 动态加载子页面
    page = st.sidebar.radio("选择页面", ["天气查询助手", "博客写作助手"])
    if page == "天气查询助手":
        runpy.run_path("examples/agent_api_web_demo.py", run_name="__main__")
    elif page == "博客写作助手":
        runpy.run_path("examples/multi_agents_api_web_demo.py", run_name="__main__")