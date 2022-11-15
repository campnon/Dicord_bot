import random 
import json
import sqlite3
import os

class GameGuess:
    def __init__(self, message):
        self.user = message.author
        self.message = message.content
        self.check_for_guess()

    def check_for_guess(self):
        con = sqlite3.connect('discord_bot//database.db')
        cur = con.cursor()
        cur.execute(f"SELECT * FROM Guess WHERE user='{self.user}'")
        data = cur.fetchall()
        if len(data) < 1:
            print("There is no guess for this usersss")
            choice = self.pick_random(0, 100)
            cur.execute(f"INSERT INTO GUESS(user, gues) VALUES('{self.user}', '{choice}')")
            con.commit()
            return choice
        return data[0][2]

    
    def pick_random(self, min, max):
        self.min = min
        self.max = max
        choice = random.randint(self.min, self.max)
        return choice

    def game(self):
        pass
        
    
    def test(self):
        a = stock.get_symbol(self.message)
    

