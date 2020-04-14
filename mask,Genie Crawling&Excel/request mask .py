import requests  # 정보를 긁어오는데 필요한 requests 라이브러리를 가져옵니다.

gus = ['마포구', '용산구', '동작구', '노원구']

for gu in gus:
    url = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json?address=서울특별시 ' +gu

    # 입력한 주소로 가서 정보를 가져옵니다.
    r = requests.get(url)
    # 가져온 정보를 파이썬이 사용할 수 있도록 변경합니다. 
    rjson = r.json()
    stores = rjson['stores']

    for store in stores:
        try:  #try 안에있는 곳에서 에러가 발생하면 except문을 실행시키고 넘어가라
            if store['remain_stat'] == 'plenty':
                print(store['addr'], store['name'])
        except:
            # print(store['addr'], store['name'],'- ERROR !!!' )
            continue   #continue를 하게되면 에러는 출력을 안한다. 다음바퀴로 넘어가라는 뜻