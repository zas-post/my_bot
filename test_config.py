# test_config.py
from config_data.config import load_config

if __name__ == "__main__":
    config = load_config(".env")
    print("Bot Token:", config.tg_bot.token)
    print("Admin IDs:", config.tg_bot.admin_id)
    print("Database File:", config.db.db_file)
