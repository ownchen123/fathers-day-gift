import streamlit as st
import time
import base64
import os

# 页面配置
st.set_page_config(page_title="拆礼物", page_icon="✉️", layout="centered")

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
.stTextInput > div > div > div {
    background-color: transparent !important;
}

.stTextInput div[data-baseweb="input"], 
.stTextInput div[data-baseweb="base-input"],
.stTextInput input {
    background-color: rgba(5, 15, 35, 0.7) !important; /* 深邃的赛博蓝黑底色 */
    border: 1px solid rgba(0, 255, 255, 0.4) !important;
    color: #00ffff !important;
    border-radius: 8px !important;
    text-align: center;
    font-size: 18px;
    box-shadow: none !important;
}

.stTextInput div[data-baseweb="input"]:focus-within {
    border-color: #00ffff !important;
    box-shadow: 0 0 15px rgba(0, 255, 255, 0.5) !important; /* 聚焦时发光 */
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
            
.terminal-box{

    background:rgba(0,15,35,.75);

    border:1px solid rgba(0,255,255,.3);

    border-radius:20px;

    padding:30px;

    font-family:Consolas,monospace;

    color:#7ee7ff;

    font-size:22px;

    line-height:2;

    box-shadow:
        0 0 30px rgba(0,255,255,.15);

    backdrop-filter:blur(15px);
}
            
.stApp::after{

    content:"";

    position:fixed;

    top:0;
    left:0;

    width:100%;
    height:100%;

    pointer-events:none;

    background-image:
      radial-gradient(circle,#00ffff 1px,transparent 1px),
      radial-gradient(circle,#ffffff 1px,transparent 1px),
      radial-gradient(circle,#6cf 1px,transparent 1px);

    background-size:
      180px 180px,
      260px 260px,
      320px 320px;

    opacity:.25;

    animation:starsMove 80s linear infinite;

    z-index:-1;
}

@keyframes starsMove{

    from{
        transform:translateY(0);
    }

    to{
        transform:translateY(-400px);
    }
}
            
.hud-panel{

    background:
    linear-gradient(
        135deg,
        rgba(0,255,255,.05),
        rgba(0,100,255,.08)
    );

    border:1px solid rgba(0,255,255,.3);

    border-radius:20px;

    padding:25px;

    backdrop-filter:blur(20px);

    box-shadow:
        0 0 30px rgba(0,255,255,.15);

    margin-bottom:25px;
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

    background:
    linear-gradient(
        135deg,
        rgba(0,255,255,.05),
        rgba(0,80,255,.08)
    );

    border:1px solid rgba(0,255,255,.3);

    border-radius:22px;

    padding:35px;

    backdrop-filter:blur(20px);

    box-shadow:
        0 0 40px rgba(0,255,255,.2);
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

# 初始化进度状态
if 'stage' not in st.session_state:
    st.session_state.stage = 0

# ================= 互动信件环节 =================

st.markdown("""
<div style='text-align:center;margin-top:20px;'>

<h1 style='font-size:42px'>
记忆档案
</h1>

<p style='letter-spacing:4px'>
正在访问加密文件……
</p>

</div>
""",unsafe_allow_html=True)
st.markdown("---")

# 环节 0：拉开序幕
if st.session_state.stage == 0:
    

    st.markdown("""
        <div class="terminal-box">

        系统已上线<br>
        加载记忆数据库...<br><br>

        身份确认:爸爸<br>
        访问级别 :最高级<br><br>

        正在解密文件...<br>
        [系统提示] 检测到加密回忆文件，需进行身份验证<br>
        请将时间轴拨回到我出生的那一年

        </div>
        """, unsafe_allow_html=True)
    
    year = st.slider("", 2000, 2026, 2020)
    
    if st.button("确认"):
        if year == 2004:  
            st.session_state.stage = 1
            st.rerun()
        else:
            st.caption("年份好像不太对哦，再想想？（提示：问问妈妈）")

# 环节 1
elif st.session_state.stage == 1:
    # st.write("拨动时间，好像又回到了小时候……")
    # st.write("和我比赛跑步，却总是故意输给我……")
    # st.write("带着总是生病的我，在医院跑上跑下……")
    st.markdown("""
        <div class="terminal-box">

        拨动时间，好像又回到了小时候……<br><br>
                
        和我比赛跑步，却总是故意输给我……<br><br>

        带着总是生病的我，在医院跑上跑下……<br>

        </div>
        """, unsafe_allow_html=True)
    
    if st.button("提取视觉影像"):
        st.session_state.stage = 2
        st.rerun()

# 环节 2
elif st.session_state.stage == 2:
    st.write("哈哈哈，小时候的我，还挺可爱的吧")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            st.image("childhood.jpg", use_container_width=True)
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

    col1, col2, col3 = st.columns([1, 2, 1])
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
    
    st.write("> 后来，我们也走过很多地方……")
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
        
        # --- 打字机效果 1 ---
        text1 = "那是你在雁荡山拍下的满意之作"
        current_text1 = ""
        for char in text1:
            current_text1 += char
            # 加上 █ 光标，更有终端敲击感
            text_placeholder1.markdown(f"#### {current_text1}█")
            time.sleep(0.08) # 敲击间隔
        text_placeholder1.markdown(f"#### {text1}") # 敲完后移除光标
        time.sleep(0.5) 
        
        # --- 打字机效果 2 ---
        text2 = "而我，"
        current_text2 = ""
        for char in text2:
            current_text2 += char
            text_placeholder2.markdown(f"#### {current_text2}█")
            time.sleep(0.15) # 稍微放慢节奏，营造停顿感
        text_placeholder2.markdown(f"#### {text2}")
        time.sleep(0.8)
        
        # --- 打字机效果 3 (带发光特效) ---
        text3 = "成为你的骄傲了吗？"
        current_text3 = ""
        for i in range(1, len(text3) + 1):
            current_text3 = text3[:i]
            text_placeholder3.markdown(
                f"""
                <h2 style="text-align:center; color:#00ffff; text-shadow:0 0 15px #00ffff;">
                {current_text3}█
                </h2>
                """,
                unsafe_allow_html=True
            )
            time.sleep(0.18) # 终极提问，逐字重击

        # 最终定格状态，移除光标
        text_placeholder3.markdown(
            """
            <h2 style="text-align:center; color:#00ffff; text-shadow:0 0 15px #00ffff;">
            成为你的骄傲了吗？
            </h2>
            """,
            unsafe_allow_html=True
        )

        st.session_state.anim_done = True
    else:
        # 如果老爸重新加载页面，直接显示最终状态，不再重复打字动画
        st.markdown("#### 那是你在雁荡山拍下的满意之作")
        st.markdown("#### 而我，")
        st.markdown(
            """
            <h2 style="text-align:center; color:#00ffff; text-shadow:0 0 15px #00ffff;">
            成为你的骄傲了吗？
            </h2>
            """, 
            unsafe_allow_html=True
        )
        
    st.write(" ")
    ans = st.text_input("（如果我是你的骄傲，请在这里输入“是”）")
    if st.button("解锁终极核心权限"):
        if "是" in ans or ans != "":
            if "anim_done" in st.session_state:
                del st.session_state["anim_done"]
            st.session_state.stage = 6
            st.rerun()

elif st.session_state.stage == 6:
    st.write("我知道你的答案。因为你在我心里，也一直都是那个超人爸爸！")
    st.write(" ")

    # 【横向并排修改】将比例设为 4:5，让右侧的文本框有足够宽度展示信件
    col1, col2 = st.columns([4, 5])
    
    with col1:
        try:
            st.image("family.jpg", caption="永远的避风港", use_container_width=True)
        except:
            st.caption("（请上传 family.jpg）")

    with col2:
        # 【嵌套：声音条置于文本框上方】
        try:
            st.audio("voice.mp3")
        except:
            st.warning("（这里会播放音频，请确保已上传 voice.mp3）")
            
        # 文本框紧跟其后
        st.markdown("""
        <div class="cyber-box glow" style="margin-top: 15px;">
        
        <h2 style="text-align:center;">FINAL MESSAGE</h2>
        
        <hr>
        
        <p style="font-size:18px; line-height:1.8; margin-top:10px;">
        爸爸，父亲节快乐呀！<br><br>
        那些一起走过的路、一起看过的风景，<br><br>
        都被存进了我的人生数据库。<br><br>
        在我的世界里，<br>
        你永远都是等级最高的超级英雄！<br><br>
        </p>
        
        </div>
        """, unsafe_allow_html=True)
    
    st.write(" ")
    if st.button("终止系统进程"):
        st.session_state.stage = 0
        st.rerun()
