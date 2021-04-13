from uniswap_bot import UniBot
import keys
import time

def uniswap_main(token_address):
    #? Create keys.py file to add your adddress and private key to be able to make transactions
    address = keys.address 
    private_key = keys.private_key
    eth_quantity = 1

    uniswap_trading = UniBot(address, private_key, token_address, eth_quantity)
    # uniswap_trading.before_transaction()
    # uniswap_trading.buy_transaction()
    # time.sleep(20) # Wait for buy transaction # TODO: Modify it to continue unitl tokens > 0
    # uniswap_trading.after_transaction()

    # print("----Type 'CTRL+C' to swap token to $ETH----") # To sell press CTRL+C #TODO: Sell when certain threshold is reached
    # try:
    #     while True:
    #         time.sleep(3)
    #         uniswap_trading.checkPrice()
    # except KeyboardInterrupt:
    #     pass
    # print()

    uniswap_trading.sell_transaction()
    time.sleep(20) # Wait for sell transaction # TODO: Modify it to continue unitl tokens = 0 
    uniswap_trading.final_balance()