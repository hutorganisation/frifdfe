import sqlite3
from sqlite3 import Error
import config.config as config

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(config.db_path)  
        return conn
    except Error as e:
        print(e)