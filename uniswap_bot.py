from uniswap import Uniswap
from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
import time
import os
import keys

#! Set environment variable in os 
## Example:
## https://mainnet.infura.io/v3/<project_id>
## add your own project id from infura node
w3 = Web3(Web3.HTTPProvider(os.getenv('PROVIDER')))
w3.middleware_onion.inject(geth_poa_middleware, layer=0) # Necessary if not running node locally

#! Create keys.py file to add your adddress and private key to be able to make transactions
address = keys.address 
private_key = keys.private_key
uniswap_wrapper = Uniswap(address, private_key, version=2) #
eth = "0x0000000000000000000000000000000000000000"

# Read standard ERC-20 contract to have access to read functions
with open("abis/erc20_abi.json") as f:
    ABI = json.load(f)

token = Web3.toChecksumAddress("0x1f9840a85d5af5bf1d1762f925bdaddc4201f984") # Transform address obtained to checkSum address, Web3 requirement
eth_quantity = 1 #ETH to exchange for token

token_contract = w3.eth.contract(token, abi=ABI) # Create basic functions of contract to get details
token_symbol = token_contract.functions.symbol().call() # Get token symbol eg. UNI, SUPER, ETH, ERN
token_decimals = token_contract.functions.decimals().call() # Decimals of token can change depending on contract # TODO: Testing with other contracts with less decimals

eth_quantity_to_wei = w3.toWei(1, 'ether') #Get wei from ETH for functions to work

estimated_tokens = uniswap_wrapper.get_eth_token_input_price(token, eth_quantity_to_wei) / (1*10**token_decimals) # Get estimated tokens of token given

currentBalanceToken = token_contract.functions.balanceOf(address).call() / (1*10**token_decimals)
currentBalanceETH = w3.eth.get_balance(address) / (1*10**18)

print("----Before transaction----")
print("estimated number of {} for 1 ETH: {}".format(token_symbol, estimated_tokens)) # Wei -> token 
print("balance of {} in account: {}".format(token_symbol, currentBalanceToken)) # Before buy transaction token balance
print("balance of ETH in account: {}".format(currentBalanceETH)) # Get ETH balance

buy_txn = uniswap_wrapper.make_trade(eth, token, eth_quantity_to_wei).hex() # Trade ETH for token # TODO: Modify gas fee

print("----Buy token transaction----")
print("hash of txn: {}".format(buy_txn)) # Hash buy transaction
print("link to etherscan: https://rinkeby.etherscan.io/tx/{}".format(buy_txn)) #Link to buy transaction # TODO: Test on mainnet

time.sleep(20) # Wait for buy transaction # TODO: Modify it to testnet

newBalanceToken = token_contract.functions.balanceOf(address).call()
newBalanceETH = w3.eth.get_balance(address) / (1*10**18)

print("----After transaction----")
print("${} bought: {}".format(token_symbol, newBalanceToken / (1*10**token_decimals))) # Get tokens balance
print("balance of ETH in account: {}".format(newBalanceETH)) # Get current ETH balance

print("----Type 'CTRL+C' to swap token to $ETH----") # To sell press CTRL+C #TODO: Sell when certain threshold is reached
try:
    
    while True:
        time.sleep(3)
        estimated_eth = uniswap_wrapper.get_token_eth_input_price(token, newBalanceToken)

        print("Estimated ETH for {} {}: {}".format(newBalanceToken / (1*10**token_decimals), token_symbol, estimated_eth / (1*10**18))) # Get token -> Wei 

except KeyboardInterrupt:
    pass
print()

sell_txn = uniswap_wrapper.make_trade(token, eth, newBalanceToken).hex() # Trade tokens for ETH #TODO: Modify gas fee

print("----Sell token transaction----")
print("hash of txn: {}".format(sell_txn)) # Hash sell transaction
print("link to etherscan: https://rinkeby.etherscan.io/tx/{}".format(sell_txn)) # Link to sell transaction # TODO: Test on mainnet
# TODO: See if transaction is succesful, else send it again.

time.sleep(20) # Wait for sell transaction # TODO: Modify it to testnet

finalBalanceETH = w3.eth.get_balance(address) / (1*10**18)
finalBalanceToken = token_contract.functions.balanceOf(address).call()
print("balance of ETH in account: {}".format(finalBalanceETH)) # Get final ETH balance
print("balance of {} in account: {}".format(token_symbol,finalBalanceToken)) # Get final token balance, should be zero

# TODO: Reformat to functions and test with tweets listing:,UNI, etc