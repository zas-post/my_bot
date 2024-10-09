import logging
from aiogram import types, Router
from aiogram.filters import Command
from lexicon.lexicon_ru import LEXICON_RU

# Инициализация роутера
router = Router()


# Хендлер для команды /info
@router.message(Command(commands=["info"]))
async def send_info(message: types.Message):
    """
    Хендлер для команды /info. Отправляет информацию о боте и его функционале.
    """
    try:
        await message.answer(LEXICON_RU["info"])
    except Exception as e:
        logging.error(f"Ошибка в хендлере /info: {e}", exc_info=True)
        await message.answer(LEXICON_RU["error"])
