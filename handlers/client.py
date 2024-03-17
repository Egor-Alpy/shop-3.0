from aiogram import types
from aiogram.dispatcher import FSMContext
from create_bot import *
import keyboards as kb

"""######################################       MAIN FUNC       ###########################################"""

# @dp.message_handler(commands=['start'])
async def startf(message: types.Message):
    await message.delete()
    await message.answer("*Здравствуйте! Нажмите на /menu, чтобы начать работу с ботом*", parse_mode='markdown')
    # добавляем\проверяем пользователя в БД
    user_id = message.from_user.id
    name = message.from_user.first_name
    data_base.adduser(user_id, name, message)


# @dp.message_handler(commands=['menu'])
async def menuf(message: types.Message):
    await message.answer(f'*Добро пожаловать!*',
                         parse_mode='markdown',
                         reply_markup=kb.menu_markup)

# @dp.message_handler(commands=['cancel'], state="*")
async def cmd_cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.answer('*Выполнена отмена*', parse_mode='markdown')
    await state.finish()


# @dp.message_handler()
async def main_function(message: types.Message):
    if __name__ == '__main__':
        await message.reply('Да я тебя отечаю!!!!')

a = [menuf, cmd_cancel]
def register_handlers_client(dp: Dispatcher):
    print('ossk')
    dp.register_message_handler(startf, commands=['start'])
    dp.register_message_handler(menuf, commands=['menu'])
    dp.register_message_handler(main_function, content_types=['text'])
