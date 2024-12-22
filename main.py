import os
import telebot
from dotenv import load_dotenv
from telebot import *
import button
import requests
import sqlite3
#import re

load_dotenv()
secure_chat_id = os.getenv('SECURE')
token = os.getenv('TOKEN')
office = os.getenv('OFFICE')
it_adm = os.getenv('IT_ADM')
bot = telebot.TeleBot(token)
api_mts_key = os.getenv('API_MTS_KEY')
number_mts = os.getenv('NUMBER')
number_1 = os.getenv('NUMBER_1')
number_2 = os.getenv('NUMBER_2')

menu = ['💻 Тех. поддержка',['admin'],'📚 Информация',['start'],'🤖','🆙 Офис 2 👑','🆙 Офис 1 ⚙️','🔻 Офис 2 👑','🔻 Офис 1 ⚙️','⚠️ Проверить статус заявки','❌CLOSE❌','🖥 Оставить заявку','👈 назад','Постановка на охрану 👮‍♀️','Запрос на снятие с охраны ⚡️']

@bot.message_handler(commands=['admin']) # admin панель
def admin(message):
    if message.chat.title == 'Telegram Group Name IT':
        bot.send_message(chat_id=it_adm, text=f'Добрый день!\nВы в меню администратора.\nЧто Вам необходимо?\n', reply_markup=button.markup_admin())
    else:
        bot.send_message(message.chat.id,'Вы не являетесь администртором', reply_markup=button.markup_start())

@bot.message_handler(commands=['start']) # кнопка Start
def start(message):
    bot.send_message(message.chat.id, f"👋 Привет,{message.from_user.first_name}!  Я бот Digniori Arts", reply_markup=button.markup_start())
    bot.send_message(message.chat.id, '❓ Выберете интересующий Вас раздел', reply_markup=button.markup_main())

@bot.message_handler(commands=['close']) # кнопка close
def close(message):
    bot.send_message(message.chat.id, 'Goodbye', reply_markup=None)


@bot.message_handler(func=lambda message: True, content_types=['audio', 'photo', 'voice', 'video', 'document', 'text', 'location', 'contact', 'sticker'])
def get_text_messages(message):
    
    
     ##########################     START      ##############################
    
    if message.text == '👋':
        bot.send_message(message.chat.id, ' Вы вернулись в главное меню.\n❓ Выберете интересующий Вас раздел', parse_mode='HTML', reply_markup=button.markup_main())
    
    elif message.text == '👈 назад':    
        bot.send_message(message.chat.id, '👋', reply_markup=button.markup_main())  
    
     ##########################      MAIN      ##############################
    
    elif message.text == '🤖':
        if message.chat.title == 'Telegram Group Name IT Secure':
            bot.send_message(chat_id=secure_chat_id, text=f'Добрый день!\nВы в меню охраны.\nЧто необходимо сделать?\n', reply_markup=button.markup_secure())
        else:
            bot.send_message(message.chat.id,'Вы не можете использовать данную фунуцию...\nОбратитесь к администратору.', reply_markup=button.markup_start())

    elif message.text == '❌CLOSE❌':
        bot.send_message(message.chat.id, 'Goodbye', reply_markup=button.markup_start())

    elif message.text == '💻 Тех. поддержка':
        bot.send_message(message.chat.id, 'Выберите подменю', reply_markup=button.markup_it())
        

    elif message.text == '📚 Информация':
        bot.send_message(message.chat.id, 'Подробно про компаниию по ' + '[ссылке](https://ya.ru/)', parse_mode='Markdown')
        bot.send_message(message.chat.id, 'Облачное хранилище по ' + '[ссылке](https://cloud.ya.ru/)', parse_mode='Markdown')

     ##########################      SECURE     ##############################
    elif message.text == 'Постановка на охрану 👮‍♀️':
        bot.send_message(chat_id=secure_chat_id, text=f'Какой объект, необходимо поставить на охрану???', reply_markup=button.markup_up())
               
    elif message.text == 'Запрос на снятие с охраны ⚡️':
        bot.send_message(chat_id=secure_chat_id, text=f'Какой объект, необходимо снять с охраны???', reply_markup=button.markup_down())


    elif message.text == '🆙 Офис 1 ⚙️':
        try:
            headers = {
                'Authorization': f'{api_mts_key}',
                'Content-Type': 'application/json',
            }
            data = {"number": f"{number_mts}", "destination": f"{number_1}", "text" : "O1"}
            requests.post('https://api.exolve.ru/messaging/v1/SendSMS', headers=headers, json=data)

            bot.send_message(chat_id=secure_chat_id, text=f'Спасибо за информацию, охранная система включена.\nУ Вас есть 15 сек покинуть помещение.', reply_markup=button.markup_start())
            bot.send_message(chat_id=secure_chat_id, text=f'👮‍♀️', reply_markup=button.markup_main())
            bot.send_message(chat_id=office, text=f'Cотрудник {message.from_user.first_name}, ушел. \nВключена сигнализация в Офисе 1 ⚙️.\nNikname:@{message.from_user.username}', parse_mode='Markdown')
        
        except Exception as e:  
            bot.send_message(message.chat.id, 'Произошла ошибка... Попробуйте снова.', reply_markup=button.markup_start())


    elif message.text == '🔻 Офис 1 ⚙️':
        #try:
        headers = {
            'Authorization': f'{api_mts_key}',
            'Content-Type': 'application/json',
        }

        data = {"number": f"{number_mts}", "destination": f"{number_1}", "text" : "O0"}
        requests.post('https://api.exolve.ru/messaging/v1/SendSMS', headers=headers, json=data)

        bot.send_message(chat_id=secure_chat_id, text=f'Спасибо за информацию, охранная система будет выключена.\nВремя ожидания 20 сек.', reply_markup=button.markup_main())
        bot.send_message(chat_id=secure_chat_id, text=f'👌 Сигнализация отключена', reply_markup=button.markup_main())
        bot.send_message(chat_id=office, text=f'Cотрудник {message.from_user.first_name}, отключил сигнализацию в Офисе 1 ⚙️.\nNikname:@{message.from_user.username}', parse_mode='Markdown')
    
        # except Exception as e:  
        #     bot.send_message(message.chat.id, 'Произошла ошибка... Попробуйте снова.', reply_markup=button.markup_start())


    elif message.text == '🆙 Офис 2 👑':
        try:
            headers = {
                'Authorization': f'{api_mts_key}',
                'Content-Type': 'application/json',
            }
            data = {"number": f"{number_mts}", "destination": f"{number_2}", "text" : "O1"}
            requests.post('https://api.exolve.ru/messaging/v1/SendSMS', headers=headers, json=data)          
                        
            bot.send_message(chat_id=office, text=f'''Cотрудник {message.from_user.first_name}, ушел. \nНаправлен запрос на включение сигнализации в Офисе 2 👑.\nNikname:@{message.from_user.username}''', parse_mode='Markdown')
            bot.send_message(chat_id=secure_chat_id, text=f'Спасибо за информацию, охранная система включена.\nУ Вас есть 15 сек покинуть помещение.')
            bot.send_message(chat_id=secure_chat_id, text=f'👮‍♀️', reply_markup=button.markup_main())
        
        except Exception as e:  
            bot.send_message(message.chat.id, 'Произошла ошибка... Попробуйте снова.', reply_markup=button.markup_start())

         
    elif message.text == '🔻 Офис 2 👑':
        try:    
            headers = {
                    'Authorization': f'{api_mts_key}',
                    'Content-Type': 'application/json',
                }
            data = {"number": f"{number_mts}", "destination": f"{number_2}", "text" : "O0"}
            requests.post('https://api.exolve.ru/messaging/v1/SendSMS', headers=headers, json=data)
            
            bot.send_message(chat_id=secure_chat_id, text=f'Спасибо за информацию, охранная система будет выключена.\nВремя ожидания 20 сек.')
            bot.send_message(chat_id=secure_chat_id, text=f'👌 Сигнализация отключена', reply_markup=button.markup_main())
            bot.send_message(chat_id=office, text=f'Cотрудник {message.from_user.first_name}, отключил сигнализацию в Офисе 2 👑.\nNikname:@{message.from_user.username}', parse_mode='Markdown')
        
        except Exception as e:  
            bot.send_message(message.chat.id, 'Произошла ошибка... Попробуйте снова.', reply_markup=button.markup_start())


    ##########################    USER_TASKS    ##############################

    elif message.text == '⚠️ Проверить статус заявки':
        bot.send_message(message.chat.id, 'Введите номер Вашего обращения:', reply_markup=button.markup_it())
        bot.register_next_step_handler(message, stat_user_tasks)

    
    elif message.text == '🖥 Оставить заявку':    
        bot.send_message(message.chat.id, f'{message.from_user.first_name}, Введите название объекта и опишите проблему:')
        bot.register_next_step_handler(message, add_task)


     ##########################    ADMIN_!!!    ##############################

    elif message.text == 'Списки задач📄':
        bot.send_message(chat_id=it_adm, text=f'Какой список Вас интересует?', reply_markup=button.markup_task_l())
        
    elif message.text == '🖊 Изменить статус':
        bot.send_message(chat_id=it_adm, text=f'Введите номер задачи для изменения статуса', reply_markup=button.markup_admin())
        bot.register_next_step_handler(message, stat_task)

    elif message.text == '⛔️Удалить задачу⛔️':
        bot.send_message(chat_id=it_adm, text=f'ВНИМАНИЕ\nУдаленные из базы задачи не восстановить!\nЕсли вы уверены, введите номер задачи.', reply_markup=button.markup_admin())
        bot.register_next_step_handler(message, del_task)

     ##########################    ADMIN_TASKS    ##############################       
        
    elif message.text == 'Все задачи 📄':
        
# Просмотр всех задач статуса задачи
        
        try:
            connection = sqlite3.connect('./requests.db')
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM request')
            tasks = cursor.fetchall()
            su = str('')
            for task in tasks:
                s1 = f' \t\t Обращение № {task[0]} \nОт: @{task[1]}. \nпроблема:\n{task[2]}\nСтатус: {task[3]}\n\n'
                su = su + s1
                s1 = ''
            connection.close()
            bot.send_message(chat_id=it_adm, text=f'{su}', parse_mode='HTML')
            bot.send_message(chat_id=it_adm, text=f'Готово!', reply_markup=button.markup_task_l())
        
        except Exception as e:
            bot.send_message(chat_id=it_adm, text=f'Список пуст.', reply_markup=button.markup_task_l())

      
    elif message.text == '❗️ Активные':
        
# Просмотр активных задач статуса задачи

        try:
            connection = sqlite3.connect('./requests.db')
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM request')
            tasks = cursor.fetchall()
            ac = str('')
            for task in tasks:
                if task[3] == 'В работе':
                    a1 = f' \t\t Обращение № {task[0]} \nОт: @{task[1]}. \nпроблема:\n{task[2]}\nСтатус: {task[3]}\n\n'
                    ac = ac + a1
                    a1 = ''                
                else:
                    continue

            connection.close()
            bot.send_message(chat_id=it_adm, text=f'{ac}', parse_mode='HTML')
            bot.send_message(chat_id=it_adm, text=f'Готово!', reply_markup=button.markup_task_l())
        except Exception as e:  
            bot.send_message(chat_id=it_adm, text=f'Список пуст. Вы отлично порабоотали!', reply_markup=button.markup_task_l())

    
    elif message.text == '✅ Выполненные':
        connection = sqlite3.connect('./requests.db')
        cursor = connection.cursor()
        try:
            connection = sqlite3.connect('./requests.db')
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM request')
            tasks = cursor.fetchall()
            da = str('')
            for task in tasks:
                if task[3] != 'В работе':
                    d1 = f' \t\t Обращение № {task[0]} \nОт: @{task[1]}. \nпроблема:\n{task[2]}\nСтатус: {task[3]}\n\n'
                    da = da + d1
                    d1 = ''         
                else:
                    continue
            connection.close()
            bot.send_message(chat_id=it_adm, text=f'{da}', parse_mode='HTML')
            bot.send_message(chat_id=it_adm, text=f'Готово!', reply_markup=button.markup_task_l())

        except Exception as e:  
            bot.send_message(chat_id=it_adm, text=f'Список пуст.', reply_markup=button.markup_task_l())


    elif message.text == '👈 admin menu':
        bot.send_message(chat_id=it_adm, text='Вы вернулись в меню Администратора...', reply_markup=button.markup_admin())


# Функция удаления задачи

def del_task(message):
 
    try:
        if message.text in menu:

            get_text_messages(message)     
            
        else:
            connection = sqlite3.connect('./requests.db')
            cursor = connection.cursor()

            try:
                del_id = int(message.text)
                cursor.execute('SELECT * FROM request')
                tasks = cursor.fetchall()
                try:
                    for task in tasks:
                    
                        if task[0] == del_id:
                            cursor.execute('DELETE FROM request WHERE id = ?', (del_id,))
                            connection.commit()
                            bot.send_message(chat_id=it_adm, text=f' \t Обращение № {task[0]} \nОт: {task[1]}. \nпроблема:\n{task[2]}\n Статус: {task[3]}\nУДАЛЕНО!✔️\n', reply_markup=button.markup_admin())
                            raise StopIteration
                        
                        else:
                            continue
                        
                    else:
                        bot.send_message(chat_id=it_adm, text='!Не правильно введен номер!\nНажмите "⛔️Удалить задачу⛔️" и введите номер.' , reply_markup=button.markup_admin())  

                except StopIteration:
                    pass    
            
            except (SyntaxError, ValueError):
                bot.send_message(chat_id=it_adm, text='Вы не ввели номер...\nНажмите "⛔️Удалить задачу⛔️" и введите номер.', reply_markup=button.markup_admin())  

            connection.close()

    except Exception as e:  
        bot.send_message(chat_id=it_adm, text='Произошла ошибка... Попробуйте снова.\nНажмите "⛔️Удалить задачу⛔️" и введите номер.', reply_markup=button.markup_admin())


# Функция изменения статуса задачи
        
def stat_task(message):
    try:
            if message.text in menu:

                get_text_messages(message)     
                
            else:
                connection = sqlite3.connect('./requests.db')
                cursor = connection.cursor()

                try:
                    stat_task_adm = int(message.text)
                    cursor.execute('SELECT * FROM request')
                    tasks = cursor.fetchall()
                    try:
                        for task in tasks:
                        
                            if task[0] == stat_task_adm:
                                cursor.execute('UPDATE request SET status = ? WHERE id = ?', ('Выполнено!', stat_task_adm))
                                connection.commit()
                                bot.send_message(chat_id=it_adm, text=f' \t Обращение № {task[0]} \nОт: {task[1]}. \nпроблема:\n{task[2]}\n Статус: {task[3]}\n\n 🔝Статус ОБНОВЛЕН!🔝', reply_markup=button.markup_admin())
                                raise StopIteration
                            
                            else:
                                continue
                            
                        else:
                            bot.send_message(chat_id=it_adm, text=f'!Не правильно введен номер!\nНажмите "🖊 Изменить статус" и введите номер.' , reply_markup=button.markup_admin())  

                    except StopIteration:
                        pass    
                
                except (SyntaxError, ValueError):
                    bot.send_message(chat_id=it_adm, text=f'Вы не ввели номер...\nНажмите "🖊 Изменить статус" и введите номер.', reply_markup=button.markup_admin())  

                connection.close()

    except Exception as e:  
        bot.send_message(chat_id=it_adm, text=f'Произошла ошибка... Попробуйте снова.\nНажмите "🖊 Изменить статус" и введите номер.', reply_markup=button.markup_admin())


# Функция вывода статуса задачи пользователю
        
def stat_user_tasks(message):
  
    try:
        if message.text in menu:

            get_text_messages(message)     
            
        else:
            connection = sqlite3.connect('./requests.db')
            cursor = connection.cursor()

            try:
                nomber = int(message.text)
                cursor.execute('SELECT * FROM request')
                tasks = cursor.fetchall()
                try:
                    for task in tasks:
                    
                        if task[0] == nomber:
                            bot.send_message(message.chat.id, f' \t Обращение № {task[0]} \nОт: {task[1]}. \nпроблема:\n{task[2]}\n Статус: {task[3]}\n\n', reply_markup=button.markup_it())
                            raise StopIteration
                        
                        else:
                            continue
                        
                    else:
                        bot.send_message(message.chat.id,'!Не правильно введен номер!\nНажмите "⚠️ Проверить статус заявки" и введите номер.' , reply_markup=button.markup_it())  

                except StopIteration:
                    pass    
            
            except (SyntaxError, ValueError):
                bot.send_message(message.chat.id,'Вы не ввели номер...\nНажмите "⚠️ Проверить статус заявки" и введите номер.', reply_markup=button.markup_it())  

            connection.close()

    except Exception as e:  
        bot.send_message(message.chat.id, 'Произошла ошибка... Попробуйте снова.\nНажмите "⚠️ Проверить статус заявки" и введите номер.', reply_markup=button.markup_it())

  
#Функция внесения задачи пользователем

def add_task(message): 
        
    try:
        if message.text in menu:

            get_text_messages(message)     
            
        else:
                       
            connection = sqlite3.connect('./requests.db')
            cursor = connection.cursor()

                # Создаем таблицу request
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS request (
            id INTEGER PRIMARY KEY,
            username TEXT,
            example TEXT,
            status TEXT DEFAULT 'В работе'
            )
            ''')


            cursor.execute('INSERT INTO request (username, example, status) VALUES (?, ?, ?)', (message.from_user.username, message.text, 'В работе'))
            connection.commit()

            last_id = cursor.lastrowid
            connection.close()

            bot.send_message(message.chat.id, f'Номер Вашего обращения: {last_id} \nСпасибо!\n\nПо номеру обращения Вы можете проверить статус.', reply_markup=button.markup_it())
            bot.send_message(chat_id=it_adm, text=f'{message.from_user.first_name} оставил заявку: \n{message.text}\nNikname: @{message.from_user.username}', reply_markup=None)

    except Exception as e:  
        bot.send_message(message.chat.id, 'Произошла ошибка... Попробуйте снова.\n\nНажмите кнопку "🖥 Оставить заявку" и введите сообщение.', reply_markup=button.markup_it())

if __name__ == "__main__":
    # bot.polling(none_stop=True, interval=0)
    while True:
        try:
            bot.polling(none_stop=True)

        except Exception as e:
            logger.error(e)  # или просто print(e) если у вас логгера нет,
            # или import traceback; traceback.print_exc() для печати полной инфы
            time.sleep(15)