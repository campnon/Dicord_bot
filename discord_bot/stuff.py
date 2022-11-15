import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

sql = """
CREATE TABLE Guess(user,guess)


"""


cur.execute(sql)