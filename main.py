import os
import random
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

TOKEN = os.environ.get("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = random.randint(1, 100)
    context.user_data["number"] = number
    context.user_data["tries"] = 0
    await update.message.reply_text(
        "I have chosen a number between 1 and 100. Try to guess it by sending a number."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Send /start to start a new game. Then send your guesses as numbers."
    )


async def handle_guess(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "number" not in context.user_data:
        await update.message.reply_text("Use /start to start a new game.")
        return
    try:
        guess = int(text)
    except ValueError:
        await update.message.reply_text("Please send a valid number.")
        return

    context.user_data["tries"] += 1
    number = context.user_data["number"]

    if guess < number:
        await update.message.reply_text("Too low!")
    elif guess > number:
        await update.message.reply_text("Too high!")
    else:
        tries = context.user_data["tries"]
        await update.message.reply_text(
            f"Correct! You guessed the number in {tries} tries."
        )
        context.user_data.clear()


def main():
    if not TOKEN:
        print("Please set the BOT_TOKEN environment variable.")
        return
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_guess)
    )

    application.run_polling()


if __name__ == "__main__":
    main()
