from tweepy import OAuthHandler, Stream, StreamListener
import requests
import json
import builtins
from pycoingecko import CoinGeckoAPI

import keys
import duplicates

cg = CoinGeckoAPI()
coinlist = cg.get_coins_list()
consumer_key=keys.consumer_key
consumer_secret=keys.consumer_secret
access_token=keys.access_token
access_token_secret=keys.access_token_secret

def telegram_bot_sendtext(bot_message):
    
    bot_token = keys.bot_token
    bot_chatID = keys.bot_chatID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)

    return response.json()

class StdOutListener(StreamListener):
    def on_data(self, data):
        try:
            print(data)
            json_data = json.loads(data)
            tweet = json_data['text'].lower().strip
            date = json_data['created_at']
            print(tweet)
            if ("listing" in tweet):
                print("listing keyword found")
                coin_symbol = json_data["entities"]['symbols'][0]['text'].lower()
                print(coin_symbol)
                for coin in coinlist:
                    if (coin['symbol'] == coin_symbol):
                        print("symbol found in coingecko")
                        coin_id = coin["id"]
                        telegram_bot_sendtext("{}\n{}\n{} {}".format(tweet,date[:-10],coin_id.capitalize(),coin_symbol.upper()))
                        print("telegram sent")
                        return True
        except Exception as e:
            print(e)
            pass

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    try:
        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        stream = Stream(auth, l)
        stream.filter(follow=['829941007076687872'])
    except Exception as e:
        print(e)
        pass