import requests
from bs4 import BeautifulSoup
import smtplib
import time
re = requests.get('https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html')

    while True:
res = re.content

soup = BeautifulSoup(res, 'html.parser')

price = float(soup.find('p', class_ ='price_color').text[1:])


if price < 60:
    smt = smtplib.SMTP('smtp.gmail.com', 587)#street,door
    smt.ehlo()#hello
    smt.starttls()#securty no one is listening
    smt.login('Sender', 'apppassword')
    smt.sendmail('sender',
                'reciver',
                f'Subject: Price Notifier\n\nHi, price has droped to {price}. Buy it!')
    smt.quit()

    time.sleep(24*60*60)