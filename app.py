import streamlit as st
import random
# 手机微信适配配置，隐藏侧边栏
st.set_page_config(
    page_title="本命能量T测试",
    page_icon="☀️",
    layout="centered",
    initial_sidebar_state="collapsed"
)
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# 初始化会话状态
def init_session():
    if "page" not in st.session_state:
        st.session_state.page = "cover"
    if "score_sport" not in st.session_state:
        st.session_state.score_sport = 0
    if "score_life" not in st.session_state:
        st.session_state.score_life = 0
    if "score_love" not in st.session_state:
        st.session_state.score_love = 0
    if "current_q" not in st.session_state:
        st.session_state.current_q = 0
    if "final_gender" not in st.session_state:
        st.session_state.final_gender = None
init_session()
# 5道题目：Q1性别，Q2‑Q5四道能量题
questions = [
    {
        "q": "你的性别是？",
        "options": ["男生", "女生"],
        "type": "gender"
    },
    {
        "q": "夏日精力耗竭时，你更倾向用哪种方式给自己快速充电？",
        "options": ["挥洒运动释放能量", "美食烟火治愈自己", "陪伴、独处感受温柔"],
        "type": "energy"
    },
    {
        "q": "抛开工作琐事，你心中理想的夏日周末会如何安排？",
        "options": ["外出动一动流汗", "探店吃喝感受烟火", "晒太阳或安静度日"],
        "type": "energy"
    },
    {
        "q": "置身夏日氛围，下面哪一种感觉最让你觉得舒服自在？",
        "options": ["动感鲜活有张力", "热闹充满生活气息", "柔和温暖松弛治愈"],
        "type": "energy"
    },
    {
        "q": "压力来袭，夏日解压你会优先选择？",
        "options": ["运动释放掉压力", "美食犒劳抚慰情绪", "慢下来向内安顿自我"],
        "type": "energy"
    }
]
# ==========货品池，全部png格式==========
goods_pool = [
    # 男生 + 爱意：4张
    {"sku":"M‑LO‑01","gender":"man","energy_key":"love","img_path":"g01.png"},
    {"sku":"M‑LO‑02","gender":"man","energy_key":"love","img_path":"g02.png"},
    {"sku":"M‑LO‑03","gender":"man","energy_key":"love","img_path":"g03.png"},
    {"sku":"M‑LO‑04","gender":"man","energy_key":"love","img_path":"g04.png"},
    # 男生 + 生活：10张
    {"sku":"M‑LI‑01","gender":"man","energy_key":"life","img_path":"g05.png"},
    {"sku":"M‑LI‑02","gender":"man","energy_key":"life","img_path":"g06.png"},
    {"sku":"M‑LI‑03","gender":"man","energy_key":"life","img_path":"g07.png"},
    {"sku":"M‑LI‑04","gender":"man","energy_key":"life","img_path":"g08.png"},
    {"sku":"M‑LI‑05","gender":"man","energy_key":"life","img_path":"g09.png"},
    {"sku":"M‑LI‑06","gender":"man","energy_key":"life","img_path":"g10.png"},
    {"sku":"M‑LI‑07","gender":"man","energy_key":"life","img_path":"g11.png"},
    {"sku":"M‑LI‑08","gender":"man","energy_key":"life","img_path":"g12.png"},
    {"sku":"M‑LI‑09","gender":"man","energy_key":"life","img_path":"g13.png"},
    {"sku":"M‑LI‑10","gender":"man","energy_key":"life","img_path":"g14.png"},
    # 男生 + 运动：2张
    {"sku":"M‑SP‑01","gender":"man","energy_key":"sport","img_path":"g15.png"},
    {"sku":"M‑SP‑02","gender":"man","energy_key":"sport","img_path":"g16.png"},
    # 女生 + 爱意：9张
    {"sku":"W‑LO‑01","gender":"woman","energy_key":"love","img_path":"g17.png"},
    {"sku":"W‑LO‑02","gender":"woman","energy_key":"love","img_path":"g18.png"},
    {"sku":"W‑LO‑03","gender":"woman","energy_key":"love","img_path":"g19.png"},
    {"sku":"W‑LO‑04","gender":"woman","energy_key":"love","img_path":"g20.png"},
    {"sku":"W‑LO‑05","gender":"woman","energy_key":"love","img_path":"g21.png"},
    {"sku":"W‑LO‑06","gender":"woman","energy_key":"love","img_path":"g22.png"},
    {"sku":"W‑LO‑07","gender":"woman","energy_key":"love","img_path":"g23.png"},
    {"sku":"W‑LO‑08","gender":"woman","energy_key":"love","img_path":"g24.png"},
    {"sku":"W‑LO‑09","gender":"woman","energy_key":"love","img_path":"g25.png"},
    # 女生 + 生活：7张
    {"sku":"W‑LI‑01","gender":"woman","energy_key":"life","img_path":"g26.png"},
    {"sku":"W‑LI‑02","gender":"woman","energy_key":"life","img_path":"g27.png"},
    {"sku":"W‑LI‑03","gender":"woman","energy_key":"life","img_path":"g28.png"},
    {"sku":"W‑LI‑04","gender":"woman","energy_key":"life","img_path":"g29.png"},
    {"sku":"W‑LI‑05","gender":"woman","energy_key":"life","img_path":"g30.png"},
    {"sku":"W‑LI‑06","gender":"woman","energy_key":"life","img_path":"g31.png"},
    {"sku":"W‑LI‑07","gender":"woman","energy_key":"life","img_path":"g32.png"},
    # 女生 + 运动：1张
    {"sku":"W‑SP‑01","gender":"woman","energy_key":"sport","img_path":"g33.png"},
]
# 3套能量文案
energy_info = {
    "sport":{"title":"运动能量｜热烈迸发","desc":"向往活力流动，热爱舒展身体，用动感对抗夏日沉闷。","slogan":"热力全开，自在奔赴"},
    "life":{"title":"生活能量｜烟火松弛","desc":"忠于人间烟火，懂得享受日常细碎的欢愉与松弛。","slogan":"烟火日常，自得欢愉"},
    "love":{"title":"爱意能量｜温柔舒展","desc":"内心柔软温暖，既能拥抱阳光热闹，也享受独处平和。","slogan":"心怀暖意，温柔生长"}
}
# 选项文本映射3种能量key
def get_energy_key(opt_text):
    if opt_text in ["挥洒运动释放能量","外出动一动流汗","动感鲜活有张力","运动释放掉压力"]:
        return "sport"
    elif opt_text in ["美食烟火治愈自己","探店吃喝感受烟火","热闹充满生活气息","美食犒劳抚慰情绪"]:
        return "life"
    elif opt_text in ["陪伴、独处感受温柔","晒太阳或安静度日","柔和温暖松弛治愈","慢下来向内安顿自我"]:
        return "love"
    return None
# 同分随机选能量
def calc_result():
    score_dict = {
        "sport":st.session_state.score_sport,
        "life":st.session_state.score_life,
        "love":st.session_state.score_love
    }
    max_score = max(score_dict.values())
    candidates = [k for k,v in score_dict.items() if v == max_score]
    return random.choice(candidates)
# 匹配逻辑：性别 + 能量，在分组内随机抽取一件
def select_item(gender, energy, goods):
    group = [g for g in goods if g["gender"]==gender and g["energy_key"]==energy]
    if group:
        return random.choice(group)
    return None
# ----------------------封面页 cover----------------------
if st.session_state.page == "cover":
    st.markdown("""
    <div style="text-align:center; max-width:600px; margin:3rem auto 0 auto; padding:0 16px;">
        <h1 style="font-size:2.2rem; line-height:1.3;">测测你的今日能量场</h1>
        <p style="font-size:1.2rem; margin:1rem 0 2.5rem 0;">解锁专属于你的夏日能量T</p>
    </div>
    """, unsafe_allow_html=True)
    col1,col2,col3 = st.columns([2,2,2])
    with col2:
        if st.button("开始测试",use_container_width=True):
            st.session_state.page = "quiz"
            st.rerun()
# ----------------------答题页 quiz----------------------
elif st.session_state.page == "quiz":
    idx = st.session_state.current_q
    q_item = questions[idx]
    st.markdown(f"""
    <div style="text-align:center; max-width:600px; margin:2rem auto; padding:0 16px;">
        <h2 style="font-size:1.6rem; line-height:1.4;">{q_item['q']}</h2>
    </div>
    """, unsafe_allow_html=True)
    for opt in q_item["options"]:
        col1,col2,col3 = st.columns([1,4,1])
        with col2:
            if st.button(opt, use_container_width=True):
                if q_item["type"] == "gender":
                    st.session_state.final_gender = "man" if opt=="男生" else "woman"
                elif q_item["type"] == "energy":
                    ek = get_energy_key(opt)
                    if ek == "sport":
                        st.session_state.score_sport +=1
                    elif ek == "life":
                        st.session_state.score_life +=1
                    elif ek == "love":
                        st.session_state.score_love +=1
                st.session_state.current_q += 1
                if st.session_state.current_q >= len(questions):
                    st.session_state.page = "result"
                st.rerun()
# ----------------------结果页 result----------------------
elif st.session_state.page == "result":
    final_energy = calc_result()
    final_gender = st.session_state.final_gender
    pick = select_item(final_gender,final_energy,goods_pool)
    info = energy_info[final_energy]

    st.markdown("""
    <div style="text-align:center; max-width:600px; margin:2rem auto; padding:0 16px;">
        <h1 style="font-size:2.3rem; font-weight:bold;">你的本命能力T</h1>
    </div>
    """,unsafe_allow_html=True)
    # T恤图片居中容器，最大宽度360px手机不会撑太大
    st.markdown('<div style="max-width:360px; margin:0 auto;">',unsafe_allow_html=True)
    if pick:
        try:
            st.image(pick["img_path"], use_container_width=True)
        except Exception as e:
            st.warning(f"图片缺失：{pick['img_path']}")
    else:
        st.warning("当前条件下暂无匹配款式")
    st.markdown('</div>',unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align:center; max-width:520px; margin:1.5rem auto; padding:0 16px;">
        <p style="font-size:1.3rem; font-weight:600;margin:4px 0;">{info['title']}</p>
        <p style="font-size:1rem; color:#444;">{info['desc']}</p>
        <p style="font-size:1.1rem;margin-top:8px;color:#d64848;">✨ {info['slogan']}</p>
    </div>
    """,unsafe_allow_html=True)
    # 重新测试按钮，完整清空全部状态
    c1,c2,c3 = st.columns([1,2,1])
    with c2:
        if st.button("重新测试",use_container_width=True):
            del st.session_state["page"]
            del st.session_state["score_sport"]
            del st.session_state["score_life"]
            del st.session_state["score_love"]
            del st.session_state["current_q"]
            del st.session_state["final_gender"]
            init_session()
            st.rerun()
