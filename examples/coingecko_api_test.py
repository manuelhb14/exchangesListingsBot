from pycoingecko import CoinGeckoAPI
from requests import adapters
cg = CoinGeckoAPI()
coinlist = cg.get_coins_list()

coins_info = []
coins_details = []
coins_contract_address = []
con_num = 0
coin_symbol = 'super'

while con_num<len(coinlist):
    if coinlist[con_num]['symbol'] == coin_symbol:
        coins_info.append(coinlist[con_num])
    con_num+=1

for i in coins_info:
    coins_details.append(cg.get_coin_by_id(i['id']))

for i in coins_details:
    print(i["links"]["twitter_screen_name"])
    print(i["platforms"])

# contract_address_bsc = contract_address
# coin_price = contract_address["market_data"]["current_price"]["usd"]
# print(contract_address_bsc)