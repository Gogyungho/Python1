import requests
import telegram

from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler #스케쥴러의 예제 코드에서 블러킹스케쥴러를 가져옴
 
token = '1294132162:AAEubt3TFHDBiobNsYCbHGbb-YTxdx76K40'
bot = telegram.Bot(token=token)

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200412'
def job_function():   #지속적으로 반복해야되는 작업을 함수로 선정해줌
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')
    if(imax):
        imax = imax.find_parent('div',class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id = 1158579057, text = title + ' IMAX 예매가 열렸습니다.')
        sched.pause()

sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds = 30)  #interval은 일정 간격마다 반복을 하겠다는 의미
sched.start() 

#앞서 말했던 IMAX가 열려도 메세지가 30초마다 계속해서 보내는 문제를 method를 사용해 멈출수 있다.
#scheduler의 pause를 사용하면 된다. 

#기본적인 영화 예매 알리미 완성 !.!