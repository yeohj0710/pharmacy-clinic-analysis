import pandas as pd
import time
from raw_data.geocode import get_geocode


def process_csv(input_file: str, output_file: str):
    df = pd.read_csv(input_file)

    # 홈페이지 컬럼이 결측값이면 빈 문자열로 채움
    df["홈페이지"] = df["홈페이지"].fillna("")

    lat_list = []
    lon_list = []
    total = len(df)

    for i, row in df.iterrows():
        address = row["소재지주소"]
        lat, lon = get_geocode(address)
        lat_list.append(lat)
        lon_list.append(lon)

        if (i + 1) % 100 == 0:
            print(f"{i + 1}/{total} rows processed")

        # API 호출 속도 제한을 고려하여 약간의 딜레이 추가
        time.sleep(0.1)

    df["위도"] = lat_list
    df["경도"] = lon_list

    df.to_csv(output_file, index=False, encoding="utf-8-sig")
    print(f"변환 완료! 결과 파일: {output_file}")


if __name__ == "__main__":
    process_csv("incheon_list.csv", "incheon_list_with_geo.csv")
