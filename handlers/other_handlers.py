from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

# Инициализируем роутер уровня модуля
router = Router()


# Этот хэндлер будет срабатывать на любые сообщения,
# кроме команд "/start" и "/help"
@router.message()
async def send_echo(message: Message):
    try:
        # Отправляем копию сообщения обратно в тот же чат
        await message.send_copy(chat_id=message.chat.id)
    except Exception as e:
        # В случае ошибки отправляем сообщение пользователю
        await message.reply(
            text=LEXICON_RU.get(
                "no_echo", "Произошла ошибка при обработке вашего сообщения."
            )
        )
