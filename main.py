from aiogram import Dispatcher, executor, Bot, types
import sqlite3 as sq
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text

from aiogram.dispatcher import FSMContext
import keyboards as kb
import database as db
from config import *
from StatesGroups import *
from create_bot import *


async def on_startup(_):
    print("- - - BOT IS RUNNING - - -")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)


# редактирование БД software
# Обработка несуществующего названия (исключения)