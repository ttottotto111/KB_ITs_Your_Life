import pandas as pd
import numpy as np

def get_weather_info(year,month=None):
    '''year, month의 날씨를 크롤링해서 반환.
    '''
    pass
    if month == None:
        start_month = 1
        end_month = 13
    else:
        start_month = month
        end_month = month + 1

    import time

    #날짜별 날씨 저장용
    weathers = [] 

    for month in range(start_month, end_month):
        time.sleep(0.5)
        url=f"https://www.weatheri.co.kr/bygone/pastDB_tmp.php?jijum_id=108&start={year}-{month}-01&end={year}-12-31"
        print(url)

        weather = pd.read_html( url )

        w = weather[3]
        w.columns = w.loc[0,:]
        w = w[["날짜","날씨"]]
        w.drop(0, axis=0,inplace=True)

        def get_date(x):
            return x[0:4] + x[6:8] + x[9:11]

        w.loc[ : , "날짜"] = w["날짜"].apply( get_date )
#         display(w.head())
        weathers.append(w)
    # 추출한 날씨를 하나로 합치기
    w_all = weathers[0]
    for i in weathers[1:]:
        w_all = pd.concat([w_all, i], ignore_index=True)
    return w_all

if __name__ == "__main__":
    #테스트코드실행
    print(get_weather_info(2021, 3))