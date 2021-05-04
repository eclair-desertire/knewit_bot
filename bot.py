import os
import config
import telebot
from telebot import types
import json
import urllib.request
import sqlite3
import tg_analytic
Alisher_ID = 1392920598 #(debug)
Artyom_ID= 396364902 #(debug)
Nurbek_ID= 878878226
Ruslan_ID= 293907463
Server_IP='5.188.154.95'
conn = sqlite3.connect('db/knewit_database.db', check_same_thread=False)
cursor = conn.cursor()
# easter_egg=0 # Пасхалка
bot=telebot.TeleBot(config.token)
@bot.message_handler(commands=['start'])
def start_message(message): # функция срабатывает при вводе команды /start
    bot.send_message(message.chat.id,'Здравствуйте, вас приветствует консультант-бот школы программирования KnewIT!\nЧто вы хотите узнать? :)') #приветственный текст
    # bot.send_message(Alisher_ID,message.chat.id) Для получения ID пользователей
    us_id=message.from_user.id
    usname=message.from_user.username
    fname=message.from_user.first_name
    lname=message.from_user.last_name
    db_table_val(User_ID=us_id,username=usname,first_name=fname,last_name=lname)
    add_start_buttons(message)
    


@bot.message_handler(commands=['settings'])
def admin_panel(message):
    if message.chat.id==Alisher_ID or message.chat.id==Artyom_ID:
        bot.send_message(message.chat.id,'Добро пожаловать Сэр, какая отладочная информация вам нужна')
    else:
        bot.send_message(message.chat.id,'Вам недоступна эта опция')

def add_start_buttons(message):
    buttons_start=['О нас','Наши курсы','Цены','Оставить заявку','Контакты','Оставить предложение по модернизации бота']
    custom_keyboard=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in buttons_start:
        custom_keyboard.add(telebot.types.KeyboardButton(i))
    bot.send_message(message.chat.id,'Выберите нужную опцию:',reply_markup=custom_keyboard)

@bot.message_handler(content_types=['text']) # срабатывает в любом случае когда бот получит текст
def answer_handler(message):
    check_answer(message)



def check_answer(message):
    if message.text=='Наши курсы':
        our_courses(message)
    elif message.text=='Цены':
        price(message)
    elif message.text=='Оставить заявку':
        msg=bot.send_message(message.chat.id,'Введите свои данные в таком формате: Иван +7-800-555-35-35 front-end\nИли так: Иван +7-800-555-35-35')
        bot.register_next_step_handler(msg,request_send)
    elif message.text=='О нас':
        about_us(message)
    elif message.text=='Контакты':
        our_managers(message)
    elif message.text=='В главное меню':
        add_start_buttons(message)
    elif message.text=='Front-end' or message.text=='front-end' or message.text=='front end' or message.text=='Front end':
        front_end(message)
    elif message.text=='C++' or message.text=='c++':
        cplusplus(message)
    elif message.text=='C#' or message.text=='c#':
        csharp(message)
    elif message.text=='JavaSE' or message.text=='javase' or message.text=='java' or message.text=='Java' or message.text=='JavaSe':
        javase(message)
    elif message.text=='Python/Django' or message.text=='python' or message.text=='Python' or message.text=='Django' or message.text=='django':
        pydjango(message)
    elif message.text=='Unity' or message.text=='unity' or message.text=='UNITY' or message.text=='UNITY3D' or message.text=='Unity3D':
        unity(message)
    elif message.text=='Наши преподаватели':
        teachers(message)
    elif message.text=='Оставить предложение по модернизации бота':
        msg=bot.send_message(message.chat.id,'Скажите пожалуйста, как мы могли бы улучшить нашего бота?')
        bot.register_next_step_handler(msg,up_bot)
    else:
        bot.send_message(message.chat.id,'Некорректный запрос\n')

def up_bot(message):
    bot.send_message(Alisher_ID,'Предложение по улучшению бота: '+message.text)
    bot.send_message(message.chat.id,'Спасибо за предложение! Мы обязательно его рассмотрим')

def request_send(message):
    send_data=message.text.split()
    if len(send_data)==3:
        bot.send_message(message.chat.id,'Ваша заявка принята. Мы вам обязательно перезвоним!\n')
        bot.send_message(Alisher_ID,'Новая заявка(Бот): \n'+'Имя: '+
        str(send_data[0])+'\n'+'Телефон: '+str(send_data[1])+'\n'+
        'Курс: '+str(send_data[2])+'\n')
        # bot.send_message(Ruslan_ID,'Новая заявка(Бот): \n'+'Имя: '+
        # str(send_data[0])+'\n'+'Телефон: '+str(send_data[1])+'\n'+
        # 'Курс: '+str(send_data[2])+'\n')
        # bot.send_message(Nurbek_ID,'Новая заявка(Бот): \n'+'Имя: '+
        # str(send_data[0])+'\n'+'Телефон: '+str(send_data[1])+'\n'+
        # 'Курс: '+str(send_data[2])+'\n')
    elif len(send_data)==2:
        bot.send_message(message.chat.id,'Ваша заявка принята. Мы вам обязательно перезвоним!\n')
        bot.send_message(Alisher_ID,'Новая заявка(Бот): \n'+'Имя: '+
        str(send_data[0])+'\n'+'Телефон: '+str(send_data[1]))
        # bot.send_message(Ruslan_ID,'Новая заявка(Бот): \n'+'Имя: '+
        # str(send_data[0])+'\n'+'Телефон: '+str(send_data[1]))
        # bot.send_message(Nurbek_ID,'Новая заявка(Бот): \n'+'Имя: '+
        # str(send_data[0])+'\n'+'Телефон: '+str(send_data[1]))
    else:
        bot.send_message(message.chat.id,'Некорректные данные')

def about_us(message):# о компании
    with open('static_files/knewit_logo.jpg','rb') as snd_png:
        bot.send_photo(message.chat.id,snd_png)
    bot.send_message(message.chat.id,'8 лет успешного обучения.\nKnewIT – первая школа программирования в Казахстане.\nKnewIT – это профессиональное обучение с возможностью трудоустройства.\nКурсы программирования подходят для уровней beginer, junior и middle developer.\n')
    keyboard=types.InlineKeyboardMarkup()
    urlbutton=types.InlineKeyboardButton(text='Наш сайт',url='https://knewit.kz/',callback_data='perehod')
    keyboard.add(urlbutton)
    bot.send_message(message.chat.id,'Наш адрес:\nГ. Алматы , ул. Макатаева 117А, БЦ LOTOS, каб. 423',reply_markup=keyboard)

# @bot.callback_query_handler(lambda query: query.data=='perehod')
# def process_callback(query):
#     bot.send_message(Alisher_ID,'PERESHEL NA SAYT')

def teachers(message):
    bot.send_message(message.chat.id,'ТУТ БУДЕТ ИНФА О ПРЕПОДАХ\n')

def our_courses(message):# выводит список курсов
    bot.send_message(message.chat.id,'Мы предлагаем такие курсы как:\n'+
    'Front-end\n'+'Python/Django\n'+'C++\n'+
    'C#\n'+'JavaSE\n')
    bot.send_message(message.chat.id,'Хотите узнать подробнее о каждом курсе? Нажмите на нужную кнопку\n')
    buttons_course=['Front-end','Python/Django','C++', 'C#','Unity','JavaSE','В главное меню']
    custom_keyboard=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in buttons_course:
        custom_keyboard.add(telebot.types.KeyboardButton(i))
    bot.send_message(message.chat.id,'Выберите нужную опцию:',reply_markup=custom_keyboard)
    

def front_end(message):
    with open('static_files/Front_end.png','rb') as s_photo:
        bot.send_photo(message.chat.id,s_photo)
    bot.send_message(message.chat.id,'Продолжительность курса: 3 месяца\n'+'На каждом из этих месяцев вы будете изучать:\n')
    bot.send_message(message.chat.id,'1 месяц: HTML/CSS\n'+
            '2 месяц: Javascript\n'+
                '3 месяц: Jquery, дополнения к javascript\n'+
                '4 месяц: Vue.js\n')
    bot.send_message(message.chat.id,'В одном месяце 13 занятий, занятия проводятся 3 раза в неделю по 2 часа. Расписание обговаривается отдельно с преподавателями\n'+
            'На каждом уроке вам будет даваться домашнее задание для закрепления материала\n'+
            'По окончанию курса, вы овладаете основными навыками алгоритмизации и программирования, что поможет трудоустроиться в дальнейшем\n')


def unity(message):
    with open('static_files/Unity_Logo.png','rb') as s_photo:
        bot.send_photo(message.chat.id,s_photo)
    bot.send_message(message.chat.id,'Продолжительность курса: 3 месяца\n'+'На каждом из этих месяцев вы будете изучать:\n')
    bot.send_message(message.chat.id,'1 месяц: Первое знакомство с редактором Unity, первая игра, угадайка пароля\n'+
        '2 месяц: Углубленное изучение возможностей движка, игра платформер\n'+
        '3 месяц: Продвинутое изучение Unity, игра рейл-ган шутер в космосе\n')
    bot.send_message(message.chat.id,'В одном месяце 13 занятий, занятия проводятся 3 раза в неделю по 2 часа. Расписание обговаривается отдельно с преподавателями\n'+
            'На каждом уроке вам будет даваться домашнее задание для закрепления материала\n'+
            'По окончанию курса, вы овладеете основными навыками для создания крутых игр!\n')

def cplusplus(message):
    with open('static_files/LogoCPP.png','rb') as s_photo:
        bot.send_photo(message.chat.id,s_photo)
    bot.send_message(message.chat.id,'Продолжительность курса: 3 месяца\n'+'На каждом из этих месяцев вы будете изучать:\n')
    bot.send_message(message.chat.id,'1 месяц: Основы синтаксиса, введение в программирование.\n'+
            '2 месяц: углубленное изучение языка, сложные конструкции и функции\n'+
                '3 месяц: ООП, дипломный проект\n')
    bot.send_message(message.chat.id,'В одном месяце 13 занятий, занятия проводятся 3 раза в неделю по 2 часа. Расписание обговаривается отдельно с преподавателями\n'+
            'На каждом уроке вам будет даваться домашнее задание для закрепления материала\n'+
            'По окончанию курса, вы овладаете основными навыками алгоритмизации и программирования, что поможет трудоустроиться в дальнейшем\n')


def csharp(message):
    with open('static_files/csharp.jpg','rb') as s_photo:
        bot.send_photo(message.chat.id,s_photo)
    bot.send_message(message.chat.id,'Продолжительность курса: 3 месяца\n'+'На каждом из этих месяцев вы будете изучать:\n')
    bot.send_message(message.chat.id,'1 месяц: Основы синтаксиса, введение в программирование.\n'+
    '2 месяц: углубленное изучение языка, сложные конструкции и функции, ООП\n'+
        '3 месяц: GUI, дипломный проект\n')
    bot.send_message(message.chat.id,'В одном месяце 13 занятий, занятия проводятся 3 раза в неделю по 2 часа. Расписание обговаривается отдельно с преподавателями\n'+
            'На каждом уроке вам будет даваться домашнее задание для закрепления материала\n'+
            'По окончанию курса, вы овладаете основными навыками алгоритмизации и программирования, что поможет трудоустроиться в дальнейшем\n')


def pydjango(message):
    with open('static_files/pydjango.png','rb') as s_photo:
        bot.send_photo(message.chat.id,s_photo)
    bot.send_message(message.chat.id,'Продолжительность курса: 5 месяцев\n'+'На каждом из этих месяцев вы будете изучать:\n')
    bot.send_message(message.chat.id,'1 месяц: Основы синтаксиса, введение в программирование.\n'+
        '2 месяц: углубленное изучение языка, сложные конструкции и функции, ООП\n'+'3 месяц: GUI, TelegramBot\n'+
        '4 месяц: HTML/CSS/SQL (MySQL/PosgreSQL)\n'+
        '5 месяц: Создание сайтов на Django, дипломный проект\n')
    bot.send_message(message.chat.id,'В одном месяце 13 занятий, занятия проводятся 3 раза в неделю по 2 часа. Расписание обговаривается отдельно с преподавателями\n'+
            'На каждом уроке вам будет даваться домашнее задание для закрепления материала\n'+
            'По окончанию курса, вы овладаете основными навыками алгоритмизации и программирования, создания программ, сайтов и ботов, что поможет трудоустроиться в дальнейшем\n')


def javase(message):
    with open('static_files/javase.png','rb') as s_photo:
        bot.send_photo(message.chat.id,s_photo)
    bot.send_message(message.chat.id,'Продолжительность курса: 3 месяца\n'+'На каждом из этих месяцев вы будете изучать:\n')
    bot.send_message(message.chat.id,'1 месяц: Основы синтаксиса, введение в программирование.\n'+
            '2 месяц: углубленное изучение языка, сложные конструкции и функции, ООП\n'+
                '3 месяц: Клиент-серверные приложения, GUI\n')
    bot.send_message(message.chat.id,'В одном месяце 13 занятий, занятия проводятся 3 раза в неделю по 2 часа. Расписание обговаривается отдельно с преподавателями\n'+
            'На каждом уроке вам будет даваться домашнее задание для закрепления материала\n'+
            'По окончанию курса, вы овладаете основными навыками алгоритмизации и программирования, что поможет трудоустроиться в дальнейшем\n')

def our_managers(message): # выводит контакты менеджеров
    bot.send_message(message.chat.id,'Наши менеджеры:'+'\n'+'Нурбек: +7-701-938-04-63\n')

def price(message): # выводит цены на курсы
    bot.send_message(message.chat.id,'Цены на наши курсы (оплата помесячная):\nOnline обучение, групповое: 39 000 тенге/мес\nОчное обучение, групповое: 55 000 тенге/мес.\nИндивидуальные занятия: 150 000 тенге/мес.\n')

def db_table_val(User_ID: int, username: str,first_name:str,last_name:str):
	cursor.execute('INSERT INTO USERS (User_ID, username,first_name,last_name) VALUES (?, ?, ?, ?)', (User_ID, username,first_name,last_name))
	conn.commit()

if __name__ == '__main__': 
     bot.infinity_polling()