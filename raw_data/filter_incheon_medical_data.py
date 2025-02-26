import pandas as pd

df = pd.read_csv("incheon_list_with_geo.csv")

df_pharmacy = df[df["병원/약국구분"] == "약국"][
    ["NO", "병원/약국명", "소재지주소", "위도", "경도"]
]
df_pharmacy = df_pharmacy.rename(columns={"NO": "id", "병원/약국명": "이름"})
df_pharmacy.to_csv("incheon_pharmacy_list.csv", index=False)

categories = ["의원", "병원", "치과의원", "치과병원"]
df_clinic = df[df["병원/약국구분"].isin(categories)][
    ["NO", "병원/약국명", "소재지주소", "위도", "경도"]
]
df_clinic = df_clinic.rename(columns={"NO": "id", "병원/약국명": "이름"})
df_clinic.to_csv("incheon_clinic_list.csv", index=False)
