from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import LEXICON_RU  # Импортируем лексикон


# Функция для создания клавиатуры админ-панели
def admin_panel_keyboard() -> InlineKeyboardMarkup:
    """Создает и возвращает клавиатуру для админ-панели."""
    keyboard = InlineKeyboardBuilder()

    # Задаем текст кнопок
    stats_button_text = f"📊 {LEXICON_RU['stats_message']}"
    user_list_button_text = f"👥 {LEXICON_RU['user_list_message']}"
    broadcast_button_text = f"📤 {LEXICON_RU['broadcast_prompt']}"
    close_button_text = f"❌ {LEXICON_RU['admin_panel_closed']}"

    # Добавляем кнопки с текстом и callback данными
    keyboard.button(text=stats_button_text, callback_data="stats")
    keyboard.button(text=user_list_button_text, callback_data="user_list")
    keyboard.button(text=broadcast_button_text, callback_data="send_broadcast")
    keyboard.button(text=close_button_text, callback_data="close")

    # Преобразуем генератор кнопок в список и определяем количество столбцов
    buttons_list = list(keyboard.buttons)  # Преобразование генератора в список
    num_columns = min(len(buttons_list), 2)
    keyboard.adjust(num_columns)  # Автоматическое распределение по столбцам

    # Возвращаем объект клавиатуры
    return keyboard.as_markup()
