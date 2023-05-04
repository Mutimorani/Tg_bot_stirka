from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import TOKEN
from pars import res

bot = Bot(TOKEN)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)  # one time mean close after using any button
b1 = KeyboardButton('/stirka')
kb.add(b1)

async def on_startup(_):
    print('Бот был успешно запущен')

@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    user_name = message.from_user.first_name
    await bot.send_message(message.from_user.id,
                           f'Здравствуй, {user_name}',
                           parse_mode="HTML",
                           reply_markup=kb)

@dp.message_handler(commands=['stirka'])
async def send_kb(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text='\n'.join(res), parse_mode='HTML')
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)