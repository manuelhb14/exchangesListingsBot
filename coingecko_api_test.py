from pycoingecko import CoinGeckoAPI
from requests import adapters
cg = CoinGeckoAPI()

coinlist = cg.get_coins_list()
print(len(coinlist))
print(coinlist[0])
coin_symbol = "ada"
for i in coinlist:
    if i["symbol"] == coin_symbol:
        print(i["id"])

seen = {}
dupes = []

for x in coinlist:
    if x["symbol"] not in seen:
        seen[x["symbol"]] = 1
    else:
        if seen[x["symbol"]] == 1:
            dupes.append(x)
        seen[x["symbol"]] += 1
print("\nlist of duplicated ids")
for i in dupes:
    print(i["symbol"],  end="', '")
print()