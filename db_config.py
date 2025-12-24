import psycopg2
import os

def get_connection():
    conn = psycopg2.connect(
        dbname="multiagent_ai",
        user="postgres",
        password="Jan27@2005",  
        host="localhost",
        port="5432"
    )
    return conn
