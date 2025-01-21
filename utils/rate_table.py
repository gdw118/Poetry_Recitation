import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
from matplotlib.ticker import PercentFormatter
import constant


def load_data():
    return pd.read_csv(constant.file_path222)


def provide_learning_advice(mean_value, variance_value):
    # 定义正确率和方差的阈值
    high_rate_threshold = 0.85  # 高正确率阈值
    low_rate_threshold = 0.60  # 低正确率阈值
    high_variance_threshold = 0.05  # 高方差阈值，表示不稳定性

    # 分析并提供学习建议
    if mean_value >= high_rate_threshold:
        if variance_value < high_variance_threshold:
            advice = "您的学习表现优秀，而且表现很稳定，请继续保持！"
        else:
            advice = "您的学习表现很不错，但是不够稳定。还需要进一步稳固记忆哦！"
        st.success(advice)  # 使用 Streamlit 显示建议
    elif high_rate_threshold > mean_value >= low_rate_threshold:
        advice = "您的作答正确率还不错，但有提升空间，继续加油！"
        st.warning(advice)
    else:
        advice = "您的正确率稍差，需要加油背诵哦~"
        st.error(advice)


def show_rate_table():
    df1 = load_data()
    x = range(len(df1) - 10, len(df1))
    y = df1.iloc[len(df1) - 10:len(df1), 2]

    # 通过计算平均值和方差值来给出一些学习建议
    column_data = df1.iloc[:, 2]
    mean_value = column_data.mean()  # 计算平均正确率
    variance_value = column_data.var()  # 计算正确率方差

    # 创建折线图
    fig, ax = plt.subplots()  # 创建图形和轴
    ax.plot(x, y, marker='o')

    # 添加标题和标签
    ax.set_title("Correct Rate Plot")
    ax.set_xlabel("Turn")
    ax.set_ylabel("Correct Rate")

    ax.set_xticks(x)

    # 设置y轴为百分比格式
    ax.yaxis.set_major_formatter(PercentFormatter(1))

    # 显示图形
    st.write("您的正确率变化如下：")
    st.pyplot(fig)

    # 使用 Streamlit 显示结果
    mean_value *= 100
    st.write(f"平均正确率: {mean_value:.2f}%")
    st.write(f"波动程度: {variance_value:.2f}")
    provide_learning_advice(mean_value/100, variance_value)
