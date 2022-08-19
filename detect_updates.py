from email import message
import requests
import smtplib
import schedule
from bs4 import BeautifulSoup
from time import sleep
from email.mime.text import MIMEText
from email.utils import formatdate

countSoya = 0
countRumoi = 0
countKamikawa = 0
countOhotsuku = 0
countNemuro = 0
countKushiro = 0
countTokachi = 0
couuntHidaka = 0
countSorachi = 0
countIshikari = 0
countIburi = 0
countShiribeshi = 0
countHiyama1 = 0
countHiyama2 = 0
countOshima = 0

def detect_updates():
    url = 'https://teiden-info.hepco.co.jp/teiden_top.html'
    res = requests.get(url)

    soup = BeautifulSoup(res.content, 'html.parser')
    soya = {(str(soup.select("#soya")))}
    rumoi= {(str(soup.select("#rumoi")))}
    kamikawa = {(str(soup.select("#kamikawa")))}
    ohotsuku = {(str(soup.select("#ohotsuku")))}
    nemuro = {(str(soup.select("#nemuro")))}
    kushiro = {(str(soup.select("#kushiro")))}
    tokachi = {(str(soup.select("#tokachi")))}
    hidaka = {(str(soup.select("#hidaka")))}
    sorachi = {(str(soup.select("#sorachi")))}
    ishikari = {(str(soup.select("#ishikari")))}
    iburi = {(str(soup.select("#iburi")))}
    shiribeshi = {(str(soup.select("#shiribeshi")))}
    hiyama1 = {(str(soup.select("#hiyama")))}
    hiyama2 = {(str(soup.select("#hiyama2")))}
    oshima = {(str(soup.select("#oshima")))}

    with open("soya.txt") as f:
        teidenSoya = f.read()
    
    with open("rumoi.txt") as f:
        teidenRumoi = f.read()
    
    with open("kamikawa.txt") as f:
        teidenKamikawa = f.read()
    
    with open("ohotsuku.txt") as f:
        teidenOhotsuku = f.read()
    
    with open("nemuro.txt") as f:
        teidenNemuro = f.read()

    with open("kushiro.txt") as f:
        teidenKushiro = f.read()
    
    with open("tokachi.txt") as f:
        teidenTokachi = f.read()
    
    with open("hidaka.txt") as f:
        teidenHidaka = f.read()
    
    with open("sorachi.txt") as f:
        teidenSorachi = f.read()
    
    with open("ishikari.txt") as f:
        teidenIshikari = f.read()

    with open("iburi.txt") as f:
        teidenIburi = f.read()
    
    with open("shiribeshi.txt") as f:
        teidenShiribeshi = f.read()

    with open("hiyama1.txt") as f:
        teidenHiyama1 = f.read()

    with open("hiyama2.txt") as f:
        teidenHiyama2 = f.read()

    with open("oshima.txt") as f:
        teidenOshima = f.read()        

    if str(soya) == teidenSoya:
            global countSoya
            countSoya = 0
    else:
        if countSoya == 0:
            send_mail("宗谷地方で停電発生")
            countSoya = countSoya + 1
        else:
            pass

    if str(rumoi) == teidenRumoi:
            global countRumoi
            countRumoi = 0
    else:
        if countRumoi == 0:
            send_mail("留萌地方で停電発生")
            countRumoi = countRumoi + 1
        else:
            pass

    if str(kamikawa) == teidenKamikawa:
            global countKamikawa
            countKamikawa = 0
    else:
        if countKamikawa == 0:
            send_mail("上川地方で停電発生")
            countKamikawa = countKamikawa + 1
        else:
            pass

    if str(ohotsuku) == teidenOhotsuku:
            global countOhotsuku
            countOhotsuku = 0
    else:
        if countOhotsuku == 0:
            send_mail("オホーツク地方で停電発生")
            countOhotsuku = countOhotsuku + 1
        else:
            pass

    if str(nemuro) == teidenNemuro:
            global countNemuro
            countNemuro = 0
    else:
        if countNemuro == 0:
            send_mail("根室地方で停電発生")
            countNemuro = countNemuro + 1
        else:
            pass

    if str(kushiro) == teidenKushiro:
            global countKushiro
            countKushiro = 0
    else:
        if countKushiro == 0:
            send_mail("釧路地方で停電発生")
            countKushiro = countKushiro + 1
        else:
            pass

    if str(tokachi) == teidenTokachi:
            global countTokachi
            countTokachi = 0
    else:
        if countTokachi == 0:
            send_mail("十勝地方で停電発生")
            countTokachi = countTokachi + 1
        else:
            pass

    if str(hidaka) == teidenHidaka:
            global countHidaka
            countHidaka = 0
    else:
        if countHidaka == 0:
            send_mail("日高地方で停電発生")
            countHidaka = countHidaka + 1
        else:
            pass

    if str(sorachi) == teidenSorachi:
            global countSorachi
            countSorachi = 0
    else:
        if countSorachi == 0:
            send_mail("空知地方で停電発生")
            countSorachi = countSorachi + 1
        else:
            pass

    if str(ishikari) == teidenIshikari:
            global countIshikari
            countIshikari = 0
    else:
        if countIshikari == 0:
            send_mail("石狩地方で停電発生")
            countIshikari = countIshikari + 1
        else:
            pass

    if str(iburi) == teidenIburi:
            global countIburi
            countIburi = 0
    else:
        if countIburi == 0:
            send_mail("胆振地方で停電発生")
            countIburi = countIburi + 1
        else:
            pass

    if str(shiribeshi) == teidenShiribeshi:
            global countShiribeshi
            countShiribeshi = 0
    else:
        if countShiribeshi == 0:
            send_mail("後志地方で停電発生")
            countShiribeshi = countShiribeshi + 1
        else:
            pass

    if str(hiyama1) == teidenHiyama1:
            global countHiyama1
            countHiyama1 = 0
    else:
        if countHiyama1 == 0:
            send_mail("檜山地方で停電発生")
            countHiyama1 = countHiyama1 + 1
        else:
            pass

    if str(hiyama2) == teidenHiyama2:
            global countHiyama2
            countHiyama2 = 0
    else:
        if countHiyama2 == 0:
            send_mail("檜山地方で停電発生")
            countHiyama2 = countHiyama2 + 1
        else:
            pass

    if str(oshima) == teidenOshima:
            global countOshima
            countOshima = 0
    else:
        if countOshima == 0:
            send_mail("渡島地方で停電発生")
            countOshima = countOshima + 1
        else:
            pass


def send_mail(props):
    sendAddress = 'dge8g1210@gmail.com'
    password = 'phnjiganpajeiaxi'

    subject = '停電発生テスト２'
    bodyText = props
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
    
schedule.every(2).seconds.do(detect_updates)

while True:
    schedule.run_pending()
    sleep(1)