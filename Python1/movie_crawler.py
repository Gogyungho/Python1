#IMAX 영화 예매 오픈 여부 크롤링 하기 

import requests
from bs4 import BeautifulSoup


url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200411'
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')
imax = soup.select_one('span.imax')  #영화 하나의 요소를 가져오기 때문에 select_one이 된다. 

if(imax):
    print("IMAX 예매가 열렸습니다.")
else:
    print("IMAX 예매가 열리지 않았습니다.")


    #해당 영화를 크롤링해서 단순히 예매가 열렸는지 아닌지 메세지가 뜬다. 