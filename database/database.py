import sqlite3
from contextlib import closing

# Путь к файлу базы данных
DB_PATH = "database/database.db"


# Функция для инициализации базы данных и создания таблиц, если их еще нет
def initialize_database():
    try:
        with closing(sqlite3.connect(DB_PATH)) as conn, closing(
            conn.cursor()
        ) as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    is_admin INTEGER DEFAULT 0  -- Использование INTEGER вместо BOOLEAN
                )
                """
            )
            conn.commit()
    except sqlite3.Error as e:
        print(f"Ошибка при инициализации базы данных: {e}")


# Функция для добавления нового пользователя в базу данных
def add_user(
    user_id: int, username: str, first_name: str, last_name: str, is_admin: bool = False
):
    try:
        # Преобразуем логическое значение is_admin в целое число (1 для True и 0 для False)
        is_admin_int = int(is_admin)

        with closing(sqlite3.connect(DB_PATH)) as conn, closing(
            conn.cursor()
        ) as cursor:
            cursor.execute(
                """
                INSERT OR IGNORE INTO users (user_id, username, first_name, last_name, is_admin)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    user_id,
                    username,
                    first_name,
                    last_name,
                    is_admin_int,
                ),  # Используем преобразованное значение
            )
            conn.commit()
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении пользователя в базу данных: {e}")


# Функция для получения списка всех пользователей
def get_all_users():
    try:
        with closing(sqlite3.connect(DB_PATH)) as conn, closing(
            conn.cursor()
        ) as cursor:
            cursor.execute(
                "SELECT user_id, username, first_name, last_name, is_admin FROM users"
            )
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Ошибка при получении списка пользователей: {e}")
        return []  # Возвращаем пустой список в случае ошибки
