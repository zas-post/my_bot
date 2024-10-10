from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from database.database import add_user

# Инициализируем роутер уровня модуля
router = Router()

# Список идентификаторов администраторов (например, из конфигурации)
admin_ids = []  # Замените на свой список admin_ids


# Функция для установки идентификаторов администраторов
def set_admin_ids(ids):
    global admin_ids
    admin_ids = ids


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    # Получаем имя пользователя или задаем "пользователь", если имя не указано
    username = message.from_user.username or "пользователь"
    first_name = message.from_user.first_name or ""
    last_name = message.from_user.last_name or ""

    # Проверяем, является ли пользователь администратором
    is_admin = (
        message.from_user.id in admin_ids
    )  # Проверяем, есть ли ID в списке администраторов

    # Добавляем пользователя в базу данных
    add_user(
        user_id=message.from_user.id,
        username=username,
        first_name=first_name,
        last_name=last_name,
        is_admin=is_admin,  # Устанавливаем is_admin в зависимости от проверки
    )

    # Формируем текст ответа, используя словарь с текстами
    await message.answer(text=LEXICON_RU["start"].format(username=username))
