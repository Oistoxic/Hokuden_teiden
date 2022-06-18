from bs4 import BeautifulSoup
import requests
import send_mail

def detect_updates():
    url = 'https://192.168.128.180:3000'
    res = requests.get(url, verify=False)

    soup = BeautifulSoup(res.text, 'html.parser')
    new_elem = str(soup.select('.root'))

    try:
        with open('old_elem.txt') as f:
          old_elem = f.read()
    except:
          old_elem = ''

    if new_elem == old_elem:
        print('変化なし')
        return False
    else:
        with open('old_elem.txt', 'w') as f:
            f.write(new_elem)
        print('Webページが更新されました')
        send_mail.send_mail
        return True

detect_updates()