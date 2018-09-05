import os
import psycopg2
from src import Feeder


class FeedUsername(Feeder):

    @staticmethod
    def build_connector():
        params = {
            'USER_DB_HOST': os.getenv('USER_DB_HOST', 'userdb'),
            'USER_DB_DATABASE': os.getenv('USER_DB_DATABASE', 'postgres'),
            'USER_DB_USER': os.getenv('USER_DB_USER', 'postgres'),
            'USER_DB_PASSWORD': os.getenv('USER_DB_PASSWORD', ''),
            'USER_DB_PORT': int(os.getenv('USER_DB_PORT', 5432)),
        }
        try:
            conn = psycopg2.connect("""
            dbname='{USER_DB_DATABASE}'
            user='{USER_DB_USER}'
            host='{USER_DB_HOST}'
            password='{USER_DB_PASSWORD}'
            port='{USER_DB_PORT}'""".format(**params))
            return conn
        except Exception as e:
            print('Unable to connect to user db.', str(e))

    @staticmethod
    def get_data(conn):
        data = {}
        try:
            cur = conn.cursor()
            cur.execute("SELECT id, username FROM public.userservice_user")
            fetch = cur.fetchall()
            for uid, username in fetch:
                data[uid] = username
        except Exception as e:
            print(e.pgerror)
        return data
