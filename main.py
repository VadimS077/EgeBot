import random
from urllib.parse import urlencode

from aiogram.types import message

from music import musicplay
import requests
import telebot
import urllib3

from config import *
from reshuege.academic_subjects import *
from reshuege.headers import headers
from reshuege.parser import parse_themes
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN, parse_mode=None)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет,я телеграмм-бот для ЕГЭ.Мои функции-Тренировка и специально подобранная музыка для учебы.Чтобы воспользоваться мной,открой меню возле ввода сообщения")
@bot.message_handler(commands=['preparing'])
def prepare(message):
    bot.send_message(message.chat.id,'Для хорошей подготовки недостаточно только тренироваться на случайных варинтах.Предлегаю ссылку для перехода на мой канал,где вы можете ознакомиться с источниками,которые снабдят вас актуальной и полезной информацией')
    bot.send_message(message.chat.id,"https://t.me/hotinfoegogus")
@bot.message_handler(commands=['music'])
def musicplay(msg):
    a = ["1AecnkFXTY27XtZ6VqzGdZ", "0vvXsWCC9xrXsKd4FyS8kM", "5YKm5Zt0AUdKrlrvWzUV6l"]
    b = random.choice(a)
    bot.send_message(chat_id=msg.chat.id, text="https://open.spotify.com/playlist/" + str(b))

@bot.message_handler(commands=['subjects'])
def choose_academic_subject(msg):
    try:
        markup = telebot.types.InlineKeyboardMarkup(row_width=1)
        for i in range(len(all_subjects)):
            subject = all_subjects[i]
            button = telebot.types.InlineKeyboardButton(text=subject.title, callback_data=str(i))
            markup.add(button)
        bot.send_message(chat_id=msg.chat.id, text='Выберите предмет:', reply_markup=markup)
    except Exception as e:
        print('Ошибка:', e.args)
        bot.send_message(chat_id=msg.chat.id, text='Во время обработки запроса произошла ошибка')


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    try:
        subject = all_subjects[int(call.data)]
        link = gen_random_link(subject)
        text = '*Генерация варианта прошла успешно*\n\n' + \
               'Предмет: ' + subject.title + '\n' + \
               'Сссылка: ' + link
        bot.send_message(chat_id=call.message.chat.id, text=text, parse_mode='Markdown')
    except Exception as e:
        print('Ошибка:', e.args)
        bot.send_message(chat_id=call.message.chat.id, text='Во время обработки запроса произошла ошибка')


def gen_random_link(subj: AcademicSubject) -> str:
    themes = parse_themes(subj)

    # Выбираем случайные темы
    select_themes_indexes = random.sample(range(len(themes)), random.randint(*NUMBER_CATEGORIES))

    # Генерируем payload
    payload = {
        'public': 'false',
        'defthemes': 'true',
    }
    for i in range(len(themes)):
        theme = themes[i]
        payload[theme['name']] = random.randint(*NUMBER_TASKS) if i in select_themes_indexes else 0

    # Отправляем запрос
    payload_str = urlencode(payload)
    response = requests.post(subj.main_page_url + '/test?a=generate', headers=headers, data=payload_str, verify=False,
                             allow_redirects=False)
    return subj.main_page_url + response.headers['Location']


if __name__ == '__main__':
    bot.infinity_polling()
