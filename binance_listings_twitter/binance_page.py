import urllib.request as rq
from hashlib import sha1
from bs4 import BeautifulSoup
import json 
import time
import data_processing


current_webpage = rq.urlopen('https://www.binance.com/en/support/announcement/c-48').read()
soup = BeautifulSoup(current_webpage,'lxml')
current_data = json.loads(soup.find('script', id='__APP_DATA').string)['routeProps']['b723']['data']['catalogs'][0]['articles'][0]['title']
print("running") 
time.sleep(5)
while True:
    # try: 
        new_webpage = rq.urlopen('https://www.binance.com/en/support/announcement/c-48').read()
        soup = BeautifulSoup(new_webpage,'lxml')
        new_data = json.loads(soup.find('script', id='__APP_DATA').string)['routeProps']['b723']['data']['catalogs'][0]['articles'][2]['title']
        if (new_data==current_data):
            print("===")
            time.sleep(5)
            continue
        else:
            if "innovation" in new_data:
                data_processing.coin_data_webpage(new_data)
                # info,platform,price = coin_details.coingecko_info(cg, coinlist, coin_symbol, coin_twitter)
                # contracts = coin_details.uni_cake_link(platform)
                # cg_link = urllib.parse.quote_plus("https://coingecko.com/en/coins/" + info['name'].lower().replace(' ','-').replace('.','-'))
                # cmc_link = urllib.parse.quote_plus("https://coinmarketcap.com/currencies/" + info['name'].lower().replace(' ','-').replace('.','-'))
                # telegram_bot_sendtext("{}\n{}\n{} {}\nPrice atm: {}\nCoinGecko: {}\nCoinMarketCap: {}\nExchanges links:\n{}".format(date[:-10],urllib.parse.quote_plus(text),info['name'],coin_symbol.upper(),str(price),cg_link,cmc_link,contracts))
                # print("telegram sent")
    #         break
    # except Exception as e: 
    #     print("error")    
