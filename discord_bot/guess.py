import random 

class GameGuess:
    def __init__(self, message):
        self.user = massage.author
        self.message = message.content

    def pick_random(self, min, max):
        self.min = min
        self.max = max
        choice = random.randint(self.min, self.max)
        return choice

    def game(self):
        pass
    
    def test(self):
        a = stock.get_symbol(self.message)
   