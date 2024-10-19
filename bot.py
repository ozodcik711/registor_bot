# import asyncio
# import logging
# import sys
# from aiogram import Bot, Dispatcher, F
# from aiogram.filters import CommandStart, Command
# from aiogram.types import Message
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.storage.memory import MemoryStorage
# from states import Registor

# TOKEN = "8063090121:AAF2TD8jL-HMMho2KS4QPr57D0zxyk8g4Xk"
# ADMIN_ID = [6598593846]

# # Bot va Dispatcher obyektini yaratish
# bot = Bot(TOKEN)
# dp = Dispatcher(storage=MemoryStorage())

# # /start komandasi uchun handler
# @dp.message(CommandStart())
# async def command_start_handler(message: Message, state: FSMContext):
#     full_name = message.from_user.full_name
#     text = f"Salom {full_name}, Ro'yxatdan o'tish botga hush kelibsiz!"
#     await message.answer(text)
#     # Ro'yxatdan o'tishni boshlash
#     await register(message, state)

# # Ro'yxatdan o'tish jarayonini boshlash
# async def register(message: Message, state: FSMContext):
#     await message.answer("Ro'yxatdan o'tish uchun ma'lumotlarni kiriting!\nIsmingizni kiriting:")
#     await state.set_state(Registor.ism)

# # Ism kiritish
# @dp.message(F.text, Registor.ism)
# async def register_ism(message: Message, state: FSMContext):
#     ism = message.text
#     await state.update_data(name=ism)
#     await state.set_state(Registor.familiya)
#     await message.answer("Familiyangizni kiriting:")

# # Agar ism noto'g'ri formatda bo'lsa
# @dp.message(Registor.ism)
# async def register_ism_del(message: Message, state: FSMContext):
#     await message.delete()
#     await message.answer(text="Ismingizni to'g'ri kiriting ❗️")

# # Familiya kiritish
# @dp.message(F.text, Registor.familiya)
# async def register_familiya(message: Message, state: FSMContext):
#     familiya = message.text
#     await state.update_data(surname=familiya)
#     await state.set_state(Registor.yosh)
#     await message.answer("Yoshingizni kiriting:")

# # Yosh kiritish
# @dp.message(F.text, Registor.yosh)
# async def register_yosh(message: Message, state: FSMContext):
#     yosh = message.text
#     await state.update_data(age=yosh)
#     await state.set_state(Registor.tel)
#     await message.answer("Telefon raqamingizni kiriting:")

# # Telefon raqamini tekshirish va kiritish
# @dp.message(F.text.regexp(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"), Registor.tel)
# async def register_tel(message: Message, state: FSMContext):
#     tel = message.text
#     await state.update_data(tel=tel)
#     await state.set_state(Registor.kurs)
#     await message.answer("Kurs nomini kiriting:")

# # Telefon raqami noto'g'ri formatda bo'lsa
# @dp.message(Registor.tel)
# async def register_tel_del(message: Message, state: FSMContext):
#     await message.delete()
#     await message.answer(text="Telefon raqamni to'g'ri kiriting ❗️")

# # Kurs nomini kiritish va ma'lumotlarni tasdiqlash
# @dp.message(F.text, Registor.kurs)
# async def register_kurs(message: Message, state: FSMContext):
#     data = await state.get_data()

#     ism = data.get("name")
#     familiya = data.get("surname")
#     yosh = data.get("age")
#     tel = data.get("tel")
#     kurs = message.text

#     text = f"Ism: {ism}\nFamiliya: {familiya}\nYosh: {yosh}\nTelefon: {tel}\nKurs: {kurs}"
#     await message.answer("Siz ro'yxatdan o'tdingiz!")

#     for admin in ADMIN_ID:
#         await bot.send_message(chat_id=admin, text=text)

#     await state.clear()

# # Bot ishga tushirilganda
# @dp.startup()
# async def bot_start():
#     for admin in ADMIN_ID:
#         await bot.send_message(admin, "Tabriklaymiz 🎉\nBotimiz ishga tushdi!")

# # Bot to'xtatilganda
# @dp.shutdown()
# async def bot_shutdown():
#     for admin in ADMIN_ID:
#         await bot.send_message(admin, "Bot to'xtadi ❗️")

# # Asosiy funksiya
# async def main():
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())
