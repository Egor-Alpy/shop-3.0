from create_bot import *
from handlers import *
from config import *

async def on_startup(_):
    print("- - - BOT IS RUNNING - - -")
    await bot.set_my_commands(bot_commands_client)


other.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
client.register_handlers_client(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)


# редактирование БД software
# Обработка несуществующего названия (исключения)
