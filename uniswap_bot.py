from uniswap import Uniswap
from web3 import Web3
import keys

address = keys.address         # or "0x0000000000000000000000000000000000000000", if you're not making transactions
private_key = keys.private_key  # or None, if you're not going to make transactions
uniswap_wrapper = Uniswap(address, private_key, version=2)  # pass version=2 to use Uniswap v2

eth = "0x0000000000000000000000000000000000000000"
token = "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984"

print(uniswap_wrapper.get_eth_token_input_price(token, 1)) # ETH -> token
print(uniswap_wrapper.get_token_eth_input_price(token, 1)) # token -> ETH
# print(uniswap_wrapper.make_trade(token, eth, 1*10**18))