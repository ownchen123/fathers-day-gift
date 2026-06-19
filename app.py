import streamlit as st
import time

# 页面配置：设置标题和移动端适配
st.set_page_config(page_title="System Auth", page_icon="💻", layout="centered")

# 注入自定义 CSS，强制全局黑底绿字，模拟复古终端风格
st.markdown("""
<style>
    .stApp { background-color: #0c0c0c; color: #00ff00; font-family: 'Courier New', Courier, monospace; }
    h1, h2, h3, p, div, label { color: #00ff00 !important; font-family: 'Courier New', Courier, monospace; }
    .stTextInput input { background-color: #1e1e1e; color: #00ff00; border: 1px solid #00ff00; border-radius: 2px; }
    .stButton button { background-color: #00ff00; color: #000000; font-weight: bold; border-radius: 4px; border: none; width: 100%;}
    .stButton button:hover { background-color: #00cc00; color: #ffffff; }
    .stAudio { filter: sepia(20%) hue-rotate(90deg) saturate(300%); } /* 让音频播放器也带点复古绿滤镜 */
</style>
""", unsafe_allow_html=True)

# 使用 session_state 管理游戏进度状态
if 'stage' not in st.session_state:
    st.session_state.stage = 0

st.title("> root@family-server:~$ ./fathers_day.sh")

# 第 0 关：系统启动与第一道验证
if st.session_state.stage == 0:
    st.write("Initializing system boot...")
    st.write("Checking permissions...")
    st.write("User identified: DAD.")
    st.markdown("---")
    st.write("[SYSTEM PROMPT] 检测到加密回忆文件，需进行身份验证。")
    
    # 替换成只有你们知道的问题
    ans1 = st.text_input("> 请输入密码 (问题：我上大学走的那天，你送我去车站穿的什么颜色的衣服？)", key="q1")
    
    if st.button("Enter ↵"):
        if "蓝" in ans1:  # 设定你的正确答案
            st.session_state.stage = 1
            st.rerun()
        elif ans1:
            st.error("> [ERROR] Password incorrect. Try again.")

# 第 1 关：解锁照片与第二道验证
elif st.session_state.stage == 1:
    st.write("> Access Granted. Loading memory block 1...")
    st.markdown("---")
    
    # 展示照片，使用相对路径调用同一文件夹下的图片
    try:
        st.image("memory.jpg", caption="[LOG: FILE EXTRACTED SUCCESSFULLY]", use_container_width=True)
    except:
        st.warning("[WARNING] memory.jpg missing. Please upload the photo.")
    
    st.write("其实那时候我有点紧张，但看到你站在前面，我就觉得没什么好怕的。")
    st.write("[SYSTEM PROMPT] 核心加密区仍未解锁，请进行最终验证。")
    
    ans2 = st.text_input("> 请输入数字指令 (问题：你最拿手的那道红烧肉，通常要炖多少分钟？)", key="q2")
    
    if st.button("Execute ↵"):
        if "40" in ans2 or "四十" in ans2: # 设定你的正确答案
            st.session_state.stage = 2
            st.rerun()
        elif ans2:
            st.error("> [ERROR] Command failed. Try again.")

# 第 2 关：最终解锁音频与走心语句
elif st.session_state.stage == 2:
    st.write("> Override confirmed. Decrypting core files...")
    # 制造一点终端打字的延迟感
    with st.spinner("Decoding audio sequence..."):
        time.sleep(1.5)
    st.markdown("---")
    
    st.write("### [SUCCESS] Happy Father's Day!")
    
    # 展示音频文件
    try:
        st.audio("voice.mp3")
    except:
        st.warning("[WARNING] voice.mp3 missing. Please upload the audio.")
    
    # 朴素的煽情语句
    st.write("""
    > 爸，平时很少把爱挂在嘴边。
    > 很多时候我更习惯在终端里敲代码，掌控着程序的运行。
    > 但其实我心里一直都知道，你才是我人生这套系统里，那个永远在后台静静运行、最稳固的底层逻辑。
    >
    > 谢谢你一直以来的包容和支撑。
    > 节日快乐！今天别干活了，好好休息。
    """)
    
    if st.button("Logout"):
        st.session_state.stage = 0
        st.rerun()