import json 

class stock:
    def __init__(slef):
        pass
    
    def api_url(self):
        self.base_url = 'https://api.polygon.io/v2/'
        pass

    def get_url_parms(self, dict):
        self.parms = dict
        for values in self.parms:
            pass
        pass
    
    def temp_data(self, message):
        sym = self.get_symbol(message)
        import requests
        from bs4 import BeautifulSoup
        url = f'https://www.google.com/finance/quote/{sym}:NASDAQ'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        rows = soup.find("div", {"class": "YMlKec fxKbKc"})
        for value in rows:
            return value
    
    def get_symbol(self, message):
        conntent = message.content
        symbol = conntent.split()
        return symbol[1]






