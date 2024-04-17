import pandas as pd
# Đọc dữ liệu từ tệp CSV
df = pd.read_csv("Product Data.csv")
# Loại bỏ các bản sao dựa trên cột "product name"
df = df.drop_duplicates(subset='product name')
# Hiển thị DataFrame sau khi loại bỏ các bản sao
print(df)