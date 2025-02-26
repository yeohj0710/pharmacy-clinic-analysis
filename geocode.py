import requests
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()


def get_geocode(address: str):
    client_id = os.getenv("NAVER_CLIENT_ID")
    client_secret = os.getenv("NAVER_CLIENT_SECRET")

    if not client_id or not client_secret:
        raise ValueError("NAVER API Key가 설정되지 않았습니다. .env 파일을 확인하세요.")

    url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"

    params = {"query": address}
    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret,
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data.get("addresses"):
            result = data["addresses"][0]
            lat = result["y"]
            lon = result["x"]
            return lat, lon
        else:
            print("해당 주소에 대한 결과가 없습니다.")
            return None, None
    else:
        print(f"API 요청 실패: {response.status_code}, {response.text}")
        return None, None


if __name__ == "__main__":
    address = input("주소를 입력하세요: ")
    lat, lon = get_geocode(address)
    if lat and lon:
        print(f"위도: {lat}, 경도: {lon}")
    else:
        print("위도와 경도를 찾을 수 없습니다.")
