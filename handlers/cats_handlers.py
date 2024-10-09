import logging
import requests
from aiogram import types, Router
from aiogram.filters import Command

# URL для запроса картинок котиков
API_CATS_URL = "https://api.thecatapi.com/v1/images/search"

# Текст сообщения при ошибке
ERROR_TEXT = "😿 К сожалению, не удалось получить картинку с котиком. Попробуйте позже!"

# Инициализация роутера
router = Router()


@router.message(Command(commands=["cat"]))
async def send_cat_picture(message: types.Message):
    """
    Хендлер для команды /cat. Отправляет случайную картинку с котиком.
    """
    try:
        # Синхронный запрос к API для получения случайной картинки котика
        response = requests.get(API_CATS_URL)

        # Проверка успешности запроса
        if response.status_code == 200:
            cat_data = response.json()
            cat_link = cat_data[0]["url"]

            # Отправка картинки пользователю
            await message.answer_photo(photo=cat_link)
        else:
            # Логируем ошибку и отправляем сообщение пользователю
            logging.error(f"Ошибка при запросе к API котиков: {response.status_code}")
            await message.answer(ERROR_TEXT)

    except Exception as e:
        # Логируем исключение и отправляем сообщение об ошибке
        logging.error(f"Ошибка в хендлере котиков: {e}", exc_info=True)
        await message.answer(ERROR_TEXT)
