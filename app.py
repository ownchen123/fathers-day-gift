import streamlit as st
import time

# 页面配置
st.set_page_config(page_title="老爸专属回忆大闯关", page_icon="🎮", layout="centered")

# 注入自定义 CSS：改为温和的“复古小游戏”暖色调，不再是刺眼的黑客绿
st.markdown("""
<style>
    .stApp { background-color: #2b2b36; color: #f0f0f0; font-family: 'Microsoft YaHei', sans-serif; }
    h1, h2, h3, p, div, label { color: #f0f0f0 !important; }
    /* 输入框样式：深灰底，暖色边框 */
    .stTextInput input { 
        background-color: #3b3b46 !important; 
        color: #ffffff !important; 
        border: 2px solid #5a5a72 !important; 
        border-radius: 8px; 
    }
    .stTextInput input:focus {
        border-color: #ff9f43 !important; 
        box-shadow: 0 0 8px #ff9f43 !important; 
    }
    /* 按钮样式：活力橙色，圆角 */
    .stButton button { 
        background-color: #ff9f43 !important; 
        border: none !important;
        border-radius: 8px; 
        width: 100%;
        transition: 0.3s;
    }
    .stButton button p { 
        color: #ffffff !important; 
        font-weight: bold !important;
        font-size: 16px !important;
    }
    .stButton button:hover { 
        background-color: #ff7f50 !important; 
    }
    /* 进度条颜色 */
    .stProgress > div > div > div > div { background-color: #ff9f43; }
</style>
""", unsafe_allow_html=True)

# 初始化游戏进度
if 'stage' not in st.session_state:
    st.session_state.stage = 0

# 游戏标题
st.title("🎮 老爸专属回忆大闯关")

# 进度条显示 (总共5个阶段，0到4)
progress_text = f"当前进度：第 {st.session_state.stage + 1} / 5 关"
st.progress((st.session_state.stage) / 4, text=progress_text)
st.markdown("---")

# ================= 关卡逻辑 =================

# 第 1 关：热身与小时候的照片
if st.session_state.stage == 0:
    st.write("【系统提示】欢迎玩家登录！检测到您是本店的尊贵VIP老爸，正在为您加载专属数据...")
    st.write("但在看礼物之前，必须要通过几道考验！")
    
    # 幽默互动：不需要照片的纯文字问答
    ans0 = st.text_input("▶ 第一题：请摸着良心回答，咱家到底是谁说了算？（请输入称呼）", key="q0")
    if st.button("提交答案"):
        if "妈" in ans0 or "老婆" in ans0:
            st.session_state.stage = 1
            st.rerun()
        elif ans0:
            st.error("【警告】回答错误！请认清家庭地位重新作答！😂")

# 第 2 关：幽默回应 + 旅游照片
elif st.session_state.stage == 1:
    st.success("【回答正确】觉悟很高嘛！既然如此，给你看点有年代感的东西：")
    
    try:
        st.image("childhood.jpg", caption="当年那个调皮捣蛋的小孩", use_container_width=True)
    except:
        st.warning("（这里会显示你小时候的照片，请确保已上传 childhood.jpg）")
    
    st.write("一转眼我都这么大了。老爸，咱们家以前也走过不少地方...")
    
    ans1 = st.text_input("▶ 第二题：还记得我第一次坐飞机/看海是去哪里旅游吗？", key="q1")
    if st.button("提交答案"):
        # 【此处修改】将“北京”替换为你们真实的旅游地点关键字
        if "北京" in ans1 or "三亚" in ans1: 
            st.session_state.stage = 2
            st.rerun()
        elif ans1:
            st.error("【提示】老爸你再好好想想，是不是记串了？")

# 第 3 关：展示旅游照 + 进入个人照关卡
elif st.session_state.stage == 2:
    st.success("【通关】老爸记性可以啊！")
    
    try:
        st.image("travel.jpg", caption="那些年我们的旅行轨迹", use_container_width=True)
    except:
        st.warning("（这里会显示旅游照片，请确保已上传 travel.jpg）")
        
    st.write("那时候去玩可开心了，哪怕一路上都是你在拎包扛行李。")
    st.markdown("---")
    st.write("接下来这道题稍微有点技术含量了：")
    
    ans2 = st.text_input("▶ 第三题：你最拿手的那个绝活菜（比如红烧肉），通常要放几勺酱油？", key="q2")
    if st.button("提交答案"):
        if "两" in ans2 or "2" in ans2: # 替换为正确的答案关键字
            st.session_state.stage = 3
            st.rerun()
        elif ans2:
            st.error("【错误】大厨怎么连自己的秘方都忘了？")

# 第 4 关：个人照 + 灵魂拷问（雁荡山）
elif st.session_state.stage == 3:
    st.write("【密码正确】正在解锁核心区域...")
    with st.spinner("加载高品质影像中..."):
        time.sleep(1)
        
    try:
        st.image("solo.jpg", use_container_width=True)
    except:
        st.warning("（这里会显示雁荡山的个人照，请确保已上传 solo.jpg）")
        
    st.markdown("### 这是你在雁荡山拍下的满意之作，")
    st.markdown("### 而我，成为你的骄傲了吗？")
    
    st.write(" ")
    st.write("老爸，准备好接收最终的礼物了吗？")
    ans3 = st.text_input("▶ 最后一题：请输入通关密语（提示：三个字，包含“爱”字）", key="q3")
    if st.button("开启终极宝箱"):
        if "爱你" in ans3:
            st.session_state.stage = 4
            st.rerun()
        elif ans3:
            st.error("就差一点点了！别不好意思敲出来！")

# 第 5 关：最终全家福 + 音频 + 煽情祝福
elif st.session_state.stage == 4:
    st.balloons() # 触发全屏气球特效
    st.success("🎉 通关大吉！全家福碎片已拼齐！")
    
    try:
        st.image("family.jpg", caption="我们这一家子", use_container_width=True)
    except:
        st.warning("（这里会显示全家福，请确保已上传 family.jpg）")
        
    st.markdown("---")
    
    try:
        st.audio("voice.mp3")
    except:
        st.warning("（这里会播放音频，请确保已上传 voice.mp3）")
        
    st.write("""
    爸爸，节日快乐！
    
    刚才的雁荡山照片一直存在我的相册里。其实不用等到什么特别的日子，你在我心里一直都是最棒的榜样。虽然平时咱们爷俩可能交流没那么多，或者偶尔还要拌两句嘴，但我知道你为这个家付出了多少。
    
    以后换我来做你的底气。今天别操心家里的事了，好好休息，做个快乐的“老男孩”！
    """)
    
    st.write(" ")
    if st.button("重新回顾游戏"):
        st.session_state.stage = 0
        st.rerun()
