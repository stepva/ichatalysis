from const import ME, REACTION_DICT


def process_raw_msgs(df):
    df.loc[df["room_name"] == "", "room_name"] = None
    df.drop_duplicates(subset=["date", "room_name", "from_phone_number"], inplace=True)

    df["full_name"] = df["first_name"]
    df.loc[df["last_name"].notnull(), "full_name"] = (
        df["first_name"] + " " + df["last_name"]
    )

    df.loc[df["room_name"].notnull(), "thread_id"] = df["room_name"]
    df.loc[df["room_name"].notnull(), "number"] = df["room_name"]
    df.loc[df["room_name"].isna() & df["full_name"].notnull(), "thread_id"] = df[
        "full_name"
    ]
    df.loc[df["is_from_me"] == 1, "full_name"] = ME

    df["reaction"] = df["associated_message_type"].map(REACTION_DICT)

    df.rename(columns={"thread_id": "chat"}, inplace=True)
    check_unmatches_msgs(df)
    return df


def check_unmatches_msgs(df):
    failed = df[df["chat"].isna()].shape[0]
    pct = round(failed / df.shape[0] * 100, 1)
    print(f"Failed to match {failed:,} messages ({pct}%), I'm sorry :(")
