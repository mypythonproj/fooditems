from django.db import models
import sqlite3

# Create your models here.
def sql_database():
    conn = sqlite3.connect('Client_data.db') #Opens Connection to SQLite database file.
    conn.execute('''CREATE TABLE Client_db
                (NAME            BLOB NOT NULL,
                PASSWORD         BLOB NOT NULL,
                );''') #Creates the table
    conn.commit() # Commits the entries to the database
    conn.close()

def create_user(username, password):
    conn = sqlite3.connect('Client_data.db')
    cursor = conn.cursor()
    params = (username,password)
    cursor.execute("INSERT INTO Client_db VALUES (?,?)",params)
    conn.commit()
    print('User Creation Successful')
    conn.close()

def data_retrieval(username,password):
    conn = sqlite3.connect('Client_data.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Client_db WHERE NAME =:NAME",{'NAME':username})
    if cur.fetchone()[1] == password:
        print('LogIn Successful')