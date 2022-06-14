import sqlite3
import os
import pandas as pd


def connect_db(path, db_file):
    con = sqlite3.connect(os.path.join(path, db_file))
    cur = con.cursor()
    return con, cur


def attach_db(cur, path, db_file):
    file_path = os.path.join(path, db_file)
    cur.execute(f"ATTACH DATABASE '{file_path}' as contacts;")


def close_con(con):
    con.close()


def query_db(con, query):
    df = pd.read_sql_query(query, con)
    return df
