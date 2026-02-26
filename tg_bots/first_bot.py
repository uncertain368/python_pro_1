import random, telebot, time, schedule, threading, os

bot = telebot.TeleBot("TOKEN")

def gen_pass():
    elements = "+-/*!&$#?=@<>123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    password = ""
    for i in range(15):
        password += random.choice(elements)
    return password

def hello():
    return (
        "Доступные команды:\n"
        "/start — меню\n"
        "/pass — сгенерировать пароль\n"
        "/hello — приветствие\n"
        "/bye - прощание\n"
        '/prediction - шар судьбы\n'
        '/coin - подбросить монетку\n'
        '/set <секунды> - бесконечный таймер с интервалами\n'
        '/unset - остановка таймера\n'
        '/mem - рандомный мем\n'
        '/mem_birds - рандомный мем с птичкой\n'
    )

def q():
    results = ('Хотите узнать ответ на свой вопрос?..\n')
    results += ('Кручу шар судьбы..\n')
    results += (random.choice(['Да', 'Нет', 'Возможно', 'Маловероятно', 'Как мама скажет', 'Как карта ляжет', 'Не думаю', 'Сомнительно', 'Теоретически возможно', 'Такой себе выбор', '50 на 50', 'Спорно', 'У меня нет слов', 'Не факт', 'Ни рыба, ни мясо']))
    return results

def q2():
    results = ('Хотите подбросить монетку?\n')
    results += ('Бросаю..\n')
    results += (random.choice(['Орёл', 'Решка']))
    return results

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!\n" + hello())
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
    
@bot.message_handler(commands = ['pass'])
def send_password(message):
    bot.reply_to(message, gen_pass())

@bot.message_handler(commands = ['prediction'])
def send_q(message):
    bot.reply_to(message, q())
    
@bot.message_handler(commands = ['coin'])
def send_q2(message):
    bot.reply_to(message, q2())

path = r'C:\Users\pc\OneDrive\Desktop\python_a_k\bot\images' 
img = os.listdir(path)

@bot.message_handler(commands=['mem'])
def mem(message):
    filename = random.choice(img)
    full_path = os.path.join(path, filename)
    with open(full_path, 'rb') as f:   
        bot.send_photo(message.chat.id, f)


path_b = r'C:\Users\pc\OneDrive\Desktop\python_a_k\bot\images_birds' 
img_b = os.listdir(path_b)

@bot.message_handler(commands=['mem_birds'])
def mem(message):
    filename_b = random.choice(img_b)
    full_path_b = os.path.join(path_b, filename_b)
    with open(full_path_b, 'rb') as f:   
        bot.send_photo(message.chat.id, f)



def beep(chat_id) -> None:
    """Send the beep message."""
    bot.send_message(chat_id, text='Beep!')


@bot.message_handler(commands=['set'])
def set_timer(message):
    args = message.text.split()
    if len(args) > 1 and args[1].isdigit():
        sec = int(args[1])
        schedule.every(sec).seconds.do(beep, message.chat.id).tag(message.chat.id)
    else:
        bot.reply_to(message, 'Usage: /set <seconds>')


@bot.message_handler(commands=['unset'])
def unset_timer(message):
    schedule.clear(message.chat.id)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
if __name__ == '__main__':
    threading.Thread(target=bot.infinity_polling, name='bot_infinity_polling', daemon=True).start()
    while True:
        schedule.run_pending()
        time.sleep(1)
