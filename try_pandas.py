import pandas as pd


# อ่านข้อมูลจากไฟล์ CSV
df = pd.read_csv("datasets/1642645053.csv", encoding="tis-620")
print(df.head(10))