from uniswap import Uniswap
from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
import os

class UniBot():
    def __init__(self, address, private_key, token_address, eth_quantity):
        self.address = address
        self.private_key = private_key
        self.token_address = Web3.toChecksumAddress(token_address) # Transform address obtained to checkSum address, Web3 requirement
        self.w3 = self.start_provider_connection() 
        self.uniswap_wrapper = self.start_uniswap_connection()
        self.eth_quantity = self.w3.toWei(eth_quantity, 'ether')
        self.eth = "0x0000000000000000000000000000000000000000"
        self.abi = self.load_erc72_abi()
        self.token_contract = self.w3.eth.contract(self.token_address, abi=self.abi) # Create basic functions of contract to get details
        self.token_symbol = self.token_contract.functions.symbol().call() # Get token symbol eg. UNI, SUPER, ETH, ERN
        self.token_decimals = self.token_contract.functions.decimals().call() # Decimals of token can change depending on contract # TODO: Testing with other contracts with less decimals
        self.newBalanceToken = 0
    #? Set environment variable in os 
    ## Example:
    ## https://mainnet.infura.io/v3/<project_id>
    ## add your own project id from infura node
    def start_provider_connection(self):
        w3 = Web3(Web3.HTTPProvider(os.getenv('PROVIDER')))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0) # Necessary if not running node locally
        return w3

    def start_uniswap_connection(self):
        return Uniswap(self.address, self.private_key, version=2) #

    # Read standard ERC-20 contract to have access to read functions
    def load_erc72_abi(self):
        with open("abis/erc20_abi.json") as f:
            return json.load(f)

    def before_transaction(self):
        estimated_tokens = self.uniswap_wrapper.get_eth_token_input_price(self.token_address, self.eth_quantity) / (1*10**self.token_decimals) # Get estimated tokens of token given

        currentBalanceToken = self.token_contract.functions.balanceOf(self.address).call() / (1*10**self.token_decimals)
        currentBalanceETH = self.w3.eth.get_balance(self.address) / (1*10**18)

        print("----Before transaction----")
        print("estimated number of {} for 1 ETH: {}".format(self.token_symbol, estimated_tokens)) # Wei -> token 
        print("balance of {} in account: {}".format(self.token_symbol, currentBalanceToken)) # Before buy transaction token balance
        print("balance of ETH in account: {}".format(currentBalanceETH)) # Get ETH balance

    def buy_transaction(self):
        buy_txn = self.uniswap_wrapper.make_trade(self.eth, self.token_address, self.eth_quantity).hex() # Trade ETH for token # TODO: Modify gas fee

        print("----Buy token transaction----")
        print("hash of txn: {}".format(buy_txn)) # Hash buy transaction
        print("link to etherscan: https://rinkeby.etherscan.io/tx/{}".format(buy_txn)) #Link to buy transaction # TODO: Test on mainnet
        
    
    def after_transaction(self):
        self.newBalanceToken = self.token_contract.functions.balanceOf(self.address).call()
        newBalanceETH = self.w3.eth.get_balance(self.address) / (1*10**18)
        print("----After transaction----")
        print("${} bought: {}".format(self.token_symbol, self.newBalanceToken / (1*10**self.token_decimals))) # Get tokens balance
        print("balance of ETH in account: {}".format(newBalanceETH)) # Get current ETH balance

    def checkPrice(self):
        estimated_eth = self.uniswap_wrapper.get_token_eth_input_price(self.token_address, self.newBalanceToken)
        print("estimated ETH for {} {}: {}".format(self.newBalanceToken / (1*10**self.token_decimals), self.token_symbol, estimated_eth / (1*10**18))) # Get token -> Wei 


    def sell_transaction(self):
        sell_txn = self.uniswap_wrapper.make_trade(self.token_address, self.eth, self.newBalanceToken).hex() # Trade tokens for ETH #TODO: Modify gas fee
        print("----Sell token transaction----")
        print("hash of txn: {}".format(sell_txn)) # Hash sell transaction
        print("link to etherscan: https://rinkeby.etherscan.io/tx/{}".format(sell_txn)) # Link to sell transaction # TODO: Test on mainnet
    # TODO: See if transaction is succesful, else send it again.

    def final_balance(self):
        final_balance_ETH = self.w3.eth.get_balance(self.address) / (1*10**18)
        final_balance_token = self.token_contract.functions.balanceOf(self.address).call()
        print("balance of ETH in account: {}".format(final_balance_ETH)) # Get final ETH balance
        print("balance of {} in account: {}".format(self.token_symbol,final_balance_token)) # Get final token balance, should be zero

    # TODO: Reformat to functions and test with tweets listing:,UNI, etc