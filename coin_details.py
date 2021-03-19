def coingecko_info(cg,coinlist,coin_symbol,coin_twitter):
    coin_num = 0
    tweet_num = 0
    info = []
    details = []
    twitter_usrname = []
    platform = []
    price = []
    while coin_num < len(coinlist):
        if (coinlist[coin_num]['symbol']==coin_symbol):
            info.append(coinlist[coin_num])
        coin_num+=1
    for i in info:
        print(i)
        details.append(cg.get_coin_by_id(i['id']))
    for i in details:
        twitter_usrname.append(i['links']['twitter_screen_name'].lower())
        platform.append(i['platforms'])
        price.append(i['market_data']['current_price']['usd'])
    while tweet_num < len(twitter_usrname):
        if(twitter_usrname[tweet_num]==coin_twitter):
            return (info[tweet_num],platform[tweet_num],price[tweet_num])
        tweet_num+=1 
    return('Error....')

def uni_cake_link(platform):
    contracts = ''
    if ('ethereum' in platform):
        contracts += ('https%3A%2F%2Fapp.uniswap.org%2F%23%2Fswap%3FoutputCurrency%3D' + platform['ethereum'] + '\n')
    if ('binance-smart-chain' in platform):
        contracts += ('https%3A%2F%2Fexchange.pancakeswap.finance%2F%23%2Fswap%3FoutputCurrency%3D' + platform['binance-smart-chain'])
    return contracts
    