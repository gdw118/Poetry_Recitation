import streamlit as st
from utils.crawl import crawl_search
from utils.split_crawl_res import split_res
from utils.recite import recite
from utils.save_correct_rate import save_correct_rate
from utils.rate_table import show_rate_table
import time


def main():
    st.title('享记诗词')

    if 'count' not in st.session_state:
        st.session_state.count = 0
    if 'cnt_correct' not in st.session_state:
        st.session_state.cnt_correct = 0
    if 'start_reciting' not in st.session_state:  # 标志是否已经显示过初始化背诵界面
        st.session_state.start_reciting = False

    mode = st.sidebar.selectbox(
        label="请您选择模式",
        options=("搜索/录入诗歌", "诗歌背诵", "查看正确率走向")
    )

    if mode == "搜索/录入诗歌":
        title = st.text_input("请输入诗歌题目：")
        author = st.text_input("请输入作者：")

        if st.button('搜索并录入'):
            crawl_res = crawl_search(title, author)
            with st.spinner('录入中...'):
                split_res(crawl_res)
                time.sleep(2)
            st.success('诗歌保存成功')

    elif mode == "诗歌背诵":
        if not st.session_state.start_reciting:
            recite_time = st.number_input("请输入需要背诵的诗歌数量", min_value=1, value=1, step=1)
            if st.button('开始背诵'):
                st.session_state.start_reciting = True
                st.session_state.total = recite_time  # 存储用户输入的背诵次数
                st.session_state.count = 0
                st.session_state.cnt_correct = 0
                st.rerun()  # 强制立即重新运行脚本，即强制刷新一次界面

        if st.session_state.start_reciting:
            if st.session_state.count < st.session_state.total:
                recite()

            if st.session_state.count >= st.session_state.total:
                correct_num = st.session_state.cnt_correct
                correct_rate = correct_num / st.session_state.total
                save_correct_rate(correct_num, st.session_state.total, correct_rate)
                st.write(f"本次背诵结束！本次正确率为：{correct_rate:.1%}")

            progress = st.session_state.count / st.session_state.total
            st.progress(progress)

    elif mode == "查看正确率走向":
        show_rate_table()


if __name__ == '__main__':
    main()
