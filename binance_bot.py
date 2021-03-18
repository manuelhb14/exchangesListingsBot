from tweepy import OAuthHandler, Stream, StreamListener
import requests
import json
from pycoingecko import CoinGeckoAPI
import urllib.parse
import keys
import data_processing
import coin_details

cg = CoinGeckoAPI()
coinlist = cg.get_coins_list()[1:]

def telegram_bot_sendtext(bot_message):
    
    bot_token = keys.bot_token
    bot_chatID = keys.bot_chatID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)

    return response.json()

class StdOutListener(StreamListener):
    def on_data(self, data):
        try:
            print("basic tweet info...")
            json_data,tweet,date,user,text,isBinance = data_processing.basic_info(data)
            print("from: " + str(user) + " isBinance: " + str(isBinance))
            if ("list" in tweet):
                coin_symbol,coin_twitter = data_processing.coin_data(json_data)
                print("list keyword found")
                print(coin_symbol)
                if (isBinance):
                    info,platform,price = coin_details.coingecko_info(cg, coinlist, coin_symbol, coin_twitter)
                    contracts = coin_details.uni_pancake_link(platform)
                    telegram_bot_sendtext("{}\n{}\n{} {}\nPrice atm: {}\nExchanges links:\n{}".format(date[:-10],urllib.parse.quote_plus(text),info['name'],coin_symbol.upper(),str(price),contracts))
                    print("telegram sent")
                    return True
                else:
                    print("Not from Binance account")                      
            else:
                ("list keyword not found, sending telegram with binance tweet...")
                telegram_bot_sendtext("{}\n{}".format(date[:-10],urllib.parse.quote_plus(text)))  
            print("")
        except Exception as e:
            print(e)
            pass

    def on_error(self, status):
        print(status)
        return True

if __name__ == '__main__':
    try:
        l = StdOutListener()
        auth = OAuthHandler(keys.consumer_key, keys.consumer_secret)
        auth.set_access_token(keys.access_token, keys.access_token_secret)

        stream = Stream(auth, l)
        stream.filter(follow=['877807935493033984'])
        #877807935493033984
        #829941007076687872

    except Exception as e:
        print(e)
        pass