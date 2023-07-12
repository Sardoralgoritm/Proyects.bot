# from aiogram.types import Message, KeyboardButton
# from aiogram.filters.command import Command
# from aiogram.utils.keyboard import ReplyKeyboardBuilder
# from aiogram import Bot, Router, Dispatcher
# from config import BOT_API3
# from aiogram.filters.text import Text
# from asyncio import run
# from random import randint

# bt = Bot(token=BOT_API3)
# dp = Dispatcher()
# cnt = 0
# num = randint(1,10)
# ckekt = 0
# ran = randint(1,10)
# left = 1
# right = 10

# async def input_f(smg:Message):
#     num1 = ReplyKeyboardBuilder()
#     num1.add(KeyboardButton(text="1"), KeyboardButton(text="2"), KeyboardButton(text="3"), KeyboardButton(text="4"), KeyboardButton(text="5"), KeyboardButton(text="6"), KeyboardButton(text="7"), KeyboardButton(text="8"), KeyboardButton(text="9"), KeyboardButton(text="10"))

#     num1.adjust(3,3,3,1)
#     await smg.answer(text="Tanlang:", reply_markup=num1.as_markup())
    

# @dp.message(Command("start"))
# async def start_button(sms:Message):
#     st = ReplyKeyboardBuilder()
#     snt = KeyboardButton(text="🎲 Son Topish O'yini 🎲")
#     inf = KeyboardButton(text="❗️ Info ❗️")
#     st.add(snt, inf)
#     st.adjust(1,1)
#     await sms.answer(text="Assalomu alaykum menu tanlang:", reply_markup=st.as_markup())

# @dp.message(Text(text="🎲 Son Topish O'yini 🎲"))
# async def find_number(sms:Message):
#     await sms.answer(text="Keling o'ylagan sonni topish o'ynaymiz!\n1 dan 10 gacha son o'yladim. Topa olasizmi?: ")
#     num = randint(1,10)
#     num1 = ReplyKeyboardBuilder()
#     num1.add(KeyboardButton(text="1",), KeyboardButton(text="2"), KeyboardButton(text="3"), KeyboardButton(text="4"), KeyboardButton(text="5"), KeyboardButton(text="6"), KeyboardButton(text="7"), KeyboardButton(text="8"), KeyboardButton(text="9"), KeyboardButton(text="10"))
#     num1.adjust(3,3,3,1)
#     await sms.answer(text="Tanlang:", reply_markup=num1.as_markup())

# @dp.message(Text)
# async def text(sms:Message):
#     global cnt
#     global chekt
#     number = int(sms.text)
#     if number == num and chekt == 0:
#         cnt += 1
#         await sms.answer(f"TOPDINGIZ!!! {num} sonini o'ylagan edim {cnt} ta taxmin bilan topdingiz. Tabriklayman!!!", reply_markup=ReplyKeyboardBuilder().add(KeyboardButton(text="Enter",)).adjust(1).as_markup())
#         ckekt = 1
#     elif ckekt == 1:
#         @dp.message(Text(text="Enter"))
#         # def run()

#     elif number < num:
#         await sms.answer(text="Xato men o'ylagan son bundan kattaroq. Yana harakat qiling!")
#         cnt += 1
#     else:
#         await sms.answer(text="Xato men o'ylagan son bundan kichikroq. Yana harakat qiling!")
#         cnt += 1
#         num1 = ReplyKeyboardBuilder()
#         num1.add(KeyboardButton(text="1"), KeyboardButton(text="2"), KeyboardButton(text="3"), KeyboardButton(text="4"), KeyboardButton(text="5"), KeyboardButton(text="6"), KeyboardButton(text="7"), KeyboardButton(text="8"), KeyboardButton(text="9"), KeyboardButton(text="10"))
#         num1.adjust(3,3,3,1)
#         await sms.answer(text="Tanlang:", reply_markup=num1.as_markup())
#         number = text(sms)
        

# async def start():
#     try:
#         await dp.start_polling(bt)
#     except:
#         bt.session.close()

# if __name__ == "__main__":
#     run(start())
# 
# 
# 
# from telegram import *
# from telegram.ext import *
# from config import BOT_API3

# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# async def text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     tex=update.message.text
#     print(tex)

# app = ApplicationBuilder().token(BOT_API3).build()

# app.add_handler(CommandHandler("hello", hello))
# app.add_handler(MessageHandler(filters.TEXT,text))

# app.run_polling()