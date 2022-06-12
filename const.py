import os

USER = os.path.expanduser("~")

MSG_PATH = os.path.join(USER, "Library/Messages")
MSG_FILE = "chat.db"
MSG_COPY = "copy_" + MSG_FILE

AB_PATH = os.path.join(USER, "Library/Application Support/AddressBook/Sources")
AB_FILE = "AddressBook-v22.abcddb"
AB_COPY = "copy_" + AB_FILE

MSG_QUERY = """select c.chat_identifier as thread_id,
            m.is_from_me, 
            case when m.is_from_me = 1 then m.account
            else h.id end as from_phone_number, 
            case when m.is_from_me = 0 then m.account
            else coalesce(h2.id, h.id) end as to_phone_number,
            m.service,
            datetime((m.date / 1000000000) + 978307200, 'unixepoch', 'localtime') as date,
            m.text, 
            att.mime_type as attachment,
            m.associated_message_type,
            c.display_name as room_name,
            coalesce(nums.ZFULLNUMBER, nums2.ZFULLNUMBER) as number,
            name.ZFIRSTNAME as first_name,
            name.ZLASTNAME as last_name

            from message as m
            left join handle h on m.handle_id = h.rowid
            left join chat_message_join cmj on m.rowid = cmj.message_id 
            left join chat c on cmj.chat_id = c.rowid
            left join chat_handle_join ch on c.rowid = ch.chat_id
            left join handle h2 on ch.handle_id = h2.rowid
            left join message_attachment_join maj on maj.message_id = m.rowid
            left join attachment att on att.rowid = maj.attachment_id
            left join contacts.ZABCDPHONENUMBER nums on replace(nums.ZFULLNUMBER, ' ', '') = replace(h.id, ' ', '')
            left join contacts.ZABCDPHONENUMBER nums2 on replace(nums2.ZFULLNUMBER, ' ', '') = replace(h2.id, ' ', '')
            left join contacts.ZABCDEMAILADDRESS mail on coalesce(h.id, h2.id) = mail.ZADDRESS
            left join contacts.ZABCDRECORD name on coalesce(mail.ZOWNER, nums.ZOWNER, nums2.ZOWNER) = name.Z_PK


            where
            -- try to eliminate duplicates due to non-unique message.cache_roomnames/chat.room_name
            (h2.service is null or m.service = h2.service)

            order by m.date asc;"""

ME = "Me"

REACTION_DICT = {
    2000: "love",
    2001: "like",
    2002: "dislike",
    2003: "haha",
    2004: "!!!",
    2005: "???",
    3000: "removed love",
    3001: "removed like",
    3002: "removed dislike",
    3003: "removed haha",
    3004: "removed !!!",
    3005: "removed ???",
}
