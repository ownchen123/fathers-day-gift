import streamlit as st
import time
import base64
import os

# 页面配置
st.set_page_config(page_title="致老爸的一封信", page_icon="✉️", layout="centered")

st.markdown("""
<style>

/* =======================
   Cyber Memory Archive
   ======================= */

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600&display=swap');

.stApp{
    background:
        radial-gradient(circle at top,#1e2248 0%,#0b1021 45%,#050814 100%);
    color:#e6f4ff;
    font-family:'Orbitron',sans-serif;
}

/* 扫描线 */

.stApp::before{
    content:"";
    position:fixed;
    left:0;
    top:0;
    width:100%;
    height:100%;
    pointer-events:none;

    background:
        repeating-linear-gradient(
            to bottom,
            rgba(255,255,255,0.03),
            rgba(255,255,255,0.03) 1px,
            transparent 2px,
            transparent 4px
        );

    z-index:999;
}

/* 标题 */

h1,h2,h3{
    color:#78d7ff !important;
    text-shadow:
        0 0 10px #4fc3ff,
        0 0 20px #4fc3ff;
}

p,div,label{
    color:#dbefff !important;
}

/* 中央内容区域 */

.block-container{
    max-width:900px;
    padding-top:2rem;
}

/* 卡片 */

[data-testid="stVerticalBlock"]{
    border-radius:20px;
}

/* 图片 */

img{
    border-radius:18px !important;

    border:1px solid rgba(0,255,255,0.35);

    box-shadow:
        0 0 25px rgba(0,255,255,0.25),
        inset 0 0 20px rgba(255,255,255,0.05);

    transition:0.4s;
}

img:hover{
    transform:scale(1.02);
}

/* 输入框 */

.stTextInput input{

    background:rgba(255,255,255,0.05)!important;

    border:1px solid rgba(0,255,255,.4)!important;

    border-radius:12px!important;

    color:white!important;

    text-align:center;

    font-size:18px;

    backdrop-filter:blur(8px);
}

/* Slider */

.stSlider{
    padding-top:15px;
}

.stSlider div[data-baseweb="slider"] div{
    color:#00eaff;
}

/* 按钮 */

.stButton button{

    background:
        linear-gradient(
        135deg,
        #00c6ff,
        #0072ff
        ) !important;

    border:none !important;

    border-radius:14px !important;

    height:55px;

    color:white !important;

    font-weight:600;

    letter-spacing:2px;

    box-shadow:
        0 0 15px rgba(0,200,255,0.5);

    transition:0.3s;
}

.stButton button:hover{

    transform:translateY(-3px);

    box-shadow:
        0 0 30px rgba(0,255,255,0.8);
}

/* 分割线 */

hr{
    border:none;
    height:1px;
    background:linear-gradient(
        to right,
        transparent,
        #00ffff,
        transparent
    );
}

/* Caption */

[data-testid="stCaptionContainer"]{
    text-align:center;
    color:#93dfff !important;
}

/* 音频播放器 */

audio{
    width:100%;
}

/* Markdown 信息框 */

.cyber-box{
    background:rgba(255,255,255,.04);

    border:1px solid rgba(0,255,255,.25);

    border-radius:18px;

    padding:20px;

    backdrop-filter:blur(12px);

    box-shadow:
        0 0 20px rgba(0,255,255,.15);
}

/* 闪烁动画 */

@keyframes glow{
    0%{opacity:.6}
    50%{opacity:1}
    100%{opacity:.6}
}

.glow{
    animation:glow 2s infinite;
}

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

st.markdown("""
<div style='text-align:center;margin-top:20px;'>

<h1 style='font-size:42px'>
MEMORY ARCHIVE
</h1>

<p style='letter-spacing:4px'>
ACCESSING ENCRYPTED FILES...
</p>

</div>
""",unsafe_allow_html=True)
st.markdown("---")

# 环节 0：拉开序幕
if st.session_state.stage == 0:
    st.code("""
        SYSTEM ONLINE
        
        Loading Memory Database...
        
        Identity Confirmed:
        USER : 爸爸
        
        Access Level :
        HIGHEST
        
        Decrypting Childhood Archive...
        """)
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

    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        try:
            st.image("primary.jpg", use_container_width=True)
        except:
            st.caption("（请上传 primary.jpg）")
            
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
    # 【核心修改点：缩小 solo.jpg】
    # 将原来的 [1, 1] 等分改为非等分，让右侧 solo.jpg 的列变得更窄
    col1, col2 = st.columns([3, 2]) 
    with col1:
        try:
            st.image("travel.jpg", use_container_width=True)
        except:
            st.caption("（请上传 travel.jpg ）")
    with col2:
        # 【二次缩小与居中】
        # 在窄列中，再次使用 columns 技巧来居中图片并进一步缩小
        sub_col1, sub_col2, sub_col3 = st.columns([1, 6, 1]) # 再次缩小居中
        with sub_col2:
            try:
                st.image("solo.jpg", use_container_width=True)
            except:
                st.caption("（请上传 solo.jpg 雁荡山照片）")
            
    st.write(" ")
    
    if "anim_done" not in st.session_state:
        text_placeholder1 = st.empty()
        text_placeholder2 = st.empty()
        text_placeholder3 = st.empty()
        
        text_placeholder1.markdown("#### 那是你在雁荡山拍下的满意之作")
        time.sleep(4) 
        text_placeholder2.markdown("#### 而我，")
        time.sleep(4)
        text_placeholder3.markdown("<h3 style='color:#8B0000 !important;'>成为你的骄傲了吗？</h3>", unsafe_allow_html=True)
        
        st.session_state.anim_done = True
    else:
        st.markdown("#### 那是你在雁荡山拍下的满意之作")
        st.markdown("#### 而我，")
        st.markdown("<h3 style='color:#8B0000 !important;'>成为你的骄傲了吗？</h3>", unsafe_allow_html=True)
    
    st.write(" ")
    ans = st.text_input("（如果我是你的骄傲，请在这里输入“是”）")
    if st.button("拆开信件的最后"):
        if "是" in ans or ans != "":
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
    
    st.markdown("""
        <div class="cyber-box">
        
        <h2 style="text-align:center;">
        FINAL MESSAGE
        </h2>
        
        <hr>
        
        <p style="font-size:20px;line-height:2;">
        
        爸爸，父亲节快乐。
        
        虽然现在我不在你们身边，
        
        但那些一起走过的路、
        一起搬过的行李、
        一起看过的风景，
        
        都被存进了我的人生数据库。
        
        谢谢你一直以来的守护。
        
        在我的世界里，
        
        你永远都是等级最高的超级英雄。
        
        ❤️
        
        </p>
        
        </div>
        """,unsafe_allow_html=True)
    
    st.write(" ")
    if st.button("合上信纸"):
        st.session_state.stage = 0
        st.rerun()
