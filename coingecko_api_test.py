from pycoingecko import CoinGeckoAPI
from requests import adapters
cg = CoinGeckoAPI()

coinlist = cg.get_coins_list()
# print(len(coinlist))
coin_symbol = 'matic'
for i in coinlist:
    if i['symbol'] == coin_symbol:
        coin_info = i
        print(coin_info)
contract_address = cg.get_coin_by_id(coin_info['id'])
print(contract_address.keys())
for key in contract_address.keys():
    print(contract_address[key])

# seen = {}
# dupes = []

# for x in coinlist:
#     if x['symbol'] not in seen:
#         seen[x['symbol']] = 1
#     else:
#         if seen[x['symbol']] == 1:
#             dupes.append(x)
#         seen[x['symbol']] += 1
# print('\nlist of duplicated ids')
# for i in dupes:
#     print(i['symbol'],  end='', '')
# print()