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

# 【优化4】将BGM放到页面最顶层，避免每次重绘时从头播放
def get_base64_audio(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

audio_b64 = get_base64_audio("bgm.mp3")
if audio_b64:
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

# 环节 0：拉开序幕
if st.session_state.stage == 0:
    st.write("Initializing system boot...")
    st.write("Checking permissions...")
    st.write("用户身份确认: 爸爸.")
    st.markdown("---")
    st.write("[系统提示] 检测到加密回忆文件，需进行身份验证")
    
    year = st.slider("请将时间轴拨回到我出生的那一年：", 2000, 2026, 2020)
    
    if st.button("确认"):
        if year == 2004:  
            st.session_state.stage = 1
            st.rerun()
        else:
            st.caption("年份好像不太对哦，再想想？（提示：问问妈妈）")

# 环节 1
elif st.session_state.stage == 1:
    st.write("拨动时间，好像又回到了小时候……")
    st.write("和我比赛跑步，却总是故意输给我……")
    st.write("带着总是生病的我，在医院跑上跑下……")
    
    if st.button("翻开记忆相册"):
        st.session_state.stage = 2
        st.rerun()

# 环节 2
elif st.session_state.stage == 2:
    st.write("哈哈哈，小时候的我，还挺可爱的吧")
    
    # 【优化1】修正上下文管理器报错，并居中缩小图片
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            st.image("childhood.jpg", caption="那时的我还在你肩头", use_container_width=True)
        except:
            st.caption("（请上传 childhood.jpg）")
    
    year = st.slider("请将时间轴拨到我读小学那一年：", 2000, 2026, 2020)
    
    if st.button("确认"):
        if year == 2011:  
            st.session_state.stage = 3
            st.rerun()
        else:
            st.caption("年份好像不太对哦，再想想？（提示：8岁上小学）")

# 环节 3
elif st.session_state.stage == 3:
    st.write("金鸡冠的公鸡~")
    st.write("竟然一晃又是12年过去了，那天，是我的19岁生日……")
    
    year = st.slider("请将时间轴拨到上大学的那年：", 2000, 2026, 2020)
    if st.button("确认"):
        if year == 2023:  
            st.session_state.stage = 4
            st.rerun()
        else:
            st.caption("年份好像不太对哦，再想想？（提示：又过了12年）")

# 环节 4
elif st.session_state.stage == 4:
    st.write("那年夏天，我们哼哧哼哧搬着五袋行李，从平阳来到杭州……")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            st.image("college.jpg", caption="2023.9.16", use_container_width=True)
        except:
            st.caption("（请上传 college.jpg）")
    
    ans2 = st.text_input("> 后来，我们也走过很多地方……")
    
    if st.button("继续旅程 ↵"):
        st.session_state.stage = 5
        st.rerun()

# 环节 5 (重点动画修复区)
elif st.session_state.stage == 5:
    col1, col2 = st.columns([1,1])
    with col1:
        try:
            st.image("travel.jpg", use_container_width=True)
        except:
            st.caption("（请上传 travel.jpg ）")
    with col2:
        try:
            st.image("solo.jpg", use_container_width=True)
        except:
            st.caption("（请上传 solo.jpg 雁荡山照片）")
            
    st.write(" ")
    
    # 【优化2】借助 st.empty() 实现文字循序渐进出现的动画效果
    # 只有当这是本阶段第一次加载时才播放动画，防止后续点击报错重演
    if "anim_done" not in st.session_state:
        text_placeholder1 = st.empty()
        text_placeholder2 = st.empty()
        text_placeholder3 = st.empty()
        
        text_placeholder1.markdown("#### 那是你在雁荡山拍下的满意之作")
        time.sleep(2) 
        text_placeholder2.markdown("#### 而我，")
        time.sleep(2)
        text_placeholder3.markdown("<h3 style='color:#8B0000 !important;'>成为你的骄傲了吗？</h3>", unsafe_allow_html=True)
        
        # 标记动画已完成
        st.session_state.anim_done = True
    else:
        # 如果动画已播放过，直接显示静态文字，防止等待重构
        st.markdown("#### 那是你在雁荡山拍下的满意之作")
        st.markdown("#### 而我，")
        st.markdown("<h3 style='color:#8B0000 !important;'>成为你的骄傲了吗？</h3>", unsafe_allow_html=True)
    
    st.write(" ")
    ans = st.text_input("（如果我是你的骄傲，请在这里输入“是”）")
    if st.button("拆开信件的最后"):
        if "是" in ans or ans != "":
            # 进入下一关前清理动画状态
            if "anim_done" in st.session_state:
                del st.session_state["anim_done"]
            st.session_state.stage = 6
            st.rerun()

# 环节 6：最终告白
elif st.session_state.stage == 6:
    st.write("我知道你的答案。因为你在我心里，也一直都是那个超人爸爸！")

    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        try:
            st.image("family.jpg", caption="永远的避风港", use_container_width=True)
        except:
            st.caption("（请上传 family.jpg）")

    try:
        st.audio("voice.mp3")
    except:
        st.warning("（这里会播放音频，请确保已上传 voice.mp3）")
        
    st.markdown("---")
    
    # 【优化3】移除导致文字消失的 st.spinner，改为直接渲染排版
    st.markdown("""
    <div style='background-color:#EEDC82; padding:20px; border-radius:10px; color:#5C4A3D; font-size:18px; line-height:1.8;'>
    爸爸，父亲节快乐。<br><br>
    也许我不善言辞，也许我离家在外不能天天陪着你，但请你相信，你给予我的爱和底气，足够我勇敢地面对这世界上的任何困难。<br><br>
    以后，换我来做你和妈妈的依靠。<br>
    今天什么都别操心了，好好休息。我爱你，老爸。
    </div>
    """, unsafe_allow_html=True)
    
    st.write(" ")
    if st.button("合上信纸"):
        st.session_state.stage = 0
        st.rerun()
