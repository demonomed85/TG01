import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=["help"]))
async def cmd_help(message: Message):
    await message.answer("Доступные команды: \n /start \n /help")

@dp.message(Command(commands=["start"]))
async def cmd_start(message: Message):
    await message.answer("Hello!")
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())