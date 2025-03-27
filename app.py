import streamlit as st

st.title("Streamlit测试应用")
st.write("这是我的第一个Streamlit应用")

name = st.text_input("请输入你的名字")
if name:
    st.write(f"你好，{name}！")

number = st.slider("选择一个数字", 0, 100)
st.write(f"你选择的数字是：{number}")