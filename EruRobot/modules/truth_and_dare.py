import html
import random
import EruRobot.modules.truth_and_dare_string as truth_and_dare_string
from EruRobot import dispatcher
from telegram import ParseMode, Update, Bot
from EruRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async


def truth(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))


def dare(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))
    
def sigma(update: Update, context: CallbackContext):
    update.effective_message.reply_video(random.choice(truth_and_dare_string.SIGMA))



TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth, run_async=True)
SIGMA_HANDLER = DisableAbleCommandHandler("sigma", sigma, run_async=True)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare, run_async=True)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
dispatcher.add_handler(SIGMA_HANDLER)
