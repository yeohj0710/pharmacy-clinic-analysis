# pharmacy clinic analysis

### 개요

- 약국, 병/의원 위치 데이터 분석 코드

### 데이터 가공 과정

- 약국, 병/의원 주소 데이터
  - 건강보험심사평가원의 병원, 약국 찾기 기능 이용
    - 검색 결과를 반영한 엑셀 파일을 제공

### 코드 설명

- geocode.py
  - 주소를 입력받아, 네이버 API를 이용해 위도와 경도를 반환
- add_geocode_to_csv.py
  - 건강보험심사평가원의 병원, 약국 데이터에 위도와 경도를 추가
- filter_medical_data.py
  - `*_list_with_geo.csv`를 약국 데이터와 병/의원 데이터로 분리
- fix_csv_encoding.py
  - 한글이 깨지는 csv 파일을 한글이 깨지지 않는 인코딩으로 설정
- convert_distanc_to_meters.py
  - 거리 데이터가 km 단위인 경우 m 단위로 변경
- calculate_pharmacy_distance.py
  - **각 약국들로부터 가장 가까운 병/의원의 거리를 구하고, 내림차순으로 정렬**

### 파일 설명

- incheon_list.csv
  - 인천광역시의 모든 약국, 병/의원 데이터
- incheon_list_with_geo.csv
  - 인천광역시의 모든 약국, 병/의원 데이터 + 위도/경도
- incheon_pharmacy_list.csv
  - 인천광역시의 모든 약국 데이터 + 위도/경도
- incheon_clinic_list.csv
  - 인천광역시의 모든 의원, 치과의원 데이터 + 위도/경도
- 인천광역시 약국 근처 의원 거리순 정렬.xlsx

  - 최종적으로 약국들을, 가장 가까운 의원까지의 거리를 기준으로 정렬한 데이터

- seoul_list.csv
  - 서울특별시의 모든 약국, 병/의원 데이터
- seoul_list_with_geo.csv
  - 서울특별시의 모든 약국, 병/의원 데이터 + 위도/경도
- seoul_pharmacy_list.csv
  - 서울특별시의 모든 약국 데이터 + 위도/경도
- seoul_clinic_list.csv
  - 서울특별시의 모든 의원, 치과의원 데이터 + 위도/경도
- 서울특별시 약국 근처 의원 거리순 정렬.xlsx
  - 최종적으로 약국들을, 가장 가까운 의원까지의 거리를 기준으로 정렬한 데이터
