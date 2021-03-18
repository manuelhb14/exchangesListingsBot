from sys import platform
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
    print(i)
    print(i['links']['twitter_screen_name'])
    if ('ethereum' in i['platforms']):
        print('https%3A%2F%2Fapp.uniswap.org%2F%23%2Fswap%3FoutputCurrency%3D' + i['platforms']['ethereum'] + '\n')
    if ('binance-smart-chain' in i['platforms']):
        print('https%3A%2F%2Fexchange.pancakeswap.finance%2F%23%2Fswap%3FoutputCurrency%3D' + i['platforms']['binance-smart-chain'])

# contract_address_bsc = contract_address
# coin_price = contract_address['market_data']['current_price']['usd']
# print(contract_address_bsc)