import streamlit as st
import pandas as pd
import random
import constant

df = pd.read_csv(constant.file_path111)


def recite():
    if 'if_next' not in st.session_state:
        st.session_state.if_next = False
    if 'prompt' not in st.session_state:
        st.session_state.prompt = ''
    if 'correct_answer' not in st.session_state:
        st.session_state.correct_answer = ''
    if 'show' not in st.session_state:
        st.session_state.show = []
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False
    if 'initiated' not in st.session_state or st.session_state.initiated is False:
        # 初始化题目
        random_row = df.sample()
        st.session_state.initiated = True

        poem = random_row.iloc[:, 3].values[0].split('。')
        poem[0] = poem[0] + '。'
        poem[1] = poem[1] + '。'

        i = random.randint(0, 1)
        test = poem[i].split('，', 1)
        if len(test) > 1:
            test[0] += '，'
        else:
            test.append('')

        st.session_state.show = test

        # 随机挖空上半句或下半句
        j = random.randint(0, 1)
        if j == 0:
            st.session_state.prompt = "___________，" + test[1]
            st.session_state.correct_answer = test[0].replace('，', '')
        else:
            st.session_state.prompt = test[0] + "___________。"
            st.session_state.correct_answer = test[1].replace('。', '')

    # 显示题目和输入框
    answer = st.text_input("请填空：" + st.session_state.prompt, key=f"input_{st.session_state.count}")

    # 检查是否点击提交按钮
    if st.button("提交本题", key=f"submit_{st.session_state.count}"):
        st.session_state.submitted = True
        if answer == st.session_state.correct_answer:
            st.session_state.cnt_correct += 1
            st.success("答对了！你真棒！")
        else:
            st.error(f"很遗憾！答错了。正确答案是：{st.session_state.show[0] + st.session_state.show[1]}")
        # 做题数量+1
        st.session_state.count += 1

    # 只有在提交答案后显示“下一道题”按钮
    if st.session_state.submitted:
        if st.button("下一道题"):
            st.session_state.initiated = False  # 重置初始化状态，使下一道题可以开始初始化
            st.session_state.submitted = False
            st.rerun()  # 强制立即重新运行脚本，即强制刷新一次界面
