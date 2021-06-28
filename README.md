# Exchanges New Listings Bot

Exchanges Listings Bot that sends notifications with a Telegram bot using Twitter API and automatically.

Use Twitter API to send notifications with Telegram when exchanges tweets about new listings.

Exchanges that will be monitored: Binance, Huobi, Kraken, KuCoin, Bitfinex, Bithumb, Crypto.com. More exchanges can be added.

Current exchanges: Binance

## Instructions

Create a keys.py file with your keys

```python
# Twitter access keys to read stream and retrieve Binance tweets

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""


# Telegram bot id's and keys

bot_token = ''
bot_chatID = ''
```

Run exchanges_bot.py and wait for notifications. To automatically buy the token on Uniswap or PancakeSwap you can see [this repository](https://github.com/manuelhb14/cake_uni_transaction_bot). A bot for placing orders on Binance futures will be developed in the future.
