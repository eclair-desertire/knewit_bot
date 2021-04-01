import os
import config
import telebot
# from keyboa import keyboa_maker
Alisher_ID = 1392920598 #(debug)
# easter_egg=0 # Пасхалка
# Manager_ID=0
bot=telebot.TeleBot(config.token)
# variants=['Наши курсы','Цены, на наши курсы','О нас','Контакты'] Другой вариант кнопок который встраивается в сообщения
# kb_vars=keyboa_maker(items=variants,copy_text_to_callback=True)
# bot.send_message(message.chat.id,reply_markup=kb_vars,text='Выберите нужную опцию:') Прописать в функцию
@bot.message_handler(commands=['start'])
def start_message(message): # функция срабатывает при вводе команды /start
    bot.send_message(message.chat.id,'Здравствуйте, вас приветствует консультант-бот школы программирования KnewIT!\nЧто вы хотите узнать? :)') #приветственный текст
    keyboard=telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Наши курсы','Цены','Оставить заявку', 'О нас','Наши преподаватели','Контакты')
    bot.send_message(message.chat.id,'Выберите нужную опцию:',reply_markup=keyboard)
    

@bot.message_handler(commands=['request'])
def request_send(message): # функция которая отвечает за заявки
    lst=message.text.split()
    if len(lst)==2:
        request=lst[1].split(',')
        bot.send_message(message.chat.id,'Мы вам обязательно перезвоним!\n')
        bot.send_message(Alisher_ID,'Новая заявка(Бот): \n'+'Имя: '+
        str(request[0])+'\n'+'Телефон: '+str(request[1])+'\n'+
        'Курс: '+str(request[2])+'\n')
    elif len(lst)==4:
        request=lst[1]+lst[2]+lst[3]
        request=request.split(',')
        bot.send_message(message.chat.id,'Мы вам обязательно перезвоним!\n')
        bot.send_message(Alisher_ID,'Новая заявка(Бот): \n'+'Имя: '+
        str(request[0])+'\n'+'Телефон: '+str(request[1])+'\n'+
        'Курс: '+str(request[2])+'\n')
    else:
        bot.send_message(message.chat.id,'Некорректные данные, пожалуйста введите свои данные еще раз')
    

@bot.message_handler(content_types=['text']) # срабатывает в любом случае когда бот получит текст
def answer_handler(message):
    check_answer(message)


def check_answer(message):# обработчик ответов
    if message.text=='Наши курсы':
        our_courses(message)
    elif message.text=='Цены':
        price(message)
    elif message.text=='Оставить заявку':
        bot.send_message(message.chat.id,'Введите свои данные в таком формате:\n/request Иван, +7-800-555-35-35, front-end\n')
    elif message.text=='О нас':
        about_us(message)
    elif message.text=='Контакты':
        our_managers(message)
    elif message.text=='В главное меню':
        keyboard=telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Наши курсы','Цены','Оставить заявку','О нас', 'Наши преподаватели','Контакты')
        bot.send_message(message.chat.id,'Выберите нужную опцию:',reply_markup=keyboard)
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
    elif message.text=='Наши преподаватели':
        teachers(message)
    else:
        bot.send_message(message.chat.id,'Некорректный запрос\n')

def about_us(message):# о компании
    bot.send_message(message.chat.id,'7 лет успешного обучения.\nKnewIT – первая школа программирования в Казахстане.\nKnewIT – это профессиональное обучение с возможностью трудоустройства.\nКурсы программирования подходят для уровней beginer, junior и middle developer.\n')
    bot.send_message(message.chat.id,'Наш адрес:\nГ. Алматы , ул. Макатаева 117А, БЦ LOTOS, каб. 423')
def teachers(message):
    bot.send_message(message.chat.id,'ТУТ БУДЕТ ИНФА О ПРЕПОДАХ\n')

def our_courses(message):# выводит список курсов
    bot.send_message(message.chat.id,'Мы предлагаем такие курсы как:\n'+
    'Front-end\n'+'Python/Django\n'+'C++\n'+
    'C#\n'+'JavaSE\n')
    bot.send_message(message.chat.id,'Хотите узнать подробнее о каждом курсе? Нажмите на нужную кнопку\n')
    keyboard=telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Front-end','Python/Django','C++', 'C#', 'JavaSE','В главное меню')
    bot.send_message(message.chat.id,'Выберите нужную опцию:',reply_markup=keyboard)

def front_end(message):
    bot.send_message(message.chat.id,'Тут будет полная инфа, PLACEHOLDER')

def cplusplus(message):
    with open('static_files/LogoCPP.png','rb') as s_photo:
        bot.send_photo(message.chat.id,s_photo)
    bot.send_message(message.chat.id,'Продолжительность курса: 3 месяца\n'+'На каждом из этих месяцев вы будете изучать следующие темы:\n')
    bot.send_message(message.chat.id,'''Месяц 1:
1.	Установка среды разработки
2.	Введение в язык и основы синтаксиса
3.	 Типы данных и переменные
4.	Операции ввода и вывода
5.	Арифметические операторы
6.	Операторы присваивания
7.	Логические операторы(BOOL подробно), по желанию можно дать битовые операции(необязательно)
8.	 Математические операции (#include <cmath>)
9.	 Условия(IF, SWITCH), условные операторы
10.	Циклы(while, do..while, for, break, continue etc.)
11.	STRING подробно
12.	Массивы(Одномерные, двумерные)
13.	Указатели и ссылки, динамическая память, динамические массивы(vector)
14.	Методы сортировки(простые)
15.	Сортировка сложнее buble
\n''')
    bot.send_message(message.chat.id,'''Месяц 2:
1.	Функции
2.	Параметры функций
3.	Перегрузка Функций
4.	Рекурсия
5.	Структуры
6.	Вложенные структуры
7.	Шаблоны
\n''')
    bot.send_message(message.chat.id,'''Месяц 3:
1.	Введение в ООП
2.	Классы, обьекты
3.	Методы
4.	Конструкторы
5.	Деструкторы
6.	Модификаторы доступа
7.	Инкапсуляция
8.	Наследование
9.	Полиморфизм
10.	Работа с файлами
11.	Исключения
12.	Знакомство с STL
\n''')
    bot.send_message(message.chat.id,'В одном месяце 13 занятий, занятия проводятся 3 раза в неделю по 2 часа. Расписание обговаривается отдельно с преподавателями\n')
    bot.send_message(message.chat.id,'На каждом уроке вам будет даваться домашнее задание для закрепления материала\n')
    bot.send_message(message.chat.id,'По окончанию курса, вы овладаете основными навыками алгоритмизации и программирования, что поможет трудоустроиться в дальнейшем\n')
    bot.send_message(message.chat.id,'Если вы желаете ознакомиться с курсом подробнее, ниже будет прикреплен учебный план этого курса:\n')
    with open('static_files/C++.docx','rb') as send_fl:
        bot.send_document(message.chat.id,send_fl)


def csharp(message):
    bot.send_message(message.chat.id,'Тут будет полная инфа, PLACEHOLDER')

def pydjango(message):
    bot.send_message(message.chat.id,'Тут будет полная инфа, PLACEHOLDER')

def javase(message):
    bot.send_message(message.chat.id,'Тут будет полная инфа, PLACEHOLDER')

def our_managers(message): # выводит контакты менеджеров
    bot.send_message(message.chat.id,'Наши менеджеры:'+'\n'+'Олегшер: 8-800-555-35-35\n')

def price(message): # выводит цены на курсы
    bot.send_message(message.chat.id,'Цены на наши курсы (оплата помесячная):\nOnline обучение, групповое: 39 000 тенге/мес\nОчное обучение, групповое: 55 000 тенге/мес.\nИндивидуальные занятия: 150 000 тенге/мес.\n')
if __name__ == '__main__':
     bot.infinity_polling()