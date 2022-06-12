import time
import pandas as pd
from analysis import top_chats
from db_utils import attach_db, close_con, connect_db, query_db

from const import AB_COPY, AB_PATH, MSG_COPY, MSG_PATH, MSG_QUERY
from processing import process_raw_msgs
from utils import prepare_files, print_load_status

# todo nastavení –> soukromí a zabezpeční –> plný přístup k disku -> unlock and allow terminal (vs code maybe)
# https://stackoverflow.com/questions/58479686/permissionerror-errno-1-operation-not-permitted-after-macos-catalina-update


def main():
    start = time.time()
    prepare_files()
    con, cur = connect_db(MSG_PATH, MSG_COPY)
    attach_db(cur, AB_PATH, AB_COPY)
    df = query_db(con, MSG_QUERY)
    close_con(con)
    print_load_status(start, df)

    df = process_raw_msgs(df)
    top_chats(df, 10)


if __name__ == "__main__":
    main()
