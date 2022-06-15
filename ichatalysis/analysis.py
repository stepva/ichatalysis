import pandas as pd
import emoji
from collections import Counter
from pprint import pprint


def top_chats(df, n):
    top = (
        df.groupby("chat")["chat"]
        .agg(["count"])
        .sort_values(by="count", ascending=False)
    )
    print(top.head(n))


def chat_output(df, chat):
    dfc = df[df["chat"] == chat]
    print(
        f"\n{chat}, from {dfc['date'].min().date()} to {dfc['date'].max().date()}",
    )
    print(f"Total messages: {dfc.shape[0]}", "\n")
    print(messages_view(dfc), "\n")
    print(reactions_view(dfc), "\n")
    print(attachments_view(dfc), "\n")
    pprint(emojis_view(dfc, 5), sort_dicts=False)


def messages_view(df):
    df_ = df.groupby("name")["text"].agg(["count"])
    df_["%"] = round(100 * df_["count"] / df_["count"].sum(), 1)
    return df_


def reactions_view(df):
    df_ = (
        df.groupby(["name", "reaction"])["reaction"]
        .agg(["count"])
        .reset_index()
        .set_index("name")
    )
    if not df_.empty:
        df_ = df_.pivot(columns="reaction", values="count").fillna(0).astype(int)
        df_.loc["Total"] = df_.sum()
        df_ = df_.sort_values(by="Total", axis=1, ascending=False)
        df_.drop("Total", inplace=True)
        return df_
    else:
        return "No reactions stats"


def attachments_view(df):
    df_ = (
        df.groupby(["name", "attachment"])["attachment"]
        .agg(["count"])
        .reset_index()
        .set_index("name")
    )
    if not df_.empty:
        df_ = df_.pivot(columns="attachment", values="count").fillna(0).astype(int)
        df_.loc["Total"] = df_.sum()
        df_ = df_.sort_values(by="Total", axis=1, ascending=False)
        df_.drop("Total", inplace=True)
        return df_
    else:
        return "No attachments stats"


def emojis_view(df, n):
    emojis = {f"Top {n} emojis": ""}
    for p, df_ in df.groupby("name"):
        t = " ".join(df_["text"].fillna("").to_list())
        e_ = [c for c in t if c in emoji.UNICODE_EMOJI["en"]]
        emojis[p] = Counter(e_).most_common(n)

    return emojis
