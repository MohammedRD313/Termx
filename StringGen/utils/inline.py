from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup,Message

from config import SUPPORT_CHAT,OWNER_ID


keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="ابدء الاستخراج ✍🏻", callback_data="gensession")
                    ],
                    [
                    InlineKeyboardButton("اوامـر الـبـوت", url="https://telegra.ph/%D8%A7%D9%88%D8%A7%D9%85%D8%B1-%D8%A8%D9%88%D8%AA-%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D8%AE%D8%B1%D8%A7%D8%AC-10-11")
                    ],
                [
                    InlineKeyboardButton("المساعد ⚙️", user_id=OWNER_ID),
                    InlineKeyboardButton("𝗦𝗰𝗼𝗿𝗽𝗶𝗼𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 ✏️", url="t.me/@Scorpion_scorp")
                ]
            ]
        )

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="Pyrogram | بايوجرام ¹", callback_data="pyrogram1"),
            InlineKeyboardButton(text="Pyrogram | بايوجرام ²", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="Telethon | تيليثون", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="استخرج مجدداً", callback_data="gensession")]]
)
