import random
import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'web_bot.settings'
django.setup()

import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import *
from .helpers import get_response
from .models import TeleBot

API_KEY = '1911758206:AAFeV4L8yMNVyTWpKOjxhZaYMY1Ah2RktXY'

# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
    # update.message.reply_text('Hello there! I\'m a bot. What\'s up?. Feel free to chat with me.!')
    keyboard = [
        [InlineKeyboardButton("Stupid", callback_data='stupid')],
        [InlineKeyboardButton("Dumb", callback_data='dumb')],
        [InlineKeyboardButton("Fat", callback_data='fat')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message_reply_text = 'Select any option'
    update.message.reply_text(message_reply_text, reply_markup=reply_markup)


def press_button_callback(update, context):
    # reply_markup = InlineKeyboardMarkup([])
    text = str(update.callback_query.data).lower()
    a = update["callback_query"]  # get the query to collect data
    user_id = a.message.chat.id
    data = a.data
    username = a.message.chat.username
    first_name = a.message.chat.first_name
    tele, created = TeleBot.objects.get_or_create(userid=user_id)
    tele.user_id = user_id
    tele.username = username
    tele.first_name = first_name

    if data == 'fat':     # increment one of the button
        tele.fat_btn = tele.fat_btn+1
    elif data == 'dumb':
        tele.dumb_btn = tele.dumb_btn+1
    elif data == 'stupid':
        tele.stupid_btn = tele.stupid_btn + 1

    tele.save()

    print(tele.username, tele.dumb_btn, tele.fat_btn, tele.stupid_btn, )
    response = get_response(text)  # get the response
    update.callback_query.message.reply_text(text=response)


def help_command(update, context):
    update.message.reply_text('Try typing anything and I will do my best to respond!')


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}: {update.message.chat.username}) says: {text}')

    user = update.message.chat.username
    user_id = update.message.chat.id

    # Bot response
    response = get_response(text)
    print(f'User {user_id}: {user} : {text} \n{response}')
    update.message.reply_text(response)


def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')