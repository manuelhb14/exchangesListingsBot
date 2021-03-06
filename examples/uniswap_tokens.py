from web3.auto.infura.mainnet import w3
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
coinlist = cg.get_coins_list()


NETWORK = "mainnet"
UNISWAP_FACTORY_ADDRESS = {
"mainnet": "0xc0a47dFe034B400B47bDaD5FecDa2621de6c4d95",
# "rinkeby": "0xf5D915570BC477f9B8D6C0E980aA81757A3AaC36"
}
UNISWAP_FACTORY_ABI = """[{"name": "NewExchange", "inputs": [{"type": "address", "name": "token", "indexed": true}, {"type": "address", "name": "exchange", "indexed": true}], "anonymous": false, "type": "event"}, {"name": "initializeFactory", "outputs": [], "inputs": [{"type": "address", "name": "template"}], "constant": false, "payable": false, "type": "function", "gas": 35725}, {"name": "createExchange", "outputs": [{"type": "address", "name": "out"}], "inputs": [{"type": "address", "name": "token"}], "constant": false, "payable": false, "type": "function", "gas": 187911}, {"name": "getExchange", "outputs": [{"type": "address", "name": "out"}], "inputs": [{"type": "address", "name": "token"}], "constant": true, "payable": false, "type": "function", "gas": 715}, {"name": "getToken", "outputs": [{"type": "address", "name": "out"}], "inputs": [{"type": "address", "name": "exchange"}], "constant": true, "payable": false, "type": "function", "gas": 745}, {"name": "getTokenWithId", "outputs": [{"type": "address", "name": "out"}], "inputs": [{"type": "uint256", "name": "token_id"}], "constant": true, "payable": false, "type": "function", "gas": 736}, {"name": "exchangeTemplate", "outputs": [{"type": "address", "name": "out"}], "inputs": [], "constant": true, "payable": false, "type": "function", "gas": 633}, {"name": "tokenCount", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [], "constant": true, "payable": false, "type": "function", "gas": 663}]"""
UNISWAP_FACTORY_CONTRACT = w3.eth.contract(address=UNISWAP_FACTORY_ADDRESS[NETWORK], abi=UNISWAP_FACTORY_ABI)
token_count = UNISWAP_FACTORY_CONTRACT.functions.tokenCount().call()
print('Token Count: {}'.format(token_count))
n = 0
file = open('uni_pairs.py', 'w')

while(n <= token_count):
    # print('=========================')
    token = UNISWAP_FACTORY_CONTRACT.functions.getTokenWithId(n).call()
    exchange = UNISWAP_FACTORY_CONTRACT.functions.getExchange(token).call()
    # print('Token Contract Address: {}'.format(token))
    # print('Uniswap Exchange Contract Address: {}'.format(exchange))
    file.write(str((token,exchange)))
    file.write('\n')
    n += 1