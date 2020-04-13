#기본적인 bs4의 사용법

import requests
from bs4 import BeautifulSoup


url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200412'
html = requests.get(url)
#print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')
#print(soup.select_one('body > div > div.sect-showtimes > ul > li:nth-child(1) > div > div.info-movie > a > strong'))

title_list = soup.select('div.info-movie')

for i in title_list:
    print(i.select_one('a > strong').text.strip())  #text만 가져오고, strip로 글자의 공백 제거


    #해당 날짜의 상영 영화 제목만 크롤링해서 띄어준다.