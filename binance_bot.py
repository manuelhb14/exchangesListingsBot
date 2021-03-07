from tweepy import OAuthHandler, Stream, StreamListener
import keys
import requests
import json

consumer_key=keys.consumer_key
consumer_secret=keys.consumer_secret
access_token=keys.access_token
access_token_secret=keys.access_token_secret

def telegram_bot_sendtext(bot_message):
    
    bot_token = keys.bot_token
    bot_chatID = keys.bot_chatID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)

    return response.json()

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        try:
            text = json.loads(data)['text']
            if ("listing" in text):
                print(data)
                telegram_bot_sendtext(text)
                return True
        except:
            print("Error")
            pass

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(follow=['877807935493033984'])