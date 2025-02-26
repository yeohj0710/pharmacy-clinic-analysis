import pandas as pd

# CSV 파일 읽기
df = pd.read_csv("incheon_pharmacy_sorted_by_clinic_distance.csv")

# 거리(KM → M) 변환
df["가장 가까운 의원/병원까지의 거리(m)"] = (
    df["가장 가까운 의원/병원까지의 거리(km)"] * 1000
)

# 기존 KM 컬럼 삭제
df = df.drop(columns=["가장 가까운 의원/병원까지의 거리(km)"])

# 변환된 파일 저장
df.to_csv(
    "incheon_pharmacy_sorted_by_clinic_distance_meters.csv",
    index=False,
    encoding="utf-8-sig",
)
