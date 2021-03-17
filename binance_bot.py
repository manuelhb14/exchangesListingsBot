from tweepy import OAuthHandler, Stream, StreamListener
import requests
import json
from pycoingecko import CoinGeckoAPI
import urllib.parse
import keys
import data_processing

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
            json_data,tweet,date,user,text,isBinance = data_processing.basic_info(data)
            print("basic tweet info...")
            print(json_data)
            print(date)
            print("from: " + str(user) + " isBinance: " + str(isBinance))
            if ("list" in tweet):
                coin_symbol = data_processing.coin_data(json_data)
                print("list keyword found")
                print(coin_symbol)    
                for coin in coinlist:
                    if ((coin['symbol']==coin_symbol) and isBinance):
                        coin_id = coin["id"]
                        coin_data = cg.get_coin_by_id(coin_id)
                        print("symbol found in coingecko")
                        contract_address_eth = coin_data["platforms"]['ethereum']
                        # contract_address_bsc = coin_data["platforms"]['ethereum']
                        coin_price = coin_data["market_data"]["current_price"]["usd"]
                        print(contract_address_eth)
                        print(coin_price)
                        telegram_bot_sendtext("{}\n{}\n{} {}\nContract address:\n{}\nPrice atm: {}\nUniswap link: {}".format(date[:-10],urllib.parse.quote_plus(text),coin_id.capitalize(),coin_symbol.upper(),contract_address_eth,str(coin_price),"https%3A%2F%2Fapp.uniswap.org%2F%23%2Fswap%3FoutputCurrency%3D"+contract_address_eth))
                        print("telegram sent")
                        return True
                print("Not from Binance account")
            elif (isBinance==True):
                print("Error here")
                text = json_data["text"]
                telegram_bot_sendtext("{}\n{}".format(date[:-10],urllib.parse.quote_plus(text)))                        
            else:
                print("list keyword not found")
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
        stream.filter(follow=['877807935493033984,829941007076687872'])
    except Exception as e:
        print(e)
        pass