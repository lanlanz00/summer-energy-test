import streamlit as st
import random

# 初始化存储
def init_session():
    defaults = {
        "page": "home",
        "gender": None,
        "score_run": 0,
        "score_food": 0,
        "score_sun": 0,
        "score_yoga": 0,
        "q_index": 0,
        "style_tag": None
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_session()

# 问卷题目，完全你的题干
question_list = [
    {
        "title": "Q2 能量不足，你会怎么充电？",
        "options": [
            ("A｜运动暴汗", "run"),
            ("B｜大吃美食", "food"),
            ("C｜社交相聚", "sun"),
            ("D｜独处放空", "yoga")
        ]
    },
    {
        "title": "Q3 理想周末怎么度过？",
        "options": [
            ("A｜外出运动", "run"),
            ("B｜探店吃喝", "food"),
            ("C｜出门闲逛晒太阳", "sun"),
            ("D｜居家休息", "yoga")
        ]
    },
    {
        "title": "Q4 夏日更喜欢哪种氛围？",
        "options": [
            ("A｜动感热烈", "run"),
            ("B｜趣味治愈", "food"),
            ("C｜热闹明媚", "sun"),
            ("D｜安静松弛", "yoga")
        ]
    },
    {
        "title": "Q5 解压优先选？",
        "options": [
            ("A｜挥洒汗水", "run"),
            ("B｜美食犒劳", "food"),
            ("C｜户外散心", "sun"),
            ("D｜静心舒缓", "yoga")
        ]
    },
    {
        "title": "Q6 选 T 恤更看重？",
        "options": [
            ("A｜简约好穿", "simple"),
            ("B｜潮流丰富", "fashion"),
            ("C｜前卫吸睛", "large")
        ],
        "is_style_q": True
    }
]

energy_meta = {
    "run": {
        "title": "跑步能量场",
        "desc": "享受挥洒汗水的畅快，源源不断向外释放鲜活力量",
        "slogan": "热力全开，奔赴热爱"
    },
    "food": {
        "title": "美食能量场",
        "desc": "热爱人间烟火，在美食里捕捉生活小确幸",
        "slogan": "食趣相伴，快乐满格"
    },
    "sun": {
        "title": "日光能量场",
        "desc": "偏爱热闹与陪伴，拥抱明亮热烈的生活气息",
        "slogan": "向阳而生，自在发光"
    },
    "yoga": {
        "title": "瑜伽能量场",
        "desc": "向内寻找平静，享受独处松弛自在的时刻",
        "slogan": "松弛有度，静心自洽"
    }
}

# ===================== 12条测试货品（测试用，后续可以替换成真实款号） =====================
# 图片文件名：g01.jpg ~ g12.jpg
goods_pool = [
    # 男生 6款
    {"sku":"M‑001","gender":"man","energy_key":"run","style_tag":"simple","img_path":"g01.jpg"},
    {"sku":"M‑002","gender":"man","energy_key":"run","style_tag":"fashion","img_path":"g02.jpg"},
    {"sku":"M‑003","gender":"man","energy_key":"sun","style_tag":"large","img_path":"g03.jpg"},
    {"sku":"M‑004","gender":"man","energy_key":"food","style_tag":"simple","img_path":"g04.jpg"},
    {"sku":"M‑005","gender":"man","energy_key":"food","style_tag":"fashion","img_path":"g05.jpg"},
    {"sku":"M‑006","gender":"man","energy_key":"yoga","style_tag":"large","img_path":"g06.jpg"},
    # 女生 6款
    {"sku":"W‑001","gender":"woman","energy_key":"run","style_tag":"simple","img_path":"g07.jpg"},
    {"sku":"W‑002","gender":"woman","energy_key":"sun","style_tag":"fashion","img_path":"g08.jpg"},
    {"sku":"W‑003","gender":"woman","energy_key":"sun","style_tag":"large","img_path":"g09.jpg"},
    {"sku":"W‑004","gender":"woman","energy_key":"food","style_tag":"simple","img_path":"g10.jpg"},
    {"sku":"W‑005","gender":"woman","energy_key":"yoga","style_tag":"fashion","img_path":"g11.jpg"},
    {"sku":"W‑006","gender":"woman","energy_key":"yoga","style_tag":"large","img_path":"g12.jpg"},
]
# =========================================================================================

# 计算最高分，同分随机选一个能量
def get_energy_key():
    s = {
        "run": st.session_state.score_run,
        "food": st.session_state.score_food,
        "sun": st.session_state.score_sun,
        "yoga": st.session_state.score_yoga
    }
    max_val = max(s.values())
    top_keys = [k for k, v in s.items() if v == max_val]
    return random.choice(top_keys)

# 筛选货品：三条件匹配优先，不匹配就忽略风格兜底
def select_item(gender, energy_key, style_tag):
    full_match = [g for g in goods_pool
                  if g["gender"] == gender
                  and g["energy_key"] == energy_key
                  and g["style_tag"] == style_tag]
    if full_match:
        return random.choice(full_match)
    fallback = [g for g in goods_pool if g["gender"] == gender and g["energy_key"] == energy_key]
    if fallback:
        return random.choice(fallback)
    return None

# 页面样式
st.markdown("""
<style>
.stButton>button {
    width:100%;
    height:3.3rem;
    font-size:16px;
    margin:4px 0;
}
</style>
""", unsafe_allow_html=True)

# 首页
if st.session_state.page == "home":
    st.markdown("# 测测你的今日能量场")
    st.markdown("##### 解锁专属于你的夏日能量T")
    st.divider()
    if st.button("开始测试"):
        st.session_state.page = "q1_gender"
        st.rerun()

# Q1性别
elif st.session_state.page == "q1_gender":
    st.markdown("# Q1（前置，不计分）你的选择？")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("A｜男生"):
            st.session_state.gender = "man"
            st.session_state.q_index = 0
            st.session_state.page = "quiz_loop"
            st.rerun()
    with c2:
        if st.button("B｜女生"):
            st.session_state.gender = "woman"
            st.session_state.q_index = 0
            st.session_state.page = "quiz_loop"
            st.rerun()

# Q2‑Q6循环答题
elif st.session_state.page == "quiz_loop":
    idx = st.session_state.q_index
    q = question_list[idx]
    st.markdown(f"# {q['title']}")
    for opt_text, opt_val in q["options"]:
        if st.button(opt_text):
            if q.get("is_style_q"):
                st.session_state.style_tag = opt_val
            else:
                if opt_val == "run":
                    st.session_state.score_run +=1
                elif opt_val == "food":
                    st.session_state.score_food +=1
                elif opt_val == "sun":
                    st.session_state.score_sun +=1
                elif opt_val == "yoga":
                    st.session_state.score_yoga +=1
            st.session_state.q_index += 1
            if st.session_state.q_index >= len(question_list):
                st.session_state.page = "result_page"
            st.rerun()

# 结果页
elif st.session_state.page == "result_page":
    e_key = get_energy_key()
    picked_goods = select_item(st.session_state.gender,e_key,st.session_state.style_tag)
    info = energy_meta[e_key]

    # --------调试信息，本地测试看分数，上线可以把下面两行删掉--------
    st.write("【调试】分数‑run/food/sun/yoga：",
             st.session_state.score_run,
             st.session_state.score_food,
             st.session_state.score_sun,
             st.session_state.score_yoga)
    st.write("【调试】性别:", st.session_state.gender,"风格标签:", st.session_state.style_tag,"选中能量:",e_key)
    # ----------------------------------------------------------------

    st.markdown("# 你的本命能量T")
    st.divider()
    if picked_goods:
        st.image(picked_goods["img_path"], use_container_width=True)
        st.subheader(f"推荐款号：{picked_goods['sku']}")
    else:
        st.warning("当前条件下暂无匹配款式")

    st.markdown(f"### {info['title']}")
    st.markdown(f"{info['desc']}")
    st.markdown(f"> ✨ {info['slogan']}")
    st.divider()
    if st.button("重新测试"):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()
