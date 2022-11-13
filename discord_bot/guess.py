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
        fopen = open(fhand, 'w')
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
        pass
    
    def test(self):
        a = stock.get_symbol(self.message)
    
GameGuess("test").pick_random(0, 100)
