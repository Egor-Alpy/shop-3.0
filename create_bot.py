from aiogram import Bot, Dispatcher, executor
from config import token
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import database as db

# Экземпляр класса БД
data_base = db.DataBase()

# Временное хранилище
storage = MemoryStorage()

# инициализация бота
bot = Bot(token)
dp = Dispatcher(bot=bot,
                storage=storage)

