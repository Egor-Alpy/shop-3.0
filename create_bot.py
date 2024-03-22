from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import FSMContext

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

# проверка машины состояния
async def cancel_check(message, state: FSMContext):
    current_state = await state.get_state()
    if message.text[0] == '/' and current_state != None:
        await state.finish()
    else:
        return

def check_class(msg):
    if type(msg) == int or type(msg) == float:
        return True
    return False