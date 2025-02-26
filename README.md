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
- filter_incheon_medical_data.py
  - `incheon_list_with_geo.csv`를 약국 데이터와 병/의원 데이터로 분리
    - 약국, 의원, 치과의원, 병원, 치과병원만 포함

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
