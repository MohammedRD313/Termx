from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup,Message

from config import SUPPORT_CHAT,OWNER_ID


keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="ابدء الاستخراج ✍🏻", callback_data="gensession")
                    ],
                    [
                    InlineKeyboardButton("اوامـر الـبـوت", url="https://telegra.ph/%F0%9D%97%A0%F0%9D%97%BC%F0%9D%97%B5%F0%9D%97%AE%F0%9D%97%BA%F0%9D%97%BA%F0%9D%97%B2%F0%9D%97%B1-%F0%9D%97%A5%F0%9D%97%B6%F0%9D%97%B1%F0%9D%97%B5%F0%9D%97%AE--%F0%9D%97%99-07-29-3")
                    ],
                [
                    InlineKeyboardButton("𝘀𝘂𝗽𝗽𝗼𝗿𝘁 ⚙️", user_id=OWNER_ID),
                    InlineKeyboardButton("𝗦𝗰𝗼𝗿𝗽𝗶𝗼𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 ✏️", url="t.me/Scorpion_scorp")
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
