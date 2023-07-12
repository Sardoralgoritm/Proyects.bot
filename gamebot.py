from aiogram.types import Message, KeyboardButton, User
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from random import randint
from asyncio import run
from config import BOT_API3



class Gamebot:
    def __init__(self) -> None:
        self.bt = Bot(token="6367593670:AAE1bCfP9zblnhS92h2Lt2g2blW4fmCAOhk")
        self.dp = Dispatcher()
        self.num = randint(1, 10)
        self.cnt = 0
        self.cnt1 = 0
        self.chekt = 0
        self.left = 1
        self.right = 10
        self.num1 = randint(1, 10)



    async def start_command(self, sms:Message):
        rp = ReplyKeyboardBuilder()
        rp.add(KeyboardButton(text="🎲 Son Topish O'yini 🎲"), KeyboardButton(text="❗️ Info ❗️"))
        rp.adjust(1,1)
        await sms.answer(text="👇👇👇 Menulardan birini tanlang 👇👇👇", reply_markup=rp.as_markup())
        
    async def eco(self, sms:Message, bot:Bot):
        if sms.text == "🎲 Son Topish O'yini 🎲":
            await sms.answer(text="Keling o'ylagan sonni topish o'ynaymiz!\n1 dan 10 gacha son o'yladim. Topa olasizmi?: 🎲", reply_markup=ReplyKeyboardBuilder().add(KeyboardButton(text="1"),KeyboardButton(text="2"),KeyboardButton(text="3"),KeyboardButton(text="4"),KeyboardButton(text="5"),KeyboardButton(text="6"),KeyboardButton(text="7"),KeyboardButton(text="8"),KeyboardButton(text="9"),KeyboardButton(text="10")).adjust(3,3,3,1).as_markup())
        elif sms.text == "❗️ Info ❗️":
            await sms.answer(text=f"Assalomu alaykum hurmatli {sms.from_user.full_name} ushbu bot zerikmaslik uchun yaratildi.\nYaratuvchi: Saminov Sardorbek\nBog'lanish uchun: @ilxamovic1")
        elif sms.text == "Bosh menu ga qaytish":
            rp = ReplyKeyboardBuilder()
            rp.add(KeyboardButton(text="🎲 Son Topish O'yini 🎲"), KeyboardButton(text="❗️ Info ❗️"))
            rp.adjust(1,1)
            await sms.answer(text="👇👇 Menulardan birini tanlang 👇👇", reply_markup=rp.as_markup())
        else:
            if sms.text == "+":
                self.left = self.num1 + 1
                self.num1 = randint(self.left, self.right)
                self.cnt1 += 1
                await sms.answer(text=f"Siz {self.num1} sonini o'yladingiz: To'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)??", reply_markup=ReplyKeyboardBuilder().add(KeyboardButton(text="+"),KeyboardButton(text="-"),KeyboardButton(text="To'g'ri")).adjust(2,1).as_markup())

            elif sms.text == "-":
                self.right = self.num1 - 1
                self.num1 = randint(self.left, self.right)
                self.cnt1 += 1
                await sms.answer(text=f"Siz {self.num1} sonini o'yladingiz: To'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)??", reply_markup=ReplyKeyboardBuilder().add(KeyboardButton(text="+"),KeyboardButton(text="-"),KeyboardButton(text="To'g'ri")).adjust(2,1).as_markup())

            elif sms.text == "START":
                await sms.answer(text=f"Siz {self.num1} sonini o'yladingiz: To'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)??", reply_markup=ReplyKeyboardBuilder().add(KeyboardButton(text="+"),KeyboardButton(text="-"),KeyboardButton(text="To'g'ri")).adjust(2,1).as_markup())
                
            elif sms.text == "To'g'ri":
                self.cnt1 += 1
                await sms.answer(text=f"Soningizni {self.cnt1} ta taxmin bilan topdim!!!")
                if self.cnt == self.cnt1:
                    await sms.answer(text=f"Durrang ikkimiz ham {self.cnt} ta taxmin bilan topdik!!")
                    self.cnt = 0
                    self.cnt1 = 0
                    self.chekt = 0
                    self.left = 1
                    self.right = 10
                elif self.cnt < self.cnt1:
                    await sms.answer(text=f"Siz {self.cnt} ta taxmin bilan topdingiz va yutdingiz!!")
                    self.cnt = 0
                    self.cnt1 = 0
                    self.chekt = 0
                    self.left = 1
                    self.right = 10
                else:
                    await sms.answer(text=f"Men {self.cnt1} ta taxmin bilan topdim va yutdim!!!")
                    self.cnt = 0
                    self.cnt1 = 0
                    self.chekt = 0
                    self.left = 1
                    self.right = 10
                self.num = randint(1, 10)
                await sms.answer(text="Tashrif uchun raxmat!!!", reply_markup=ReplyKeyboardBuilder().add(KeyboardButton(text="Bosh menu ga qaytish")).adjust(1).as_markup())
                

            elif sms.text.isdigit() and int(sms.text) < self.num:
                await sms.answer(text="Xato men o'ylagan son bundan kattaroq. Yana harakat qiling!")
                self.cnt += 1
            elif sms.text.isdigit() and int(sms.text) > self.num:
                await sms.answer(text="Xato men o'ylagan son bundan kichikroq. Yana harakat qiling!")
                self.cnt += 1
            elif sms.text.isdigit() and int(sms.text) == self.num:
                self.cnt += 1
                await sms.answer(text=f"TOPDINGIZ!!! {self.num} sonini o'ylagan edim {self.cnt} ta taxmin bilan topdingiz. Tabriklayman!!!")
                await sms.answer(text="1 dan 10 gacha son o'ylang. Men topishga harakat qilaman.")
                self.ckekt = 1
                st = ReplyKeyboardBuilder()
                st.add(KeyboardButton(text="START"))
                st.adjust(1)
                await sms.answer(text="Son o'ylagan bo'lsangiz START tugmasini bosing", reply_markup=st.as_markup())
            else:
                pass

    async def start(self):
        self.dp.message.register(self.start_command, Command(commands=["start"]))
        self.dp.message.register(self.eco)
        try:
            await self.dp.start_polling(self.bt)
        except:
            await self.bt.session.close()
        
if __name__ == "__main__":
    run(Gamebot().start())

