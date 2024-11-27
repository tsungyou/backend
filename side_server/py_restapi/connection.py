from config import DB_HOST, DB_NAME, DB_PASS, DB_USER
import psycopg2

def get_db_connection():
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS)
    return conn