import telebot
from telebot import types
import sqlite3
import os
from PIL import Image
import io

# Создание экземпляра бота с токеном для доступа к Telegram Bot
bot = telebot.TeleBot("7365269398:AAF6F49NOoo8WB_MeQL97zgBbfX1isYIba4")

# Создание кнопок для регистрации и авторизации
button = types.InlineKeyboardButton(text="GET USERS", callback_data="get users")
button_products = types.InlineKeyboardButton(text="GET PRODUCTS", callback_data="get products")
button_add = types.InlineKeyboardButton(text="ADD PRODUCT", callback_data="add product")
# Создание клавиатуры с кнопками
keyboard = types.InlineKeyboardMarkup(keyboard=[[button, button_products, button_add]])

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello! What do you want?', reply_markup=keyboard)

@bot.callback_query_handler(lambda callback: True)
def handle_callback(callback):
    if callback.data == 'get users':
        database = sqlite3.connect(os.path.abspath(os.path.join(__file__, '../../shop/data.db')))
        cursor = database.cursor()
        cursor.execute('SELECT * FROM user')
        list_users = cursor.fetchall()
        for user in list_users:
            bot.send_message(callback.message.chat.id, f'ID: {user[0]}\nNAME: {user[1]}\nPASSWORD: {user[3]}')

        database.close()
    elif callback.data == 'get products':
        database = sqlite3.connect(os.path.abspath(os.path.join(__file__, '../../shop/data.db')))
        cursor = database.cursor()
        cursor.execute('SELECT * FROM product')
        list_products = cursor.fetchall()
        for product in list_products:
            bot.send_message(callback.message.chat.id, f'ID: {product[0]}\nNAME: {product[1]}\nPRICE: {product[2]}')

        database.close()
    elif callback.data == 'add product':
        bot.send_message(callback.message.chat.id, 'Please enter the name of the product:')
        bot.register_next_step_handler(callback.message, process_name_step)

# Словарь для временного хранения данных пользователей
user_data = {}

def process_name_step(message):
    chat_id = message.chat.id
    # Сохранение введенного имени в словаре user_data
    user_data[chat_id] = {'name': message.text}
    # Запрос цены
    bot.send_message(chat_id, 'Please enter the price:')
    # Переход к следующему шагу - обработке цены
    bot.register_next_step_handler(message, process_price_step)

def process_price_step(message):
    chat_id = message.chat.id
    # Сохранение введенной цены в словаре user_data
    user_data[chat_id]['price'] = message.text
    # Запрос скидки
    bot.send_message(chat_id, 'Please enter the discount:')
    # Переход к следующему шагу - обработке скидки
    bot.register_next_step_handler(message, process_discount_step)

def process_discount_step(message):
    chat_id = message.chat.id
    # Сохранение введенной скидки в словаре user_data
    user_data[chat_id]['discount'] = message.text
    # Запрос цены со скидкой
    bot.send_message(chat_id, 'Please enter the discount price:')
    # Переход к следующему шагу - обработке цены со скидкой
    bot.register_next_step_handler(message, process_discount_price_step)

def process_discount_price_step(message):
    chat_id = message.chat.id
    # Сохранение введенной цены со скидкой в словаре user_data
    user_data[chat_id]['discount_price'] = message.text
    # Запрос на отправку изображения
    bot.send_message(chat_id, 'Please send the image of the product:')
    bot.register_next_step_handler(message, process_image_step)

def process_image_step(message):
    chat_id = message.chat.id
    # Сохранение изображения
    if message.content_type == 'photo':
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # Сохранение изображения в user_data
        user_data[chat_id]['image'] = downloaded_file
        save_product_to_database(chat_id)
    else:
        bot.send_message(chat_id, 'Please send a valid image.')

def save_product_to_database(chat_id):
    data = user_data[chat_id]
    # Получение абсолютного пути к базе данных
    database_path = os.path.abspath(os.path.join(__file__, '../../shop/data.db'))
    # Подключение к базе данных SQLite
    database = sqlite3.connect(database_path)
    cursor = database.cursor()

    # Вставка данных продукта в таблицу product
    cursor.execute('INSERT INTO product (name, price, discount, discount_price, image) VALUES (?, ?, ?, ?, ?)',
                   (data['name'], data['price'], data['discount'], data['discount_price'], data['image']))
    database.commit()  # Сохранение изменений в базе данных
    database.close()  # Закрытие соединения с базой данных

    # Уведомление пользователя о успешном сохранении данных
    bot.send_message(chat_id, 'Your product has been saved successfully.')

    # Удаление данных пользователя из временного хранилища
    del user_data[chat_id]
# Запуск бота
bot.polling(none_stop=True)
