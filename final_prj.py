import os
import sys
import urllib.request
import datetime
import time
import json
import pandas as pd

ServiceKey = "0a22f0d1987342ce8610103624245be9"         #인증키

#%% #[code1]
def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
            print(e)
            print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
            return None
        
#%% #[code2]
def getTourismStatsItem(yyyymm, national_code):
    service_url = "https://openapi.gg.go.kr/LINEBUSANULUSERCNTKEY=0a22f0d1987342ce8610103624245be9"


#%% #[code0]
def main():
    jsonResult = []
    result = []
    
    print("<< 경기도의 노선별 버스 이용객수 데이터를 수집합니다. >>")
    nat_cd = input('지역 코드를 입력하세요: ')
    nStartYear = int(input('데이터를 몇 년부터 수집할까요? : '))
    nEndYear = int(input('데이터를 몇 년까지 수집할까요? : '))
    
    jsonResult, result, natName, dataEND = getBusStatsService(nat_cd, nStartYear, nEndYear)
    
    #파일 저장: json 파일
    with open(' ./%s_%s_%d_%s.json' % (natName, nStartYear, dataEND), 'w', encoding='utf8') as outfile:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys = True, ensure_ascii=False)
        outfile.write(jsonFile)
        
    #파일 저장: csv 파일
    columns = ["지역명", "지역코드", "연월", "이용객 수"]
    result_df = pd.DataFrame(result, columns = columns)
    result_df.to_csv(' ./%s_%s_%d_%s.csv' % (natName, nStartYear, dataEND), index=False, encoding='cp949')
    
    