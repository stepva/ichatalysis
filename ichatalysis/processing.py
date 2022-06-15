import pandas as pd

from const import ME, REACTION_DICT


def process_raw_msgs(df):
    df.loc[df["room_name"] == "", "room_name"] = None
    df.drop_duplicates(
        subset=["date", "room_name", "from_phone_number", "attachment_id"], inplace=True
    )

    df["name"] = df["first_name"]
    df.loc[df["last_name"].notnull(), "name"] = df["first_name"] + " " + df["last_name"]

    df.loc[df["room_name"].notnull(), "thread_id"] = df["room_name"]
    df.loc[df["room_name"].notnull(), "help_number"] = df["room_name"]
    df.loc[df["room_name"].isna() & df["name"].notnull(), "thread_id"] = df["name"]
    df.loc[df["is_from_me"] == 1, "name"] = ME

    df["reaction"] = df["associated_message_type"].map(REACTION_DICT)
    df.loc[
        df["reaction"].notnull(), "text"
    ] = None  # this could be reverted if wanted to find out to which message the reaction belongs

    df.rename(columns={"thread_id": "chat"}, inplace=True)
    df = check_unmatches_msgs(df)

    df = df[["chat", "service", "date", "text", "attachment", "name", "reaction"]]
    df["date"] = pd.to_datetime(df["date"])

    df["simple_chat"] = df["chat"].str.lower()
    df["simple_chat"] = df["simple_chat"].str.replace(" ", "")
    return df


def check_unmatches_msgs(df):
    failed = df[df["chat"].isna()].shape[0]
    pct = round(failed / df.shape[0] * 100, 1)
    print(f"Failed to match {failed:,} messages ({pct}%), I'm sorry :(")

    if pct > 10:
        print(
            "This is quite a big number, consider messaging me on Github. It is most likely due to mismatch between saved numbers in your address book (without prefix) and Messages (with prefix). But it might be something else and I would love to have a look at it and fix it!"
        )

    return df[df["chat"].notnull()]
