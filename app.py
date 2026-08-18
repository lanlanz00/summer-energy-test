# ----------------------结果页 result----------------------
elif st.session_state.page == "result":
    final_energy = calc_result()
    final_gender = st.session_state.final_gender
    pick = select_item(final_gender, final_energy, goods_pool)
    info = energy_info[final_energy]

    st.markdown("""
    <div style="text-align:center; max-width:600px; margin:1.2rem auto 0.8rem auto; padding:0 16px;">
        <h1 style="font-size:1.8rem; font-weight:bold;">你的本命能力T</h1>
    </div>
    """, unsafe_allow_html=True)

    # T恤图片居中，最大高度压缩，避免一屏装不下
    st.markdown('<div style="max-width:280px; margin:0 auto;">', unsafe_allow_html=True)
    if pick:
        try:
            st.image(pick["img_path"], use_container_width=True)
        except Exception as e:
            st.warning(f"图片缺失：{pick['img_path']}")
    else:
        st.warning("当前条件下暂无匹配款式")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align:center; max-width:520px; margin:0.8rem auto; padding:0 16px;">
        <p style="font-size:1.15rem; font-weight:600; margin:4px 0;">{info['title']}</p>
        <p style="font-size:0.95rem; color:#444; line-height:1.5;">{info['desc']}</p>
        <p style="font-size:1rem; margin-top:6px; color:#d64848;">✨ {info['slogan']}</p>
    </div>
    """, unsafe_allow_html=True)

    # 重新测试按钮
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("重新测试", use_container_width=True):
            del st.session_state["page"]
            del st.session_state["score_sport"]
            del st.session_state["score_life"]
            del st.session_state["score_love"]
            del st.session_state["current_q"]
            del st.session_state["final_gender"]
            init_session()
            st.rerun()
