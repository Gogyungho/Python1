#예매 오픈된 IMAX영화 제목 크롤링 하기 

import requests
import telegram

from bs4 import BeautifulSoup

token = '1294132162:AAEubt3TFHDBiobNsYCbHGbb-YTxdx76K40'
bot = telegram.Bot(token=token)

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200411'
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')
imax = soup.select_one('span.imax')  


if(imax):
    imax = imax.find_parent('div',class_='col-times')
    title = imax.select_one('div.info-movie > a > strong').text.strip()
    bot.sendMessage(chat_id = 1158579057, text = title + ' IMAX 예매가 열렸습니다.')
    # print(title + ' IMAX 예매가 열렸습니다.')
else:
    bot.sendMessage(chat_id = 1158579057, text = "IMAX 예매가 열리지 않았습니다.")
    # print("IMAX 예매가 열리지 않았습니다.")

#텔레그램 봇을 연결해서 해당 날짜에 IMAX영화가 열렸는지 메세지를 보내준다.