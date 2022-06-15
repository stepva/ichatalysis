import time
import argparse
import emoji
from collections import Counter

from analysis import chat_output, top_chats
from const import AB_COPY, AB_PATH, MSG_COPY, MSG_PATH, MSG_QUERY
from db_utils import attach_db, close_con, connect_db, query_db
from processing import process_raw_msgs
from utils import prepare_files, load_status


def main(argv=None):
    start = time.time()
    prepare_files()
    con, cur = connect_db(MSG_PATH, MSG_COPY)
    attach_db(cur, AB_PATH, AB_COPY)
    df = query_db(con, MSG_QUERY)
    close_con(con)
    load_status(start, df)

    df = process_raw_msgs(df)

    chats = list(df["chat"].unique())

    parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     "-V", "-version", "--version", help="Version", action="version", version=version
    # )
    parser.add_argument("chat", nargs="?", type=str, choices=chats)
    args = parser.parse_args(argv)

    if args.chat:
        chat_output(df, args.chat)
        exit()

    print("\n************************************")
    print(f"Welcome to iChatalysis!\n")

    print(
        """To see your Top 10 chats, just type \"top\"
To chatalyse a specific conversation, just say which one - it has to be the same name format like in your address book.
If you need help, read the README
To exit, just type \"exit\":
        """
    )
    i = ""
    while i != "exit":
        print("\nWhat do you want to do?")
        i = input()

        if i == "top":
            top_chats(df, 10)

        elif i in chats:
            chat_output(df, i)

        elif i != "exit":
            print(f"No chats named {i}. Try again.")


if __name__ == "__main__":
    main()
