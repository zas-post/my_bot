# utils.py

from aiogram import types

# Проверка, что сообщение содержит текст
def is_text_message(message: types.Message) -> bool:
    return message.text is not None
