# src/visualize.py
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def plot_dwt(original_data, transformed_data):
    """
    在 Streamlit 中可视化离散小波变换（DWT）的结果，包括原始信号。
    
    参数:
    - original_data (array-like): 原始信号数据。
    - transformed_data (dict): 包含 DWT 变换结果的字典，键包括：
      - "Approximation"：近似系数
      - "Detail Level N"：各层细节系数
    """
    # 总子图数量：原始信号 + 各层系数
    total_plots = 1 + len(transformed_data)
    fig, axs = plt.subplots(total_plots, 1, figsize=(10, 8))
    
    # 如果只有一个子图，axs 不是数组，因此需要判断
    if total_plots == 1:
        axs = [axs]
    
    # 绘制原始信号
    axs[0].plot(original_data, color='blue')
    axs[0].set_title('Original Signal')
    
    # 绘制各层细节系数和近似系数
    for i, (key, value) in enumerate(transformed_data.items()):
        axs[i + 1].plot(value)
        axs[i + 1].set_title(f'{key}')
    
    plt.tight_layout()
    
    # 在 Streamlit 中显示图像
    st.pyplot(fig)

def plot_cwt(original_data, coefficients, frequencies):
    """
    在 Streamlit 中可视化连续小波变换（CWT）的结果和原始信号
    
    参数:
    - original_data (array-like): 原始信号数据。
    - coefficients (numpy array): CWT 变换后的系数，表示信号在不同尺度下的变换结果。
    - frequencies (numpy array): 对应的小波频率。
    """
    # 创建上下两部分的子图
    fig, axs = plt.subplots(2, 1, figsize=(12, 8), gridspec_kw={'height_ratios': [1, 3]})
    
    # 绘制原始信号
    axs[0].plot(original_data, color='blue', linewidth=1)
    axs[0].set_title('Original Signal', fontsize=12)
    axs[0].set_xlabel('Time', fontsize=10)
    axs[0].set_ylabel('Amplitude', fontsize=10)
    axs[0].grid(True)
    
    # 绘制时频图
    im = axs[1].imshow(
        np.abs(coefficients), 
        aspect='auto', 
        extent=[0, coefficients.shape[1], frequencies[-1], frequencies[0]], 
        cmap='jet', 
        interpolation='bilinear'
    )
    axs[1].set_title('Continuous Wavelet Transform (CWT) - Time-Frequency Representation', fontsize=12)
    axs[1].set_xlabel('Time', fontsize=10)
    axs[1].set_ylabel('Frequency (Hz)', fontsize=10)
    
    # 添加颜色条
    cbar = fig.colorbar(im, ax=axs[1], orientation='vertical', label='Magnitude')
    
    # 调整布局以避免重叠
    plt.tight_layout()
    
    # 在 Streamlit 中显示图像
    st.pyplot(fig)