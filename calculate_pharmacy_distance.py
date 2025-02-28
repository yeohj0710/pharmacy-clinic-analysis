import pandas as pd
import numpy as np


def haversine_np(lat1, lon1, lat2, lon2):
    """
    단일 지점(lat1, lon1)과 여러 지점(lat2, lon2 배열) 사이의 대원거리(미터 단위)를 계산합니다.
    모든 입력은 도(degree) 단위이며, 반환값은 미터(m)입니다.
    """
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    R = 6371000
    return R * c


def main():
    pharmacy_df = pd.read_csv("seoul_pharmacy_list.csv")
    clinic_df = pd.read_csv("seoul_clinic_list.csv")

    clinic_lats = clinic_df["위도"].values
    clinic_lons = clinic_df["경도"].values

    closest_distances = []
    total = len(pharmacy_df)
    for idx, row in pharmacy_df.iterrows():
        ph_lat = row["위도"]
        ph_lon = row["경도"]
        dists = haversine_np(ph_lat, ph_lon, clinic_lats, clinic_lats * 0 + clinic_lons)
        min_dist = dists.min()
        closest_distances.append(min_dist)
        if (idx + 1) % 10 == 0 or (idx + 1) == total:
            print(f"Progress: {idx + 1}/{total} rows processed.")

    pharmacy_df["가장 가까운 의원까지의 거리"] = closest_distances

    pharmacy_df = pharmacy_df.sort_values(
        "가장 가까운 의원까지의 거리", ascending=False
    )

    pharmacy_df.to_csv(
        "seoul_pharmacy_sorted_by_clinic_distance.csv",
        index=False,
        encoding="utf-8-sig",
    )
    print("CSV 파일 생성 완료: seoul_pharmacy_sorted_by_clinic_distance.csv")


if __name__ == "__main__":
    main()
