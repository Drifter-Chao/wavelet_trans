# streamlit run D:\fc_python\wavelet_transform_project\app.py
# pyinstaller --onefile --add-data "D:/ProgramData/miniconda3/envs/wavelet/lib/site-packages/streamlit;streamlit" app.py
import streamlit as st
import pandas as pd
from src.preprocess import load_data
from src.wavelet_transform import dwt_transform, cwt_transform
from src.visualize import plot_dwt, plot_cwt

st.set_page_config(
    page_title="小波变换",
    page_icon="assets/icon_character.png"
)
# 设置标题
st.title("小波变换可视化")
print(st.__file__)
# 上传文件
uploaded_file = st.file_uploader("上传数据文件", type=["csv"])
if uploaded_file is not None:
    # 加载数据
    data = load_data(uploaded_file)
    
    # 显示上传的数据预览
    st.write("上传的数据预览：")
    st.write(data.head())
    
    # 选择列名
    columns = data.columns.tolist()  # 获取所有列名
    selected_column = st.selectbox("选择需要操作的列", columns)  # 让用户选择列名

    # 选择行名（选择行索引）
    row_indices = data.index.tolist()  # 获取所有行的索引
    selected_row_index = st.selectbox("选择需要操作的行", row_indices)  # 让用户选择行索引

    # 提取选择的列数据
    selected_data_column = data[selected_column]
    st.write(f"你选择的列：{selected_column}，数据：", selected_data_column)
    
    # 提取选择的行数据
    selected_data_row = data.loc[selected_row_index]
    st.write(f"你选择的行索引：{selected_row_index}，数据：", selected_data_row)
    
    # 离散小波变换 (DWT)
    transformed_data_dwt = dwt_transform(selected_data_column)
    st.write("离散小波变换 (DWT) 结果：")
    plot_dwt(selected_data_column, transformed_data_dwt)  # 显示 DWT 结果

    # 连续小波变换 (CWT)
    transformed_data_cwt, frequencies = cwt_transform(selected_data_column)
    st.write("连续小波变换 (CWT) 结果：")
    plot_cwt(selected_data_column, transformed_data_cwt, frequencies)  # 显示 CWT 结果