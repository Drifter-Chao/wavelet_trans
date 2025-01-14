# src/preprocess.py
import pandas as pd

def load_data(file):
    """
    加载上传的 CSV 数据文件。
    """
    df = pd.read_csv(file)
    return df