# from aiogram.types import InlineKeyboardButton, Message, KeyboardButton, CallbackQuery
# from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
# from aiogram import Bot, Router, Dispatcher
# from config import BOT_IPA2
# from aiogram.filters.command import Command
# from asyncio import run
# from aiogram.filters.text import Text

# bt = Bot(token=BOT_IPA2)
# dp = Dispatcher()

# @dp.message(Command(commands=["start", "help"]))
# async def start_message(sms:Message):
#     inRu = InlineKeyboardButton(text="RU", callback_data="lang:ru")
#     inEng = InlineKeyboardButton(text="ENG", callback_data="lang:en")
#     inUz = InlineKeyboardButton(text="UZ", callback_data="lang:uz")
#     bld = InlineKeyboardBuilder()
#     bld.add(inEng, inRu, inUz)
#     bld.adjust(2,1)
#     await sms.answer(text="Tilni tanlang",  reply_markup=bld.as_markup())

# @dp.message(Command("menu"))
# async def menu_buutons(sms:Message):
#     rp = ReplyKeyboardBuilder()
#     set = KeyboardButton(text="⚙️⚙️ Setting ⚙️⚙️")
#     lang = KeyboardButton(text="Language")
#     stat = KeyboardButton(text="📊 Statistika 📈")
#     rp.add(lang,set,stat)
#     rp.adjust(1,2)
#     await sms.answer(text=" ",reply_markup=rp.as_markup())

# @dp.message(Text(text="⚙️⚙️ Setting ⚙️⚙️"))
# async def setting_message(sms:Message):
#     await sms.answer(text="Qabul qilindi setting")

# @dp.callback_query(Text(startswith="lang:"))
# async def lang_querty(clb:CallbackQuery):
#     if clb.data == "lang:uz":
#         await clb.message.answer("Assalomu alaykum Xush kelibsiz")
#         await clb.answer(text="Sizning tilingiz muvaffaqiyatli Uzbek tiliga o'girildi!", show_alert=False)
#     elif clb.data == "lang:ru":
#         await clb.message.answer("Привет и добро пожаловать")
#         await clb.answer(text="Ваш язык успешно конвертирован в русский!",show_alert=False)
#     else:
#         await clb.message.answer("Hello Welcome to channel")
#         await clb.answer(text="Your language has been successfully converted to English!",show_alert=False)

# async def start():
#     try:
#         await dp.start_polling(bt)

#     except:
#         await bt.session.close()

# if __name__ == "__main__":
#     run(start())


# from aiogram.types import KeyboardButton
# from aiogram.utils.keyboard import ReplyKeyboardBuilder

# class Greetings:
#     def __init__(self, ful_name) -> None:
#         self.__fulname = ful_name
#         self._main_menu = ["Orders", "Settings", "Statistics", "Language", "Users"]

#     def get_greeting(self):
#         return f"""Hi my friend {self.__fulname}
#         Welcome to our bot!!!"""
    
#     @property
#     def FullName(self):
#         return self.__fulname
    
#     def get_keyboards(self):
#         rp = ReplyKeyboardBuilder()
#         for menu in self._main_menu:
#             rp.add(KeyboardButton(text=menu))
#         rp.adjust(2,2,1)
#         return rp.as_markup()
    
# class GreetingUz(Greetings):
#     def __init__(self, ful_name) -> None:
#         super().__init__(ful_name)
#         self._main_menu[0] = "Buyurmalar"
#         self._main_menu[1] = "Sozlamalar"
#         self._main_menu[1] = "Statistika"
#         self._main_menu[2] = "Til"
#         self._main_menu[3] = "Foydalanuvchilar"

#     def get_greeting(self):
#         return f"""Assalomu alaykum {self.FullName}
#         Botimizga xush kelibsiz!!!"""
    
