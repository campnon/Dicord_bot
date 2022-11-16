import random 
import json
import sqlite3
import os

class GameGuess:
    def __init__(self, message):
        self.user = message.author
        self.message = message.content
       

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

    def splt_user_message(self, split_how):
        message = self.message.split()
        if split_how is 25:
            for k in message:
                print(k)
        return int(k)
        

    def game(self):
        guesss = self.check_for_guess()
        user_gues = self.splt_user_message(25)
        if int(guesss) < user_gues:
            return f'Your guess of {user_gues}, is Higher then number choisen. Try again'
        elif int(guesss) > user_gues:
            return f'Your guess of {user_gues}, is Below then number choisen. Try again'
        elif int(guesss) == user_gues:
            #delte user guesss from databases
            return f'Youer guess of {user_gues} was the corret number, Well played'
        

        return f'The guess is {guesss}'
        
    
    def test(self):
        a = stock.get_symbol(self.message)
    

