import random 
import json
import os 

class GameGuess:
    def __init__(self, message):
        #self.user = message.author
        pass
        #self.message = message.content

   
    def open_file(slef):
        fhand  = 'data.json'
        fopen = open(fhand, 'r')
        data = json.load(fopen)
        return data

    
    def pick_random(self, min, max):
        self.min = min
        self.max = max
        choice = random.randint(self.min, self.max)
        save = 'not code yet will be a function to save' 
        #the guess witht he username of the perosn who made it'
        return choice

    def game(self):
        data = self.open_file()
        if 'Mesisamu' in data['guess']:
            print("uer already has a guess in the file")
        else:
            print("No user found in the file")
        
    
    def test(self):
        a = stock.get_symbol(self.message)
    
GameGuess("test").game()
