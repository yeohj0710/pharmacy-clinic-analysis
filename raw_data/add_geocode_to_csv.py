import pandas as pd
import time
import os
from raw_data.geocode import get_geocode


def process_csv(input_file: str, output_file: str):
    try:
        df = pd.read_csv(input_file, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(input_file, encoding="cp949")

    df["홈페이지"] = df["홈페이지"].fillna("")

    file_exists = os.path.exists(output_file)

    if file_exists:
        df_existing = pd.read_csv(output_file)
        if "위도" in df_existing.columns and "경도" in df_existing.columns:
            df["위도"] = df_existing["위도"]
            df["경도"] = df_existing["경도"]
        else:
            df["위도"] = None
            df["경도"] = None
    else:
        df["위도"] = None
        df["경도"] = None

    total = len(df)

    for i, row in df.iterrows():

        if pd.notna(row["위도"]) and row["위도"] != "":
            continue

        address = row["소재지주소"]
        attempts = 0
        lat, lon = None, None

        while attempts < 5:
            lat, lon = get_geocode(address)
            if lat is not None and lon is not None and lat != "" and lon != "":
                break
            attempts += 1
            time.sleep(0.1)

        df.at[i, "위도"] = lat
        df.at[i, "경도"] = lon

        if file_exists:
            print(f"Row {i}: Address '{address}', obtained lat: {lat}, lon: {lon}")

        if (i + 1) % 100 == 0:
            df.to_csv(output_file, index=False, encoding="utf-8-sig")
            print(f"{i + 1}/{total} rows processed and saved.")

        time.sleep(0.1)

    df = df[
        (df["위도"].notna())
        & (df["위도"] != "")
        & (df["경도"].notna())
        & (df["경도"] != "")
    ]
    df.to_csv(output_file, index=False, encoding="utf-8-sig")

    print(f"변환 완료! 결과 파일: {output_file}")


if __name__ == "__main__":
    process_csv("seoul_list.csv", "seoul_list_with_geo.csv")
