import streamlit as st
import time
import base64
import os

# 页面配置
st.set_page_config(page_title="致老爸的一封信", page_icon="✉️", layout="centered")

# 温情相册风 CSS
st.markdown("""
<style>
    /* 暖色调信纸背景和深褐色文字 */
    .stApp { background-color: #FAF3E0; color: #5C4A3D; font-family: '楷体', 'STKaiti', serif; }
    h1, h2, h3, p, div, label { color: #5C4A3D !important; }
    
    /* 弱化输入框的科技感，使其像填空题 */
    .stTextInput input { 
        background-color: transparent !important; 
        color: #8B5A2B !important; 
        border: none !important; 
        border-bottom: 2px solid #D4A373 !important; 
        border-radius: 0px; 
        text-align: center;
        font-size: 18px;
    }
    .stTextInput input:focus { box-shadow: none !important; border-bottom: 2px solid #A0522D !important; }
    
    /* 按钮变成类似火漆印章或旧质感书签 */
    .stButton button { 
        background-color: #D4A373 !important; 
        border: none !important;
        border-radius: 4px; 
        width: 100%;
        transition: 0.3s;
    }
    .stButton button p { color: #FFFFFF !important; font-size: 16px !important; letter-spacing: 2px; }
    .stButton button:hover { background-color: #BC8F8F !important; }
    
    /* 滑块颜色 */
    .stSlider > div > div > div > div { background-color: #D4A373 !important; }
</style>
""", unsafe_allow_html=True)

# 注入自动播放的隐藏 BGM (需在用户首次点击后才能突破浏览器限制播放)
def get_base64_audio(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

audio_b64 = get_base64_audio("bgm.mp3")
if audio_b64 and 'stage' in st.session_state and st.session_state.stage > 0:
    # 只要进入了第1阶段，就隐藏插入音频并循环播放
    audio_html = f"""
        <audio autoplay loop style="display:none;">
            <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
        </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)


# 初始化进度状态
if 'stage' not in st.session_state:
    st.session_state.stage = 0

# ================= 互动信件环节 =================

st.markdown("<h2 style='text-align: center;'>时光慢递 ✉️</h2>", unsafe_allow_html=True)
st.markdown("---")

# 环节 0：拉开序幕（拖拽时间轴互动）
if st.session_state.stage == 0:
    st.write("老爸，平时有些话当面总是不好意思说。今天，我想带你走一段时光隧道。")
    st.write(" ")
    
    # 互动：滑动条
    year = st.slider("请将时间轴拨回到我上大学离家的那一年：", 2000, 2026, 2020)
    
    # 替换为你实际上大学的年份
    if st.button("开启回忆"):
        if year == 2024:  # 【需修改】把2024改成你的真实年份
            st.session_state.stage = 1
            st.rerun()
        else:
            st.caption("年份好像不太对哦，再想想？（提示：其实无论哪一年，对你来说可能都历历在目）")

# 环节 1：离家回忆 -> 解锁童年与旅行照
elif st.session_state.stage == 1:
    st.write("拨动时间，好像又回到了你送我去车站的那天。")
    st.write("其实那天我有点紧张，但看着你走在前面的背影，我就觉得没什么好怕的。你的肩膀，一直是我人生里最稳固的依靠。")
    st.write(" ")
    
    # 互动：点击拼凑记忆
    if st.button("翻开老相册"):
        st.session_state.stage = 2
        st.rerun()

# 环节 2：双图并排展示（控制图片大小）
elif st.session_state.stage == 2:
    st.write("从小到大，你牵着我的手，带我看了很多风景。")
    
    # 使用 columns 把图片缩小并排在一行
    col1, col2 = st.columns(2)
    with col1:
        try:
            st.image("childhood.jpg", caption="那时的我还在你肩头", use_container_width=True)
        except:
            st.caption("（请上传 childhood.jpg）")
    with col2:
        try:
            st.image("travel.jpg", caption="你带着我丈量世界", use_container_width=True)
        except:
            st.caption("（请上传 travel.jpg）")

    st.write("风景再美，现在回想起来，最踏实的还是有你在身边。")
    st.write(" ")
    
    # 互动：填空题
    food = st.text_input("对了，看了这么多地方，我最馋的还是你做的那道：")
    if st.button("确认"):
        if food != "":
            st.session_state.stage = 3
            st.rerun()

# 环节 3：雁荡山个人照与灵魂共鸣
elif st.session_state.stage == 3:
    st.write(f"哪怕吃过再多山珍海味，最想念的永远是你做的那口家的味道。")
    st.markdown("---")
    
    # 缩小单人照的尺寸（通过嵌套 columns 控制比例）
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            st.image("solo.jpg", use_container_width=True)
        except:
            st.caption("（请上传 solo.jpg 雁荡山照片）")
            
    st.write(" ")
    # 循序渐进的煽情小字
    st.markdown("#### 这是你在雁荡山拍下的满意之作。")
    time.sleep(1) # 增加一点渲染时间的停顿感
    st.markdown("#### 那天你看着远方的山，")
    time.sleep(1)
    st.markdown("#### 而我，")
    st.markdown("<h3 style='color:#8B0000 !important;'>成为你的骄傲了吗？</h3>", unsafe_allow_html=True)
    
    st.write(" ")
    ans = st.text_input("（老爸，如果我是你的骄傲，请在这里输入“是”）")
    if st.button("拆开信件的最后"):
        if "是" in ans or ans != "":
            st.session_state.stage = 4
            st.rerun()

# 环节 4：全家福与最终告白
elif st.session_state.stage == 4:
    st.write("我知道你的答案。因为你在我心里，也一直都是最棒的父亲。")
    
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        try:
            st.image("family.jpg", caption="永远的避风港", use_container_width=True)
        except:
            st.caption("（请上传 family.jpg）")

    st.markdown("---")
    st.write("""
    爸爸，父亲节快乐。
    
    也许我不善言辞，也许我离家在外不能天天陪着你，但请你相信，你给予我的爱和底气，足够我勇敢地面对这世界上的任何困难。
    
    以后，换我来做你和妈妈的依靠。
    今天什么都别操心了，好好休息。我爱你，老爸。
    """)
    
    st.write(" ")
    if st.button("合上信纸"):
        st.session_state.stage = 0
        st.rerun()
