# import subprocess

from django.shortcuts import render, redirect

# Create your views here.
from .tele_bot import *


def home(request):
    # data = get_response('fat')
    users = TeleBot.objects.all()
    return render(request, 'home/home.html', {'users': users})


def bot_run(request):
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    # dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CallbackQueryHandler(press_button_callback))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(0)
    updater.idle()
