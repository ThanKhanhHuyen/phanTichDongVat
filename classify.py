import pandas as pd
import numpy as np
import joblib
import os

# Hàm phân loại
def classify(input):
    # Đọc mô hình MLP từ file
    current_dir = os.path.dirname(__file__)
    pkl_file_path = os.path.join(current_dir, 'multilayer_perceptron.pkl')
    mlp_model = joblib.load(pkl_file_path)

    # Phân loại nhãn của dữ liệu mới sử dụng mô hình đã được đọc từ file
    classification = mlp_model.predict([input])

    # In kết quả 
    return classification