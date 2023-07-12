# from aiogram import Bot, Router, Dispatcher
# from config import BOT_IPA
# from aiogram.types import Message, User
# from aiogram.filters.command import Command
# from aiogram.filters.text import Text
# from asyncio import run

# bt = Bot(token=BOT_IPA)
# dp = Dispatcher()

# @dp.message(Command("help"))
# async def help_handler(msg:Message):
#     us = msg.from_user
#     str = f"""Assalomu alaykum {us.first_name:15}
#     Botimiz hozrcha hamma narsa qiladi!!!"""

#     await msg.reply(text=str)

# @dp.message(Command("myid"))
# async def my_id(msg:Message):

#     await msg.reply(text=f"""Your ID:{msg.from_user.id}""")

# async def start():
#     try:
#         await dp.start_polling(bt)
#     except Exception as e:
#         await bt.session.close()


# if __name__ == "__main__":
#     run(start())

# n = 6

# cnt = 0
# while n != 3 and n != 5 and n != 2:
#     if n % 5 == 0:
#         n //= 5
#         cnt = 1
#     elif n % 3 == 0:
#         n //= 3
#         cnt = 1
#         print("a")
#     elif n % 2 == 0:
#         n //= 2
#         cnt = 1
#     else:
#         cnt = 0
#         break
# if cnt and (n == 2 or n == 5 or n == 3):
#     print(True)
# else:
#     print(False)


# from requests import get, post, auth, RequestException, status_codes

# class Account:
#     def __init__(self, password="", login="") -> None:
#         self.__password = password
#         self.__login = login

#     def get_login(self):
#         return self.__login
    
#     def get_password(self):
#         return self.__password
    
# class NTaccount(Account):
#     def __init__(self, password="salom777", login="998999553557", rem=False) -> None:
#         super().__init__(password, login)
#         self.rememberMe = rem

#     def get_remember(self):
#         return self.rememberMe
    
#     def set_remember(self, fl):
#         self.rememberMe = fl

#     def enter_to_account(self):
#         url = "https://najotedu.t8s.ru?"
#         data = {
#             "Loglogin":self.get_login(),
#             "LogPassword":self.get_password(),
#             "LogRememberMe":self.get_remember()
#         }
#         resp = post(url=url, params=data)
#         if resp.status_code == 200:
#             txt = resp.text
#             with open("account.html",mode="w+",encoding="utf-8") as f:
#                 f.write(txt)
#         else:
#             print("Xatolik")
# if __name__ == "__main__":
#     myac = NTaccount()
#     myac.enter_to_account()

