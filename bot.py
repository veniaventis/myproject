import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('static/welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Kaljanai✴")
	item2 = types.KeyboardButton("Tabakas☁")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, 'Sveiki atvykę, <b>{0.first_name}</b>, į tamsiąją kaljanų pusę!\n Aš - <b>{1.first_name}</b>, padėsiu jums pasirinkti.\n Pasirinkite kategoriją:'.format(message.from_user, bot.get_me()),
	parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == "Kaljanai✴":

			markup = types.InlineKeyboardMarkup(row_width=1)
			item1 = types.InlineKeyboardButton("Like Smoke Steel Wood 🌴", "https://telegra.ph/Like-Smoke-Steel-Wood-09-06", callback_data='good')

			markup.add(item1)

			bot.send_message(message.chat.id, 'Pažiūrėk, ką turime:', reply_markup=markup)

		elif message.text == 'Tabakas☁':

			markup = types.InlineKeyboardMarkup(row_width=1)
			item1 = types.InlineKeyboardButton("DarkSide","https://telegra.ph/DarkSide-09-06", callback_data='good')

			markup.add(item1)

			bot.send_message(message.chat.id, 'Pažiūrėk, ką turime:', reply_markup=markup)
		else:
			bot.send_message(message.chat.id, 'ia xz:D')



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")
 
    except Exception as e:
        print(repr(e))
#RUN
bot.polling(none_stop=True)