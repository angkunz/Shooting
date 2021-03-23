from tkinter import*
from tkinter import ttk
import sqlite3



def s():
        try :
            conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Python_project\Shooting_range2\main.db")
            c = conn.cursor()   
            c.execute("SELECT name,type,team FROM match1")
            rows = c.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e :
            print(e)

if __name__ == '__main__' :
    s()

