from random import randint
import telebot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
import json
import pyjokes
import random
from telebot import types

bot = telebot.TeleBot("API KEY")
file_path = 'films.json'
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт, цей бот може рекомендувати фільми, музику,"
                                      "ігри за жанрами, анекдоти, цікаві історії, а також надати можливість пограти в гру.\n"
                                      "Більше ти можеш дізнатись за командою командою /help")


@bot.message_handler(commands=['help'])
def help_list(message):
    bot.send_message(message.chat.id,
                     "В цього бота є такі функції як:\n"
                     "Рекомендувати фільм - /film\n"
                     "Рекомендувати музику - /music\n"
                     "Рекомендувати ігри за жанрами - /game\n"
                     "Розказати анекдот - /joke\n"
                     "Розказати цікаву історію - /history\n"
                     "Також ти можеш пограти в міні гру - /minigame")


@bot.message_handler(commands=['film'])
def help_for_film(message):
    key_board = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = KeyboardButton(text='Драма')
    button2 = KeyboardButton(text='Кримінал')
    button3 = KeyboardButton(text='Екшн')
    button4 = KeyboardButton(text='Фентезі')
    button5 = KeyboardButton(text='Пригоди')
    button6 = KeyboardButton(text='Трилер')
    button7 = KeyboardButton(text='Комедія')
    button8 = KeyboardButton(text='Наукова фантастика')
    button9 = KeyboardButton(text='Повернутись в меню')
    key_board.add(button1, button2, button3, button4, button5, button6, button7, button8, button9)
    bot.send_message(message.chat.id, "Виберіть жанр фільму: ", reply_markup=key_board)
    bot.register_next_step_handler(message, send_film_recommendation)


def send_film_recommendation(message):
    sent_message = message.text
    key_board = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = KeyboardButton(text='Повернутись в меню')
    key_board.add(button)
    if sent_message == 'Повернутись в меню':
        help_list(message)
        return
    elif sent_message in data:
        recomend = "\n".join(film['title'] for film in data[sent_message])
        bot.send_message(message.chat.id, f"Рекомендації у жанрі {sent_message}:\n{recomend}", reply_markup=key_board)
    else:
        bot.send_message(message.chat.id, "Вибачте, я не розумію цей жанр. Спробуйте ще раз.")
        help_for_film(message)


@bot.message_handler(commands=['music'])
def help_for_music(message):
    key_board = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = KeyboardButton(text='Поп')
    button2 = KeyboardButton(text='Рок')
    button3 = KeyboardButton(text='Реп')
    button4 = KeyboardButton(text='Електронна')
    button5 = KeyboardButton(text='Фолк')
    button6 = KeyboardButton(text='Повернутись в меню')
    key_board.add(button1, button2, button3, button4, button5, button6)
    bot.send_message(message.chat.id, "Виберіть жанр музики: ", reply_markup=key_board)
    bot.register_next_step_handler(message, send_music_recommendation)


def send_music_recommendation(message):
    sent_message = message.text
    key_board = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = KeyboardButton(text='Повернутись в меню')
    key_board.add(button)
    if sent_message == 'Повернутись в меню':
        help_list(message)
        return
    elif sent_message in data:
        recomend = "\n".join(music['title'] for music in data[sent_message])
        bot.send_message(message.chat.id, f"Рекомендації у жанрі {sent_message}:\n{recomend}", reply_markup=key_board)
    else:
        bot.send_message(message.chat.id, "Вибачте, я не розумію цей жанр. Спробуйте ще раз.")
        help_for_music(message)


@bot.message_handler(commands=['game'])
def help_for_game(message):
    key_board = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = KeyboardButton(text='Екшин')
    button2 = KeyboardButton(text='Пригоди')
    button3 = KeyboardButton(text='РПГ')
    button4 = KeyboardButton(text='Стратегії')
    button5 = KeyboardButton(text='Спорт')
    button6 = KeyboardButton(text='Головоломки')
    button7 = KeyboardButton(text='Повернутись в меню')
    key_board.add(button1, button2, button3, button4, button5, button6, button7)
    bot.send_message(message.chat.id, "Виберіть жанр игри: ", reply_markup=key_board)
    bot.register_next_step_handler(message, send_game_recommendation)


def send_game_recommendation(message):
    sent_message = message.text
    key_board = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = KeyboardButton(text='Повернутись в меню')
    key_board.add(button)
    if sent_message == 'Повернутись в меню':
        help_list(message)
        return
    elif sent_message in data:
        recomend = "\n".join(game['title'] for game in data[sent_message])
        bot.send_message(message.chat.id, f"Рекомендації у жанрі {sent_message}:\n{recomend}", reply_markup=key_board)
    else:
        bot.send_message(message.chat.id, "Вибачте, я не розумію цей жанр. Спробуйте ще раз.")
        help_for_game(message)


@bot.message_handler(commands=['joke'])
def joke_list(message):
    joke = pyjokes.get_joke("en")
    bot.send_message(message.chat.id, joke)
    help_list(message)
    return


def load_stories():
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)["Исторії"]


@bot.message_handler(commands=['history'])
def interesting_history(message):
    key_board = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = KeyboardButton(text='Повернутись в меню')
    key_board.add(button)
    stories = load_stories()
    selected_story = random.choice(stories)
    bot.send_message(message.chat.id, f"{selected_story['title']}\n\n{selected_story['story']}", reply_markup=key_board)


@bot.message_handler(commands=['minigame'])
def mini_game(message):
    key_board = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton(text='Камінь-ножиці-папір')
    button2 = types.KeyboardButton(text='Вгадай число')
    button3 = types.KeyboardButton(text='Виселица')
    button4 = types.KeyboardButton(text='Повернутись в меню')
    key_board.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, "Вибери гру в яку ми будемо грати: ", reply_markup=key_board)


@bot.message_handler(func=lambda message: message.text == 'Камінь-ножиці-папір')
def start_rock_paper_scissors(message):
    rock_paper_scissors(message)


def rock_paper_scissors(message):
    key_board = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton(text='Камінь')
    button2 = types.KeyboardButton(text='Ножиці')
    button3 = types.KeyboardButton(text='Папір')
    button4 = types.KeyboardButton(text='Повернутись в меню')
    key_board.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, "Обери варіант", reply_markup=key_board)
    bot.register_next_step_handler(message, determine_winner)


def determine_winner(message):
    user_choice = message.text
    options = ["Камінь", "Ножиці", "Папір"]
    bot_choice = random.choice(options)

    if user_choice == 'Повернутись в меню':
        help_list(message)
        return
    elif user_choice not in options:
        bot.send_message(message.chat.id, "Я не знаю такого знаку, спробуй ще раз")
        rock_paper_scissors(message)
        return

    if user_choice == bot_choice:
        result = f"Я викинув {bot_choice}, ти викинув {user_choice}. Нічия!"
    elif (user_choice == "Камінь" and bot_choice == "Ножиці") or \
            (user_choice == "Ножиці" and bot_choice == "Папір") or \
            (user_choice == "Папір" and bot_choice == "Камінь"):
        result = f"Я викинув {bot_choice}, ти викинув {user_choice}. Ти виграв!"
    else:
        result = f"Я викинув {bot_choice}, ти викинув {user_choice}. Я виграв!"

    bot.send_message(message.chat.id, result)
    rock_paper_scissors(message)


rand_number = 0


@bot.message_handler(func=lambda message: message.text == 'Вгадай число')
def random_number(message):
    global rand_number
    rand_number = random.randint(1, 100)
    key_board = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton(text='Повернутись в меню')
    key_board.add(button1)
    bot.send_message(message.chat.id,
                     "Число ми будемо вгадувати від 1 до 100. Напиши число, яке, як ти думаєш, я загадав.",
                     reply_markup=key_board)
    bot.register_next_step_handler(message, check_number)


def check_number(message):
    global rand_number
    user_text = message.text

    if user_text == 'Повернутись в меню':
        help_list(message)
        return

    if user_text.isdigit():
        user_number = int(user_text)
        if user_number > rand_number:
            bot.send_message(message.chat.id, "Меньше")
            bot.register_next_step_handler(message, check_number)
        elif user_number < rand_number:
            bot.send_message(message.chat.id, "Більше")
            bot.register_next_step_handler(message, check_number)
        else:
            bot.send_message(message.chat.id, f"Ти вгадав число! Це {rand_number}.")
            mini_game(message)
    else:
        bot.send_message(message.chat.id, "Це не число, введи число.")
        bot.register_next_step_handler(message, check_number)


words = [
    "будинок", "літо", "книга", "кіт", "машина", "яблуко", "сонце", "море", "школа", "зима",
    "птах", "ліжко", "дерево", "друг", "вікно", "хмара", "ринок", "чай", "сад",
    "квітка", "пісня", "метелик", "годинник", "село", "місто", "парк", "зірка", "корабель", "лікар"]
players = {}


@bot.message_handler(func=lambda message: message.text == 'Виселица')
def hangman_game(message):
    key_board = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton(text='Повернутись в меню')
    key_board.add(button1)

    word = random.choice(words)
    players[message.chat.id] = {
        "word": word,
        "attempts": 6,
        "guessed_letters": []
    }

    masked_word = "_" * len(word)
    bot.send_message(message.chat.id,
                     f"Я загадав слово: {masked_word}. У вас {players[message.chat.id]['attempts']} спроби(и).")
    bot.send_message(message.chat.id, "Введіть букву:", reply_markup=key_board)


@bot.message_handler(func=lambda message: message.chat.id in players)
def guess_letter(message):
    key_board = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton(text='Повернутись в меню')
    key_board.add(button1)

    player_data = players[message.chat.id]
    word = player_data["word"]
    attempts = player_data["attempts"]
    guessed_letters = player_data["guessed_letters"]

    letter = message.text.lower()

    if letter == 'повернутись в меню':
        del players[message.chat.id]
        mini_game(message)
        return

    if len(letter) != 1 or not letter.isalpha():
        bot.send_message(message.chat.id, "Будь ласка, введіть тільки одну букву.", reply_markup=key_board)
        return

    if letter in guessed_letters:
        bot.send_message(message.chat.id, "Ви вже вгадали цю букву.", reply_markup=key_board)
        return

    guessed_letters.append(letter)

    if letter in word:
        bot.send_message(message.chat.id, f"Вірно! Буква '{letter}' є в слові.", reply_markup=key_board)
    else:
        attempts -= 1
        player_data["attempts"] = attempts
        bot.send_message(message.chat.id,
                         f"На жаль, букви '{letter}' немає в слові. У вас залишилось {attempts} спроб.",
                         reply_markup=key_board)

    masked_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
    bot.send_message(message.chat.id, masked_word, reply_markup=key_board)

    if masked_word == word:
        bot.send_message(message.chat.id, f"Вітаю! Ви вгадали слово: {word}.", reply_markup=key_board)
        del players[message.chat.id]
        mini_game(message)
    elif attempts <= 0:
        bot.send_message(message.chat.id, f"Гра закінчена. Ви програли. Слово було: {word}.", reply_markup=key_board)
        del players[message.chat.id]
        mini_game(message)
    else:
        bot.send_message(message.chat.id, "Введіть наступну букву:", reply_markup=key_board)


@bot.message_handler(func=lambda message: True)
def handle_other_messages(message):
    if message.text == "Повернутись в меню":
        help_list(message)
    else:
        bot.send_message(message.chat.id, "Я не зрозумів ваше повідомлення. Спробуйте ще раз.")
        help_list(message)


bot.infinity_polling()
