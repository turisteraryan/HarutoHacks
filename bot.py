import telebot
import requests

# Your bot token
API_TOKEN = '7650154311:AAEXzWOOdwWKU8sT7uJDi1S-dIrjyqR6WHA'
ADMIN_CHAT_ID = '1824621252'  # Replace with your own chat ID

# Initialize the bot
bot = telebot.TeleBot(API_TOKEN)

# Start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Haruto Hacks! This bot is for educational purposes.")
    
    # Provide a button to visit GitHub website
    markup = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton("Visit GitHub Website", url="https://your-github-username.github.io/your-repo")
    markup.add(button)
    
    bot.send_message(message.chat.id, "Click the button below to visit the website.", reply_markup=markup)

# Receive visitor details
@bot.message_handler(func=lambda message: True)
def receive_visitor_details(message):
    if message.chat.id == ADMIN_CHAT_ID:
        bot.reply_to(message, "Visitor details received.")
    else:
        bot.send_message(ADMIN_CHAT_ID, f"New visitor details:\n{message.text}")

# Polling for new messages
bot.polling()
