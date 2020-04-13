import telegram

bot = telegram.Bot(token='AAHNgYhpUyQfSbJmOlRxRrsT9_YOMutqxjM')

for i in bot.getUpdates():
     print(i.message)  

#봇에 메세지 보내는 방법 
#id = 1158579057

#그렇게 얻은 id를 이용해 봇에 메세지를 보낼수있다. 
#bot.sendMessage(chat_id = 1158579057, text = '테스트 입니다. ')