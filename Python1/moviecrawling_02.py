#예매 오픈된 IMAX영화 제목 크롤링 하기 

import requests

from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200411'
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')
imax = soup.select_one('span.imax')


if(imax):
    imax = imax.find_parent('div',class_='col-times')
    title = imax.select_one('div.info-movie > a > strong').text.strip()
    print(title + ' IMAX 예매가 열렸습니다.')
else:
    print("IMAX 예매가 열리지 않았습니다.")


    #해당 날짜를 크롤링해서 영화 제목과 함께 예매가 열렸는지 아닌지 메세지가 뜬다.