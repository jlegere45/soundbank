import psycopg2
from dotenv import dotenv_values


def setup_connection():
    config = dotenv_values(".env")
    conn = psycopg2.connect(dbname=config["db_name"],
                            user=config["db_username"],
                            password=config["db_password"],
                            host=config["db_url"],
                            port=config["db_port"])
    curr = conn.cursor()
    return conn, curr