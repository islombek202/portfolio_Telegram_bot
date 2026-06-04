import telebot
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv() 

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1=types.KeyboardButton('About me🙋')
    btn2=types.KeyboardButton('Contact📞')
    btn3=types.KeyboardButton('Services💼')
    btn4=types.KeyboardButton('Portfolio🖼️')
    keyboard.add(btn1, btn2)
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

@bot.message_handler(func=lambda message: message.text == 'About me🙋')
def aboutme_handler(message):
    bot.send_message(message.chat.id,  """
👨‍💻 Islombek
-----------------------
🎂 25-April, 2009
🏫 School: 32-maktab
-----------------------
🚀 Python programmer
🌐 Web developer
🤖 Telegram bot creator
-----------------------
⚡ Tech lover
💎 Always improving skills

""")
@bot.message_handler(func=lambda message: message.text == 'Contact📞')
def contact_handler(message):
    keyboard = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(
        "📱 Telegram",
        url="https://t.me/karimovkarimov_bot"
    )

    btn2 = types.InlineKeyboardButton(
        "💼 LinkedIn",
        url="https://www.linkedin.com/in/islombek-karimov-b610a5408/"
    )
    btn3 = types.InlineKeyboardButton("📷 Instagram", url="https://www.instagram.com/islombek_karimov192/")
    btn4 = types.InlineKeyboardButton("🐙 GitHub", url="https://github.com/islombek202")
    keyboard.add(btn1, btn2)
    keyboard.add(btn3, btn4)

    text1 = """
📞 Contact information

☎️ Phone: +998 99 576 73 09
📧 Email: islombekkarimovvv246@gmail.com

👇 Quyidagi linklar orqali bog‘laning
"""

    bot.send_message(
        message.chat.id,
        text1,
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: message.text == 'Services💼')
def services_handler(message):
    btn1=types.InlineKeyboardButton("Dasturlash👨🏻‍💻", url="https://t.me/karimovkarimov_bot")
    btn2=types.InlineKeyboardButton("Veb-ishlanmalar🌐", url="https://t.me/karimovkarimov_bot")
    btn3=types.InlineKeyboardButton("Telegram botlar🤖", url="https://t.me/karimovkarimov_bot")
    btn4=types.InlineKeyboardButton("Konsultatsiya💬", url="https://t.me/karimovkarimov_bot")
    keyboard=types.InlineKeyboardMarkup()
    keyboard.add(btn1, btn2)
    keyboard.add(btn3, btn4)
    bot.send_message(message.chat.id, "Bizning xizmatlarimiz:\n1. Dasturlash👨🏻‍💻\n2. Veb-ishlanmalar🌐\n3. Telegram botlar🤖\n4. Konsultatsiya💬",reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Portfolio🖼️')
def portfolio_handler(message): 
    
    text3 = """*Loyihalarim*

1. **Cyrllic_to_Latin/Latin_to_Cyrllic convertor bot** 💻  
   [Telegram Bot](https://t.me)

2. **SHOP.uz-portfolio_web-site** 🛒  
   [Vercel Website](https://shop-uz-portfolio-web-site.vercel.app)

3. **Counter-hisoblagich** 🧮  
   [Vercel Website](https://counter-hisoblagich.vercel.app)

4. **Tic-Tac-Toe** ❌⭕  
   [Vercel Website](https://tic-tac-toe-kappa-two-24.vercel.app)

5. **iOS Calculator** 📱  
   [Vercel Website](https://ios-calculator-example.vercel.app)"""

    bot.send_message(message.chat.id, text3, parse_mode="Markdown")


bot.infinity_polling()