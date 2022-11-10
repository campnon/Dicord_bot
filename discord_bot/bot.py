import json


class Bot:
    
    def __init__(self):
        pass

    def auth(self):
        fhand = "C:\\Users\\Public\\Documents\\token.json"
        try:
            fopen = open(fhand)
            data = json.load(fopen)
            return data['app_id']
        except:
            return "An error has accored please try again"
        
    def stock(self):
        price = stock.temp_data()
        return price
    
    def message_split(self):
        # a function to split the string from 
        # massage comming in to the bot 
        # passed for the time being need to get a stock api to pull from 
        pass
