from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from StringGen import Anony
from StringGen.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"""
مرحبا بك فـي بـوت اسـتـخـراج جلسات العقرب | {message.from_user.first_name} 

✎┊‌ يمكنك استـخـراج التالـي 
✎┊‌ تـلـيـثـون 
✎┊‌ بايـروجـرام 

✎┊‌ تم انشاء البوت بواسطة: @Zo_r0 , @I_e_e_l
""",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
