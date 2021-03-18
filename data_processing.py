import json

def basic_info(data):
    json_data = json.loads(data)
    print(json_data)
    tweet = json_data['text'].lower()
    date = json_data['created_at']
    user = json_data['user']['id_str']
    text = json_data["text"]
    isBinance = ((user=='877807935493033984') or (user=='829941007076687872'))
    return (json_data,tweet,date,user,text,isBinance)

def coin_data(json_data):
    coin_symbol = json_data["entities"]['symbols'][0]['text'].lower()
    coin_twitter = json_data["entities"]['user_mentions'][0]['screen_name'].lower()
    return(coin_symbol,coin_twitter)