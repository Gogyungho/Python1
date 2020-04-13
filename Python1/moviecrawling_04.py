import requests
import telegram

from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler #스케쥴러의 예제 코드에서 블러킹스케쥴러를 가져옴
 
token = '1294132162:AAEubt3TFHDBiobNsYCbHGbb-YTxdx76K40'
bot = telegram.Bot(token=token)
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200411'

def job_function():   #지속적으로 반복해야되는 작업을 함수로 선정해줌
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')
    if(imax):
        imax = imax.find_parent('div',class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id = 1158579057, text = title + ' IMAX 예매가 열렸습니다.')
    else:
        bot.sendMessage(chat_id = 1158579057, text = "IMAX 예매가 열리지 않았습니다.")

sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds = 30)  #interval로 일정 간격마다 반복을 하겠다.
sched.start()

#IMAX가 열려도 메세지를 계속해서 보내는 문제가 발생한다. 
#scheduler를 멈추는 방법은 method 하나로 간단하게 할수있다. 