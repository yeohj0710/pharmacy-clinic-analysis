import pandas as pd

file_name = "raw_data/incheon_pharmacy_list.csv"

# 깨진 CSV 파일 불러오기 (예: 기본 UTF-8로 저장된 파일)
df = pd.read_csv(file_name, encoding="utf-8")

# 한글이 깨지지 않도록 새로운 파일로 저장
df.to_csv(
    file_name,
    index=False,
    encoding="utf-8-sig",
)
