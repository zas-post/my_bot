# handlers/greeting_handlers.py
import logging
import json
import re
from aiogram import types, Router
from lexicon.lexicon_ru import LEXICON_RU

router = Router()

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Загрузка ругательств из файла profanities.json и создание регулярного выражения
try:
    with open("lexicon/profanities.json", "r", encoding="utf-8") as f:
        profanities_data = json.load(f)
        profanities = set(word.lower() for word in profanities_data["profanities"])
        # Создаем регулярное выражение для поиска всех ругательств
        profanity_pattern = re.compile(
            r"\b(" + "|".join(re.escape(word) for word in profanities) + r")\b",
            re.IGNORECASE,
        )
except Exception as e:
    logging.error(f"Ошибка при загрузке ругательств: {e}")
    profanities = set()
    profanity_pattern = None


def censor_profanity(text: str) -> str:
    """Цензурирует ругательства, заменяя их на звёздочки с помощью регулярного выражения."""
    if not profanity_pattern:
        return text

    def replace_with_stars(match):
        """Заменяет найденное слово на звёздочки."""
        word = match.group(0)
        logging.info(f"Заменяем '{word}' на {'*' * len(word)}")
        return "*" * len(word)

    # Заменяем все найденные ругательства в тексте
    return profanity_pattern.sub(replace_with_stars, text)


@router.message(
    lambda message: message.text
    and any(greeting in message.text.lower() for greeting in LEXICON_RU["greetings"])
)
async def handle_greetings(message: types.Message):
    """Обрабатывает приветствия и отвечает с именем пользователя."""
    logging.info(
        f"Приветствие получено от пользователя {message.from_user.id} ({message.from_user.username})."
    )

    # Получаем имя пользователя или используем "пользователь", если имя отсутствует
    username = message.from_user.username or "пользователь"

    # Формируем ответ с приветствием и именем пользователя
    reply_message = f"<b>Привет</b>, @{username}!\n{LEXICON_RU['what_can_do']}"
    await message.reply(reply_message)


@router.message(lambda message: message.text is not None)
async def handle_all_messages(message: types.Message):
    """Обрабатывает все текстовые сообщения и заменяет ругательства на звёздочки."""

    # Игнорируем пустые сообщения
    if message.text.strip() == "":
        return  # Не обрабатываем пустые сообщения

    logging.info(
        f"Получено сообщение от {message.from_user.id} ({message.from_user.username}): {message.text}"
    )

    # Проверяем на ругательства и заменяем их
    censored_message = censor_profanity(message.text)

    # Если сообщение содержит ругательства, заменяем и отвечаем
    if censored_message != message.text:
        await message.reply(censored_message)
        logging.info(f"Отправлено сообщение с цензурой: {censored_message}")
