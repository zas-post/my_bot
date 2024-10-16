LEXICON_RU: dict[str, str] = {
    # start
    "start": (
        "<b>👋 Привет, {username}!</b>\n\n"
        "Я бот, который поможет вам узнать <b>погоду</b> в вашем городе, получить случайное "
        "<i>изображение котика</i> или воспользоваться другими <u>полезными командами</u>.\n\n"
        "<b>🛠 Основные команды для начала работы:</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "- <b>/weather</b> — Узнать погоду в вашем местоположении 🌤 <i>(работает в мобильной версии приложения)</i>\n"
        "- <b>/cat</b> — Получить картинку с котиком 🐱\n"
        "- <b>/translate_help</b> — <u>Инструкция по использованию перевода</u> 📚\n"
        "- <b>/info</b> — Узнать больше о боте и его функционале ℹ️\n"
        "- <b>/help</b> — Показать список всех доступных команд ❓\n"
        "- <b>/about</b> — Информация о версии и разработчике бота 👨‍💻\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "Если возникнут вопросы, воспользуйтесь командой <b>/help</b> или напишите мне в личные сообщения."
    ),
    "info": (
        "<b>Этот бот предоставляет доступ к различным функциям:</b>\n\n"
        "<i>Вот, что я умею:</i>\n"
        "- <b>/start</b> — <u>Начало работы с ботом</u>\n"
        "- <b>/help</b> — <u>Справка по командам ❓</u>\n"
        "- <b>/weather</b> — Узнать погоду в вашем местоположении <i>(работает в мобильной версии приложения)</i> 🌤\n"
        "- <b>/cat</b> — Получить случайную <i>картинку с котиком 🐱</i>\n"
        "- <b>/translate_help</b> — <u>Инструкция по использованию перевода</u> 📚\n"
        "- <b>/info</b> — Узнать больше о <u>возможностях бота ℹ️</u>\n"
        "- <b>/about</b> — Информация о <u>версии</u> и <u>разработчике</u> бота 👨‍💻\n\n"
        "<b>💬 Используйте команды, чтобы начать взаимодействие!</b>\n"
        "<b>Если возникнут вопросы, не стесняйтесь <i>написать</i> мне!</b>"
    ),
    "help": (
        "<b>🛠️ Список доступных команд:</b>\n\n"
        "- <b>/start</b> — <u>Начало работы с ботом</u>\n"
        "- <b>/info</b> — <u>Информация о боте</u> и его возможностях ℹ️\n"
        "- <b>/weather</b> — Узнать погоду в вашем <b>текущем местоположении</b> <i>(работает в мобильной версии приложения)</i> 🌤\n"
        "- <b>/cat</b> — Получить случайную <i>картинку с котиком 🐱</i>\n"
        "- <b>/translate_help</b> — <u>Инструкция по использованию перевода</u> 📚\n"
        "- <b>/about</b> — <u>Информация о версии</u> и <u>разработчике</u> бота 👨‍💻\n"
        "- <b>/help</b> — <i>Вывести это сообщение помощи ❓</i>\n\n"
        "<b>💬 Если у вас есть вопросы, не стесняйтесь <i>написать</i> мне!</b>"
    ),
    "about": (
        "<b>📜 Информация о боте:</b>\n\n"
        "<i>Этот бот создан для упрощения взаимодействия с различными функциями, такими как погода, изображения котиков и многое другое.</i>\n\n"
        "<b>🌟 Версия:</b> 1.1.0\n"
        "<b>👨‍💻 Разработчик:</b> Alexander\n\n"
        "<b>💬 Если у вас есть вопросы или предложения, не стесняйтесь <i>написать</i> мне!</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "© 2024 My Own Company"
    ),
    "translate_help": (
        "<b>Инструкция по использованию перевода:</b>\n\n"
        "Для перевода введите <b>!</b> и <b>текст</b> или <b>переведи</b> и <b>текст</b>.\n\n"
        "<b>Поддерживаемые языки:</b>\n"
        "- <b>en</b>: английский\n"
        "- <b>pl</b>: польский\n"
        "- <b>fr</b>: французский\n"
        "- <b>de</b>: немецкий\n"
        "- <b>es</b>: испанский\n\n"
        "По умолчанию перевод осуществляется на <b>польский</b> язык.\n\n"
        "Если нужно перевести на другой язык, то используйте формат:\n"
        "<b>!en Привет, как дела?</b> или <b>переведи на en Привет, как дела?</b>"
    ),
    "what_can_do": (
        "\nЯ могу:\n"
        "- Реагировать на приветствия и обращаться к вам по имени.\n"
        "- Отвечать на команды /start и /help, чтобы помочь вам начать работу.\n"
        "- Выполнять ваши команды, помогая находить нужную информацию и отвечая на вопросы.\n"
        "- Переводить текст: просто отправьте <b>!</b> и <b>текст</b> или <b>переведи</b> и <b>текст</b>, и я предоставлю вам перевод.\n"
        "- Информировать о погоде: отправьте своё местоположение, и я сообщу вам текущую погоду <i>(работает в мобильной версии приложения)</i>.\n\n"
        "Для получения информации о том, что я умею, просто напишите /help."
    ),
    "welcome_message": (
        "Привет! Я бот, и я могу работать в групповом чате. Я могу:"
        "- Реагировать на приветствия и обращаться к вам по имени."
        "- Отвечать на команды /start и /help для получения информации о моих функциях."
        "- Выполнять различные команды, включая получение погоды и переводы текстов."
        "- Помогать в чате, отвечая на ваши вопросы.\n"
        "Для получения информации о том, что я умею, просто напишите /help."
    ),
    "weather_request_location": (
        "Пожалуйста, отправьте своё местоположение, чтобы узнать погоду в вашем городе.\n"
        "Для этого нажмите на скрепку и выберите 'Геопозиция'.\n"
        "Это поможет мне предоставить вам наиболее точные данные о погоде."
    ),
    "error": "Произошла ошибка. Пожалуйста, попробуйте позже.",
    "unknown_command": "Извините, я не понимаю эту команду. Введите /help для получения списка доступных команд.",
    "no_echo": "Данный тип апдейтов не поддерживается методом send_copy",
    # Сообщения для админ-панели
    "/admin": "Добро пожаловать в Admin-панель!",
    "admin_panel_closed": "Админ-панель закрыта.",
    "admin_no_access": "У вас нет прав для доступа к админ-панели.",
    "access_denied": "У вас нет прав доступа к этой команде.",
    "stats_message": "Статистика: 100 пользователей.",
    "user_list_message": "Список пользователей:\n1. User1\n2. User2",  # Статический пример списка пользователей
    "broadcast_prompt": "Введите сообщение для рассылки:",
    "broadcast_successful": "Сообщение успешно разослано всем пользователям!",  # Ключ для успешной рассылки
    "no_database_connection": "Нет подключения к базе данных.",
    "no_users_found": "Пользователи не найдены.",
    "greetings": [
        "привет",
        "здравствуй",
        "добрый день",
        "доброе утро",
        "добрый вечер",
        "hello",
        "hi",
    ],
    "weather_error": ("Произошла ошибка при определении погоды. Попробуйте позже."),
    "weather_not_found": ("Не удалось получить информацию о погоде. Попробуйте позже."),
}
