def top_chats(df, n):
    top = df.groupby("chat").size().sort_values(ascending=False)
    print(top.head(n))
