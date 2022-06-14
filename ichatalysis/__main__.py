import time
from ichatalysis.analysis import top_chats
from ichatalysis.db_utils import attach_db, close_con, connect_db, query_db

from ichatalysis.const import AB_COPY, AB_PATH, MSG_COPY, MSG_PATH, MSG_QUERY
from ichatalysis.processing import process_raw_msgs
from ichatalysis.utils import prepare_files, print_load_status

# todo - simple analysis of chosen chat, emojis, games


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
