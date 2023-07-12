# from aiogram import Bot, Dispatcher
# from aiogram.types import Message
# from asyncio import run
# from aiogram.filters import Command


# admin_ID = 703586573
# class MyBot:
#     def __init__(self) -> None:
#         self.token = "5800696715:AAEqqBQXSdW6uG6Xg7H44j78oiHBDSrhLVo"
#         self.bot = Bot(self.token)
#         self.yonaltiruvchi = Dispatcher()

#     async def start_command(self, sms:Message):
#         await sms.answer(text="Welcome to My Bot!")
    
#     async def help_command(self, sms:Message):
#         await sms.answer(text="How can i help!")

#     async def eco(self, sms:Message, bot:Bot):
#         if sms.text == "jinni":
#             await sms.answer(text=f"O'zing jinni! 😂 {sms.from_user.username}")
#         else:
#             await sms.answer(text=sms.text)

#         habar = f"User: {sms.from_user.username}\n{sms.text}"
#         await bot.send_message(chat_id=admin_ID, text=habar)

#     async def start(self):
#         self.yonaltiruvchi.message.register(self.start_command, Command(commands=["start"]))
#         self.yonaltiruvchi.message.register(self.help_command, Command(commands=["yordam", "help"]))
#         self.yonaltiruvchi.message.register(self.eco)

#         await self.bot.send_message(chat_id=admin_ID, text="Bot ishga tushdi!")

#         try:
#             await self.yonaltiruvchi.start_polling(self.bot)
#         except:
#             await self.bot.session.close()
        

# if __name__ == "__main__":
#     bot = MyBot()
#     run(bot.start())

