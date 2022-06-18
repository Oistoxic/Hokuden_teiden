import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

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

send_mail()