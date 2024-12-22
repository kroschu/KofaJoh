from telebot import types

def markup_start():

    markup_start = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    btn0 = types.KeyboardButton('👋')
    markup_start.row(btn0)

    return markup_start

def markup_main():

    markup_main = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    btn1 = types.KeyboardButton('🤖')
    btn2 = types.KeyboardButton('💻 Тех. поддержка')
    btn3 = types.KeyboardButton('📚 Информация')
    btn4 = types.KeyboardButton('❌CLOSE❌')
    markup_main.row(btn1, btn2)
    markup_main.row(btn3, btn4)

    return markup_main

def markup_it():

    markup_it = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    btn1_it = types.KeyboardButton('⚠️ Проверить статус заявки')
    btn2_it = types.KeyboardButton('🖥 Оставить заявку')
    btn3_it = types.KeyboardButton('👈 назад')
    markup_it.row(btn1_it, btn2_it)
    markup_it.row(btn3_it)

    return markup_it

def markup_admin():

    markup_adm = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    btn1_adm= types.KeyboardButton('Списки задач📄')
    btn2_adm= types.KeyboardButton('🖊 Изменить статус')
    btn3_adm = types.KeyboardButton('⛔️Удалить задачу⛔️')
    btn4_adm = types.KeyboardButton('👈 назад')
    markup_adm.row(btn1_adm, btn2_adm)
    markup_adm.row(btn3_adm, btn4_adm)

    return markup_adm

def markup_task_l():

    markup_adm = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    btn1_adm= types.KeyboardButton('Все задачи 📄')
    btn2_adm= types.KeyboardButton('❗️ Активные')
    btn3_adm = types.KeyboardButton('✅ Выполненные')
    btn4_adm = types.KeyboardButton('👈 admin menu')
    markup_adm.row(btn1_adm, btn2_adm)
    markup_adm.row(btn3_adm, btn4_adm)

    return markup_adm

def markup_secure():

    markup_sec = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    btn1_sec= types.KeyboardButton('Постановка на охрану 👮‍♀️')
    btn2_sec= types.KeyboardButton('Запрос на снятие с охраны ⚡️')
    btn3_sec = types.KeyboardButton('👈 назад')
    btn4_sec  = types.KeyboardButton('❌CLOSE❌')
    markup_sec.row(btn1_sec, btn2_sec)
    markup_sec.row(btn3_sec, btn4_sec)

    return markup_sec

def markup_up():

    markup_up = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    btn1_up= types.KeyboardButton('🆙 Офис 1 ⚙️')
    btn2_up= types.KeyboardButton('🆙 Офис 2 👑')
    btn3_up = types.KeyboardButton('👈 назад')
    btn4_up  = types.KeyboardButton('❌CLOSE❌')
    markup_up.row(btn1_up, btn2_up)
    markup_up.row(btn3_up, btn4_up)

    return markup_up

def markup_down():

    markup_down = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    btn1_down= types.KeyboardButton('🔻 Офис 1 ⚙️')
    btn2_down= types.KeyboardButton('🔻 Офис 2 👑')
    btn3_down = types.KeyboardButton('👈 назад')
    btn4_down  = types.KeyboardButton('❌CLOSE❌')
    markup_down.row(btn1_down, btn2_down)
    markup_down.row(btn3_down, btn4_down)

    return markup_down
