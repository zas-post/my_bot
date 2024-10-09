# handlers/translator_service.py
from aiogram import types, Router
from aiogram.filters import Command
from aiogram.types import Message
from deep_translator import GoogleTranslator
from lexicon.lexicon_ru import LEXICON_RU
import logging

# Инициализация роутера
router = Router()

# Настроим логирование
logging.basicConfig(level=logging.INFO)

# Поддерживаемые языки
SUPPORTED_LANGUAGES = {
    "en": "английский",
    "pl": "польский",
    "fr": "французский",
    "de": "немецкий",
    "es": "испанский",
}


# Хендлер на команду /translate_help
@router.message(Command(commands="translate_help"))
async def process_translate_help_command(message: Message):
    # Отправляем пользователю текст с описанием функционала перевода
    await message.answer(text=LEXICON_RU["translate_help"])


@router.message(
    lambda message: message.text.startswith("!") or message.text.startswith("переведи ")
)
async def translate_text(message: types.Message):
    """Обработчик для перевода текста на указанный язык."""
    # Логируем начало обработки
    logging.info(f"Получено сообщение для перевода: {message.text}")

    try:
        text_to_translate = ""
        target_language = "pl"  # Язык по умолчанию — польский

        # Определяем целевой язык и текст для перевода
        if message.text.startswith("!"):
            parts = message.text[1:].strip().split(" ", 1)
            if len(parts) == 2 and parts[0] in SUPPORTED_LANGUAGES:
                target_language, text_to_translate = parts[0], parts[1]
            else:
                text_to_translate = parts[0]
        elif message.text.lower().startswith("переведи на "):
            parts = message.text[len("переведи на ") :].strip().split(" ", 1)
            if len(parts) == 2 and parts[0] in SUPPORTED_LANGUAGES:
                target_language, text_to_translate = parts[0], parts[1]

        # Проверяем, что текст для перевода не пустой
        if not text_to_translate:
            await message.reply("Текст для перевода не должен быть пустым.")
            logging.warning("Пустой текст для перевода.")
            return

        # Логируем начало перевода
        logging.info(
            f"Начинаем перевод текста: '{text_to_translate}' на язык: '{target_language}'"
        )

        # Переводим текст на указанный язык
        translated = GoogleTranslator(source="auto", target=target_language).translate(
            text_to_translate
        )

        # Логируем переведённый текст
        logging.info(f"Переведенный текст: {translated}")

        # Отправляем переведённый текст обратно пользователю
        await message.reply(
            f"<i>Перевод на {SUPPORTED_LANGUAGES.get(target_language, target_language)}:</i>  <b>{translated}</b>"
        )

    except Exception as e:
        # Логируем ошибку с выводом стека
        logging.error(f"Ошибка при переводе текста: {e}", exc_info=True)
        await message.reply("Произошла ошибка при переводе текста.")
