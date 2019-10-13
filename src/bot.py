#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time

TOKEN = '798025410:AAFa9cRNj70vh0e-bo88O59BosuGDX2NrfM'

import logging

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

INTERACTION = range(1)

def start(update, context):

    user = update.message.from_user
    logger.info("User: %s", user.first_name)
    update.message.reply_text(
        'Hello *{}*! I am Hack the Crash ChatBot 🚗🤖 and I will help you to reach to your destination safely'.format(user.first_name), parse_mode=ParseMode.MARKDOWN)
    update.message.reply_text('Where are you heading?')

    return INTERACTION


def interaction(update, context):
    
    text = update.message.text
    update.message.reply_text('Analyzing route to *{}*...'.format(text), parse_mode=ParseMode.MARKDOWN)
    time.sleep(2)
    update.message.reply_text('Here is some personalized advice just for you:')
    time.sleep(1)
    update.message.reply_text("1️⃣ Respect the speed limit, the road ahead is bumpy!")
    time.sleep(1)
    update.message.reply_text('2️⃣ Make sure your car has been checked before you head off')
    time.sleep(1)
    update.message.reply_text('3️⃣ Be mindful of the following blind spots:')
    time.sleep(1)
    update.message.reply_text('Specially on *A151*, *3* recent accidents occurred on *Sunday* in this area!', 
            parse_mode=ParseMode.MARKDOWN)
    update.message.reply_photo(
        photo=open('figures/edenham.png', 'rb'),
        caption="Dangerous area detected")

    return MENU

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def done():
    print('Done!')

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(

        entry_points=[CommandHandler('start', start)],
        states={

            INTERACTION: [ 
                MessageHandler(Filters.text, interaction) 
            ]
        }, fallbacks=[MessageHandler(Filters.regex('^Done$'), done)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    print('Starting Bot...')
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()