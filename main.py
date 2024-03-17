from create_bot import *
from handlers import *

async def on_startup(_):
    print("- - - BOT IS RUNNING - - -")

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
callback.register_handlers_callback(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)


# редактирование БД software
# Обработка несуществующего названия (исключения)