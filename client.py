




"""######################################       MAIN FUNC       ###########################################"""
from aiogram import types
from create_bot import dp
import keyboards as kb


@dp.message_handler(commands=['start'])
async def test(message: types.Message):
    await message.delete()
    await message.answer("*Здравствуйте! Нажмите на /menu, чтобы начать работу с ботом*", parse_mode='markdown')
    # добавляем\проверяем пользователя в БД
    user_id = message.from_user.id
    name = message.from_user.first_name
    data_base.adduser(user_id, name, message)


@dp.message_handler(commands=['menu'])
async def startf(message: types.Message):
    await message.answer(f'*Добро пожаловать!*',
                         parse_mode='markdown',
                         reply_markup=kb.menu_markup)

@dp.message_handler(commands=['cancel'], state="*")
async def cmd_cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.answer('*Выполнена отмена*', parse_mode='markdown')
    await state.finish()


@dp.message_handler()
async def main(message: types.Message):
    if __name__ == '__main__':
        await message.reply('Да я тебя отечаю!!!!')
