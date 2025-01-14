import pywt
import numpy as np

def dwt_transform(data, wavelet='haar', level=2):
    """
    对输入数据进行离散小波变换（DWT），并返回变换结果。
    
    参数:
    - data (list or numpy array): 输入的时序数据。可以是任何一维数据，通常是数值型的时序数据。
    - wavelet (str): 使用的小波类型。默认值为 'haar'，也可以选择其他小波类型，如 'db1', 'sym2', 'coif1', 'bior1.3' 等。
    - level (int): 小波分解的级别。默认值为 2，表示进行两级小波分解。
    
    返回:
    - transformed_data (dict): 包含变换结果的字典，字典键为：
        - "Approximation": 近似系数 (低频部分)
        - "Detail Level N": 各层细节系数 (高频部分)
    """
    
    # 使用指定的小波对数据进行分解
    coeffs = pywt.wavedec(data, wavelet, level=level)
    
    # 构建返回的字典，包含变换后的近似系数和细节系数
    transformed_data = {}
    transformed_data["Approximation"] = coeffs[0]  # 近似系数，表示低频部分
    
    # 细节系数
    for i in range(1, len(coeffs)):
        transformed_data[f"Detail Level {i}"] = coeffs[i]  # 每一层的细节系数
    
    return transformed_data

def cwt_transform(data, wavelet='cmor', scales=np.arange(1, 128)):
    """
    对输入数据进行连续小波变换（CWT），并返回变换结果。
    
    参数:
    - data (list or numpy array): 输入的时序数据。可以是任何一维数据，通常是数值型的时序数据。
    - wavelet (str): 使用的小波类型。默认值为 'cmor'（Morlet 小波）。
    - scales (numpy array): 小波变换的尺度。默认值为从 1 到 127 的范围，表示不同频率的分析。
    
    返回:
    - coefficients (numpy array): 小波系数，表示信号在不同尺度下的变换结果。
    - frequencies (numpy array): 对应的频率。
    """
    
    # 进行连续小波变换（CWT）
    coefficients, frequencies = pywt.cwt(data, scales, wavelet)
    
    # 返回变换结果
    return coefficients, frequencies
