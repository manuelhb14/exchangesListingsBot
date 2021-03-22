import urllib.request as rq
from hashlib import sha1
from bs4 import BeautifulSoup
import json 
import time


current_webpage = rq.urlopen('https://www.binance.com/en/support/announcement/c-48').read()
soup = BeautifulSoup(current_webpage,'lxml')
current_data = json.loads(soup.find('script', id='__APP_DATA').string)['routeProps']['b723']['data']['catalogs'][0]['articles'][0]['title']
print("running") 
time.sleep(5)
while True:
    try: 
        new_webpage = rq.urlopen('https://www.binance.com/en/support/announcement/c-48').read()
        soup = BeautifulSoup(new_webpage,'lxml')
        new_data = json.loads(soup.find('script', id='__APP_DATA').string)['routeProps']['b723']['data']['catalogs'][0]['articles'][0]['title']
        
        if (new_data==current_data):
            print("===")
            time.sleep(5)
            continue
        else:
            print(new_data)
            break
    except Exception as e: 
        print("error") 
