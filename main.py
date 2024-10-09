import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config_data.config import Config, load_config


from handlers import (
    start_handlers,
    help_handlers,
    info_handlers,
    about_handlers,
    admin_handlers,
    translate_handler,
    greeting_handlers,
    weather_handler,
    cats_handlers,
)


# Функция конфигурирования и запуска бота
async def main():
    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher(storage=MemoryStorage())

    # Регистрируем роутеры в диспетчере
    dp.include_router(start_handlers.router)
    dp.include_router(help_handlers.router)
    dp.include_router(info_handlers.router)
    dp.include_router(about_handlers.router)
    dp.include_router(weather_handler.router)
    dp.include_router(translate_handler.router)
    dp.include_router(admin_handlers.router)
    dp.include_router(cats_handlers.router)
    dp.include_router(greeting_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        await dp.storage.close()


if __name__ == "__main__":
    asyncio.run(main())
