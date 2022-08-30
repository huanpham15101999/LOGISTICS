import gspread
import datetime
import requests

def str2datetime(str):
    return datetime.datetime.strptime(str,'%d/%m/%Y')  # chuyen string thanh datetime

def telegram_bot_sendtext(bot_message):
    bot_token = '5461923197:AAGktSwN_8mBRJ7ZHbedhAw0NCRFSgRPScw'
    bot_chatID = '-712986951'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

sa = gspread.service_account()
sh = sa.open("MAYA 'S JOB")
wks = sh.worksheet("Sheet 1")

for i in range(2,6):
    end = wks.acell('G' + str(i)).value
    if end is not None: 
        warn = str2datetime(end) - datetime.timedelta(days=1)
        
        if datetime.datetime.now() > warn and datetime.datetime.now() < str2datetime(end):
            telegram_bot_sendtext(u'\U0001F525' + " Hey Maya, ngày mai (" + end + ") đơn hàng " + wks.acell('D' + str(i)).value + " của " + wks.acell('H' + str(i)).value + " sẽ đến" )

# chay crontab: */2 * * * * /usr/bin/python3 /home/huan/test.py
