import telebot
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv() 

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard=types.ReplyKeyboardMarkup()
    btn1=types.KeyboardButton('About me')
    btn2=types.KeyboardButton('Contact')
    btn3=types.KeyboardButton('Services')
    btn4=types.KeyboardButton('Portfolio')
    keyboard.add(btn1, btn2,)
    keyboard.add(btn3, btn4)
    text = """
✨ Salom 👋🏻

🤖 Botimizga xush kelibsiz!

⚡ Siz uchun tezkor va qulay xizmat tayyor 🚀

📝 Kerakli buyruq yoki matnni yuboring.

💎 Smart • Fast • Easy

🔥🌐⚡
"""
    bot.send_message(message.chat.id,"""
✨ Salom 👋🏻

🤖 Botimizga xush kelibsiz!

⚡ Siz uchun tezkor va qulay xizmat tayyor 🚀

📝 Kerakli buyruq yoki matnni yuboring.

💎 Smart • Fast • Easy

🔥🌐⚡
""",reply_markup=keyboard)

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     if message.text == 'About me':
#         bot.send_message(message.chat.id, "Men Islombek Karimov.\n men 2009-yil tug'ilganman")
#     elif message.text == 'Contact':
#         bot.send_message(message.chat.id, "Telefon raqam: +998995767309\nEmail: islombekkarimov246@gmail.com")

@bot.message_handler(func=lambda message: message.text == 'About me')
def aboutme_handler(message):
    bot.send_message(message.chat.id,  """
👨‍💻 Islombek

🎂 25-April, 2009
🏫 School: 32-maktab

🚀 Python programmer
🌐 Web developer
🤖 Telegram bot creator

⚡ Tech lover
💎 Always improving skills

""")
@bot.message_handler(func=lambda message: message.text == "Contact")
def contact_handler(message):
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Telegram", url="https://t.me/karimovkarimov_bot")
    btn2 = types.InlineKeyboardButton("Linkedin", url="https://www.linkedin.com/in/islombek-karimov-b610a5408/")
    btn3= types.InlineKeyboardButton("Phone", url="tel:+998995767309")
    btn4= types.InlineKeyboardButton("Email", url="mailto:islombekkarimovvv246@gmail.com")
    keyboard.add(btn1, btn2)
    keyboard.add(btn3, btn4)

    text = "Men bilan bog'lanish uchun pastdagi linklarga bosing"

    bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Services')
def services_handler(message):
    bot.send_message(message.chat.id, "Bu qism tez orada qo'shiladi...")
@bot.message_handler(func=lambda message: message.text == 'Portfolio')
def portfolio_handler(message): 
    bot.send_message(message.chat.id, "Bu qism tez orada qo'shiladi...")
bot.infinity_polling()