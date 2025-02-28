import pandas as pd

df = pd.read_csv("seoul_list_with_geo.csv")

df_pharmacy = df[df["병원/약국구분"] == "약국"][
    ["NO", "병원/약국명", "소재지주소", "위도", "경도"]
]
df_pharmacy = df_pharmacy.rename(columns={"NO": "id", "병원/약국명": "이름"})
df_pharmacy.to_csv("seoul_pharmacy_list.csv", index=False)

df_non_pharmacy = df[df["병원/약국구분"] != "약국"][
    ["NO", "병원/약국명", "소재지주소", "위도", "경도"]
]
df_non_pharmacy = df_non_pharmacy.rename(columns={"NO": "id", "병원/약국명": "이름"})
df_non_pharmacy.to_csv("seoul_clinic_list.csv", index=False)
