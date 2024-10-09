from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

# Инициализируем роутер уровня модуля
router = Router()


# Хендлер на команду /about
@router.message(Command(commands="about"))
async def process_about_command(message: Message):
    # Отправляем пользователю информацию о боте
    await message.answer(text=LEXICON_RU["about"])
