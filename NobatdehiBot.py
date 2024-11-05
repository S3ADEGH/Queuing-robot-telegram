import telebot
bot = telebot.TeleBot('7933583271:AAHrEBPTzYMP1f2cuXVjWUZmci-zUzaa2bg')
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! خوش آمدید به ربات من.")

bot.polling()