from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from StringGen import Anony
from StringGen.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"""**
           ✎┊‌ مرحبا بك {message.from_user.first_name} فـي بـوت اسـتـخـراج جلسات العقرب 🦂

✎┊‌ يمكنك استـخـراج التالـي 

✎┊‌ تـلـيـثـون 
✎┊‌ بايـروجـرام 

✎┊‌ تم انشاء البوت بواسطة: [𝗠𝗼𝗵𝗮𝗺𝗺𝗲𝗱](t.me/Zo_r0) **""",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
