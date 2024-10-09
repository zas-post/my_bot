import logging
import requests
from aiogram import types, Router
from aiogram.filters import Command
from aiogram.types import Location
from environs import Env  # Импортируем environs для работы с переменными окружения
from lexicon.lexicon_ru import LEXICON_RU

# Инициализация логгера
logging.basicConfig(level=logging.INFO)

# Инициализация роутера
router = Router()

# Инициализация объекта Env и чтение переменных из .env файла
env = Env()
env.read_env()

# Чтение API ключа из переменной окружения
OPENWEATHER_API_KEY = env.str("OPENWEATHER_API_KEY", None)

# URL для запроса погоды
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

# Проверка наличия API ключа
if not OPENWEATHER_API_KEY:
    logging.error(
        "API ключ для OpenWeather не найден. Убедитесь, что переменная OPENWEATHER_API_KEY установлена в системе или .env файле."
    )
    raise ValueError("Отсутствует API ключ для OpenWeather. Завершение работы.")


@router.message(Command(commands=["weather"]))
async def request_location(message: types.Message):
    """
    Хендлер для команды /weather. Запрашивает у пользователя его местоположение.
    """
    await message.answer(text=LEXICON_RU["weather_request_location"])


@router.message(lambda message: message.location is not None)
async def get_weather_by_location(message: types.Message):
    """
    Хендлер для обработки геопозиции пользователя и получения погоды.
    """
    try:
        # Получаем координаты из сообщения
        location: Location = message.location
        latitude = location.latitude
        longitude = location.longitude

        # Логируем координаты
        logging.info(f"Получены координаты пользователя: {latitude}, {longitude}")

        # Параметры для запроса к OpenWeatherMap
        params = {
            "lat": latitude,
            "lon": longitude,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric",
            "lang": "ru",
        }

        # Выполняем запрос к OpenWeatherMap
        response = requests.get(WEATHER_URL, params=params)

        # Проверяем успешность запроса
        if response.ok:  # Используем .ok для проверки успешности запроса
            response_data = response.json()
            # Извлекаем нужную информацию из ответа
            city = response_data.get("name", "неизвестный город")
            temperature = response_data["main"]["temp"]
            weather_description = response_data["weather"][0]["description"]

            # Формируем текст сообщения с погодой
            weather_text = (
                f"Погода в городе {city}:\n"
                f"Температура: {temperature}°C\n"
                f"Описание: {weather_description.capitalize()}"
            )

            # Отправляем сообщение с погодой пользователю
            await message.answer(weather_text)

        else:
            # В случае ошибки логируем и отправляем сообщение пользователю
            logging.error(
                f"Ошибка при запросе погоды. Код ответа: {response.status_code}, Текст ошибки: {response.text}"
            )
            await message.answer(text=LEXICON_RU["weather_not_found"])

    except requests.RequestException as req_err:
        logging.error(f"Ошибка при выполнении HTTP-запроса: {req_err}", exc_info=True)
        await message.answer(
            "Произошла ошибка при запросе к серверу погоды. Попробуйте позже."
        )

    except Exception as e:
        # Логируем и отправляем сообщение об общей ошибке
        logging.error(f"Ошибка при обработке геолокации: {e}", exc_info=True)
        await message.answer(text=LEXICON_RU["weather_error"])
