from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

coinlist = cg.get_coins_list()
print(len(coinlist))
print(coinlist[0])

print(cg.get_price(ids=[coinlist[0]['id']], vs_currencies='usd'))
fiat_currencies = cg.get_supported_vs_currencies()
for i in fiat_currencies:
    print(i, end=', ')