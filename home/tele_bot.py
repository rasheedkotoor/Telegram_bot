import random
import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'web_bot.settings'
django.setup()

from .helpers import get_response
from .models import TeleBot, Messages
import logging
from telegram.ext import *
import responses

API_KEY = '1911758206:AAEf5x4yCgrMKY_xLuGUHToub7rw2AaZ2PY'

# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot. What\'s up?. Feel free to chat with me.!')


def help_command(update, context):
    update.message.reply_text('Try typing anything and I will do my best to respond!')


def custom_command(update, context):
    update.message.reply_text('This is a custom command, you can add whatever text you want here.')


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}: {update.message.chat.username}) says: {text}')

    user = update.message.chat.username
    first_name = update.message.chat.first_name
    user_id = update.message.chat.id
    old_user, created = TeleBot.objects.get_or_create(userid=user_id, username=user, first_name=first_name)
    if not created:
        print(" not created ")
        a = Messages.objects.create(user=old_user, text=text)
        print(a.user, a.text)

    # Bot response
    response = get_response(text)

    update.message.reply_text(response)


def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')
