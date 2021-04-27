import os
import psycopg2
import pandas as pd

class DB:

    def __init__(self):
        db_url = os.environ['DATABASE_URL']
        self.conn = psycopg2.connect(db_url)
        self.cursor = self.conn.cursor()

    def getMatchingUserId(self, id):
        query = "SELECT * FROM users WHERE discord_id='{}'".format(str(id))
        result = pd.read_sql(query, self.conn)
        return result
    
    def createNewUserEntry(self, id):
        query = "INSERT INTO users(discord_id, monke_coin_amount) VALUES({}, 0)".format(str(id))
        self.cursor.execute(query)
        self.conn.commit()

    def __del__(self):
        self.conn.close()
    