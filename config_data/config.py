import logging
from dataclasses import dataclass
from environs import Env
import re

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Константы для значений по умолчанию
DEFAULT_DB_FILE = "database/database.db"


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список ID администраторов


@dataclass
class DbConfig:
    db_file: str  # Путь к файлу базы данных


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig  # Параметры базы данных


def load_config(path: str | None = None) -> Config:
    """Загрузка конфигурации из .env файла"""
    env = Env()
    env.read_env(path)

    # Загружаем параметры бота
    token = env.str("BOT_TOKEN", "")
    if not token:
        logger.error("Переменная окружения BOT_TOKEN не установлена.")
        raise ValueError("BOT_TOKEN is not set in the environment variables.")

    # Проверка валидности токена (длина ID бота 9-10 цифр и длина второй части 35 символов)
    if not re.match(r"^[0-9]{9,10}:[a-zA-Z0-9_-]{35}$", token):
        logger.error("Неверный формат BOT_TOKEN.")
        raise ValueError("Invalid BOT_TOKEN format in the environment variables.")

    # Загружаем список ID администраторов из переменной окружения
    admin_ids = env.list("ADMIN_IDS", [])

    # Преобразование в целые числа и удаление пустых строк
    admin_ids_int = list(
        filter(
            lambda x: isinstance(x, int),
            map(lambda x: int(x.strip()) if x.strip().isdigit() else None, admin_ids),
        )
    )

    # Дополнительная проверка: если список администраторов пуст
    if not admin_ids_int:
        logger.error("Список ADMIN_IDS пуст или содержит неверные значения.")
        raise ValueError(
            "ADMIN_ID list is empty or invalid. Please check your .env configuration."
        )

    # Загружаем параметры базы данных
    db_file = env.str("DB_FILE", DEFAULT_DB_FILE)  # Путь к базе данных по умолчанию

    logger.info("Конфигурация успешно загружена.")
    # Возвращаем объект Config с параметрами бота и базы данных
    return Config(
        tg_bot=TgBot(
            token=token,
            admin_ids=admin_ids_int,
        ),
        db=DbConfig(db_file=db_file),
    )
