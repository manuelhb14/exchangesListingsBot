from txns import Txn_bot
import time
import sys

token_address = "0x22168882276e5D5e1da694343b41DD7726eeb288"

quantity = int(5*10**18)
net = 'bsc-mainnet'
slippage = 30 #%
gas_price = 50*10**9 #Gwei, bsc-mainnet=5, eth-mainnet=https://www.gasnow.org/, eth-rinkeby=1

bot = Txn_bot(token_address, quantity, net, slippage, gas_price)
tokens = 0
while (tokens==0):
    try:
        time.sleep(2)
        tokens = bot.get_amounts_out_buy()
    except KeyboardInterrupt:
        print()
        sys.exit()
    except Exception as e:
        print(e)
        print("Not enough liquidity...")
bot.buy_token()
# time.sleep(30)
# bot.sell_token()
