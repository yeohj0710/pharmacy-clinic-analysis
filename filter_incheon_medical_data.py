import pandas as pd
import math
from tqdm import tqdm


def haversine_distance(lat1, lon1, lat2, lon2):
    # 위도, 경도를 라디안 단위로 변환 후 두 점 사이의 거리를 계산 (단위: km)
    R = 6371  # 지구 반지름 (km)
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


# incheon_pharmacy_list.csv 파일과 incheon_clinic_list.csv 파일 읽기
pharmacy_df = pd.read_csv("incheon_pharmacy_list.csv")
clinic_df = pd.read_csv("incheon_clinic_list.csv")

# 각 약국에서 가장 가까운 의원/병원과의 거리 계산 (진행도 표시)
min_distances = []
for _, pharmacy in tqdm(
    pharmacy_df.iterrows(), total=len(pharmacy_df), desc="Processing Pharmacies"
):
    p_lat, p_lon = pharmacy["위도"], pharmacy["경도"]
    min_distance = float("inf")
    for _, clinic in clinic_df.iterrows():
        c_lat, c_lon = clinic["위도"], clinic["경도"]
        distance = haversine_distance(p_lat, p_lon, c_lat, c_lon)
        if distance < min_distance:
            min_distance = distance
    min_distances.append(min_distance)


# 계산한 최소 거리를 새로운 컬럼에 추가하고, 내림차순으로 정렬
pharmacy_df["가장 가까운 의원/병원까지의 거리(km)"] = min_distances
pharmacy_df = pharmacy_df.sort_values(
    "가장 가까운 의원/병원까지의 거리(km)", ascending=False
)

# 결과 CSV 파일 생성 (파일명: incheon_pharmacy_sorted_by_clinic_distance.csv)
pharmacy_df.to_csv(
    "incheon_pharmacy_sorted_by_clinic_distance.csv", index=False, encoding="utf-8-sig"
)
