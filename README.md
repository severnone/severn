# Telegram Guessing Game Bot

This repository contains a simple Telegram bot that plays a number guessing game with users. The bot is written in Python using the `python-telegram-bot` library.

## Features
- `/start` — begins a new game and selects a random number between 1 and 100.
- `/help` — displays basic instructions.
- Users guess the number by sending messages with their guesses. The bot replies whether the guess is too high, too low, or correct.

The bot keeps track of the game state for each user using `context.user_data`.

## Setup
1. Install dependencies:
   ```bash
   pip install python-telegram-bot
   ```
2. Set the `BOT_TOKEN` environment variable to the token provided by `@BotFather`.
3. Run the bot:
   ```bash
   python3 main.py
   ```

The bot runs in polling mode and responds to commands in chat.
