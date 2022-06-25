import requests
import smtplib
import schedule
from bs4 import BeautifulSoup
from time import sleep
from email.mime.text import MIMEText
from email.utils import formatdate

def detect_updates():
    url = 'https://teiden-info.hepco.co.jp/teiden_top.html'
    res = requests.get(url)

    soup = BeautifulSoup(res.content, 'html.parser')
    new_elem = str(soup.select(".bg_box.opt_blue.mb_20.font_bold"))

    try:
        with open("old_elem.txt") as f:
            old_elem = f.read()
    except:
        old_elem = ""

    if new_elem == old_elem:
        print("地震なし")
    else:
        send_mail()

def send_mail():
    sendAddress = 'dge8g1210@gmail.com'
    password = 'phnjiganpajeiaxi'

    subject = '停電発生テスト２'
    bodyText = '停電が発生しました'
    fromAddress = 'dge8g1210@gmail.com'
    toAddress = 'dge8g1210@gmail.com'

    # SMTPサーバに接続
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.starttls()
    smtpobj.login(sendAddress, password)

    # メール作成
    msg = MIMEText(bodyText)
    msg['Subject'] = subject
    msg['From'] = fromAddress
    msg['To'] = toAddress
    msg['Date'] = formatdate()

    # 作成したメールを送信
    smtpobj.send_message(msg)
    smtpobj.close()

def hoge():
    print("hogehoge")

schedule.every(2).seconds.do(detect_updates)

while True:
    schedule.run_pending()
    sleep(1)