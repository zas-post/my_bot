# handlers/admin_handlers.py
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.admin_keyboards import admin_panel_keyboard
from database.database import get_all_users
from environs import Env
import logging
import asyncio

# Инициализация Router и Env
router = Router()
env = Env()
env.read_env()

# Получаем список админов из .env файла
admin_ids = env.list("ADMIN_IDS", subcast=int)

# Инициализация логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Декоратор для проверки прав администратора
def admin_only(handler):
    async def wrapper(message: types.Message):
        if message.from_user.id not in admin_ids:
            await message.answer(LEXICON_RU["access_denied"])
            return
        return await handler(message)

    return wrapper


# Состояние FSM для управления рассылкой
class BroadcastStates(StatesGroup):
    waiting_for_message = State()


# Функция для рассылки сообщений пользователям
async def broadcast_message_to_users(message, users, message_text):
    tasks = [
        message.bot.send_message(chat_id=user[0], text=message_text) for user in users
    ]
    await asyncio.gather(*tasks, return_exceptions=True)


# Хэндлер для команды /admin
@router.message(Command(commands="admin"))
@admin_only
async def admin_panel(message: types.Message):
    keyboard = admin_panel_keyboard()
    await message.answer(LEXICON_RU["/admin"], reply_markup=keyboard)


# Общая функция для обработки действий администратора
async def process_admin_callback(callback: types.CallbackQuery, action: str):
    if action == "stats":
        users = get_all_users()
        stats_message = (
            f"Всего пользователей: {len(users)}"
            if users
            else LEXICON_RU["no_users_found"]
        )
        await callback.message.edit_text(
            stats_message, reply_markup=admin_panel_keyboard()
        )
    elif action == "user_list":
        users = get_all_users()
        if users:
            user_list = "\n".join(
                [
                    f"{idx + 1}. {user[1]} (ID: {user[0]})"
                    for idx, user in enumerate(users)
                ]
            )
            await callback.message.edit_text(
                text=f"{LEXICON_RU['user_list_message']}\n{user_list}",
                reply_markup=admin_panel_keyboard(),
            )
        else:
            await callback.message.edit_text(
                text=LEXICON_RU["no_users_found"], reply_markup=admin_panel_keyboard()
            )
    await callback.answer()


# Обработчик для кнопки "📊 Статистика"
@router.callback_query(lambda c: c.data == "stats")
@admin_only
async def show_statistics(callback: types.CallbackQuery):
    await process_admin_callback(callback, "stats")


# Обработчик для кнопки "👥 Список пользователей"
@router.callback_query(lambda c: c.data == "user_list")
@admin_only
async def show_user_list(callback: types.CallbackQuery):
    await process_admin_callback(callback, "user_list")


# Обработчик для кнопки "📤 Отправить рассылку"
@router.callback_query(lambda c: c.data == "send_broadcast")
@admin_only
async def send_broadcast(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(LEXICON_RU["broadcast_prompt"], reply_markup=None)
    await callback.answer()
    await state.set_state(BroadcastStates.waiting_for_message)


# Обработчик для получения сообщения рассылки от администратора
@router.message(BroadcastStates.waiting_for_message)
@admin_only
async def get_broadcast_message(message: types.Message, state: FSMContext):
    broadcast_message = message.text
    users = get_all_users()

    if not users:
        await message.answer(LEXICON_RU["no_users_found"])
        await state.clear()
        return

    # Передаем объект message в функцию
    await broadcast_message_to_users(message, users, broadcast_message)

    await message.answer(LEXICON_RU["broadcast_successful"])
    await state.clear()


# Обработчик для кнопки "❌ Закрыть"
@router.callback_query(lambda callback: callback.data == "close")
@admin_only
async def close_admin_panel(callback: types.CallbackQuery):
    await callback.message.edit_text(
        LEXICON_RU["admin_panel_closed"], reply_markup=None
    )
    await callback.answer()
