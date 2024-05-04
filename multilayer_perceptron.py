import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import joblib
import os

#xây dựng đường dẫn tới file
current_dir = os.path.dirname(__file__)
csv_file_path = os.path.join(current_dir, 'zoo.csv')

# Đọc dữ liệu từ file CSV
data = pd.read_csv(csv_file_path)

# Chia dữ liệu thành features (đặc trưng) và labels (nhãn)
X = data.iloc[:, 1:-1]  # Lấy tất cả các cột trừ cột đầu tiên (tên) và cột cuối (nhãn)
y = data.iloc[:, -1]   # Lấy cột cuối cùng là nhãn
#Chia tập dữ liệu với 80% dữ liệu file gốc thành  train và 20% dữ liệu thành test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Xây dựng mô hình MLP - Multilayer Perceptron
mlp = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500, activation='relu', solver='adam', random_state=42)

# Huấn luyện mô hình trên tập huấn luyện (có cả back propagation)
mlp.fit(X_train_scaled, y_train)
#lưu mô hình đã huấn luyện vào file pkl
pkl_file_path = os.path.join(current_dir, 'multilayer_perceptron.pkl')
joblib.dump(mlp,pkl_file_path)
