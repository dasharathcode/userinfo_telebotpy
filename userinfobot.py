import telebot
from telebot import types

API_TOKEN = '7798592349:AAGrevQKvrj5rm01nzOv5R-gwXGqDfO4PJ0'  # Replace with your bot's API token
ADMIN_ID = '7068157354'  # Replace with your admin user ID
bot = telebot.TeleBot(API_TOKEN)

# Store user data
users = {}

# Sticker ID
STICKER_ID = "CAACAgUAAxkBAAEw5y1niRKNF20LFZM1mWYZbxLiielJyAACKwoAAtXisFR90jdNzygtfTYE"

# Start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_sticker(message.chat.id, STICKER_ID)  # Use the provided sticker ID
    user_info = f"Your Info ❤:\nUser ❤ID: {message.from_user.id}\nName❤: {message.from_user.first_name}\nLast Name❤: {message.from_user.last_name}\nUsername❤: @{message.from_user.username}"
    bot.send_message(message.chat.id, user_info)
    
    # Save user info
    users[message.from_user.id] = message.from_user
    bot.send_message(message.chat.id, "Type /help to see available commands ⚡.")


# Help command
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Available 😋 commands:\n"
        "/promot - Get 🤑promotion info.\n"
        "/start - Start😃 the bot and get your 👽info.\n"
        "/help - Show this☠ help message.\n"
        "/broadcast - Send a message to all users (admin 😎 only)."
    )
    bot.send_message(message.chat.id, help_text)


# Promote command
@bot.message_handler(commands=['promot'])
def send_promot(message):
    promot_text = "For 🤑promotion, please😚contact @KALI_LINUX_NET for more 😁 information."
    bot.send_message(message.chat.id, promot_text)


# Broadcast command (admin only)
@bot.message_handler(commands=['broadcast'])
def broadcast(message):
    if str(message.from_user.id) == ADMIN_ID:
        msg = bot.send_message(message.chat.id, "Please enter 😁the message to 🙄broadcast:")
        bot.register_next_step_handler(msg, handle_broadcast)
    else:
        bot.send_message(message.chat.id, "Only admin 😖 can do this.")


def handle_broadcast(message):
    for user_id in users:
        try:
            bot.send_message(user_id, message.text)
        except Exception as e:
            print(f"Failed to send message to {user_id}: {e}")
    bot.send_message(message.chat.id, "Broadcast 😁message😝 sent!")


# Data command (admin only)
@bot.message_handler(commands=['data'])
def send_data(message):
    if str(message.from_user.id) == ADMIN_ID:
        user_info = "\n".join([f"User ID: {user.id}, Name: {user.first_name}, Username: @{user.username}" for user in users.values()])
        bot.send_message(message.chat.id, f"User data:\n{user_info}")
    else:
        bot.send_message(message.chat.id, "Only 😚admin can do☺ this.")


# Start the bot
if __name__ == '__main__':
    bot.polling(none_stop=True)