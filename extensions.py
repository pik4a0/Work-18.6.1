import telebot
import json
import requests
TOKEN = '6330248346:AAGl12VmK4fSWqokXxKEi2ZBw1QCPJ5Usj4'
bot = telebot.TeleBot(TOKEN)


keys = {
    'биткоин': 'BTC',
    'эфириум': 'ETH',
    'Доллар': 'USD',
}
@bot.message_handler(commands=['start','help'])
def echo_test(message: telebot.types.Message):
    text= 'Для начала работы введите команду формата: \n<имя валюты> \ <в какую валюту перевести> \ <количество переводимой валюты>'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Разрешенные валюты:'
    for key in keys.keys():
        text = '\n'.join((text,key, ))
        bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    quote, base, amount = message.text.split(' ')
    r = requests.get(f'https://min-aip.cryptocompare.com/data/price?fsum={keys[quote]}&tsyms={keys[base]}')
    total_base = json.loads(r.content)[keys[base]]
    text = f'Цена {amount}{quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)

bot.polling()

