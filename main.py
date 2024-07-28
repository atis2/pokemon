import telebot 
from config import token
from random import randint
from logic import Pokemon , Fighter , Wizard

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    laki = randint(1,2)
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Fighter(message.from_user.username) if laki == 2 else Wizard(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['info'])
def info(message):
    if  message.from_user.username not in Pokemon.pokemons.keys():
        bot.reply_to(message, "Ты ne создал себе покемона")
    else:
        pokemon = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())

@bot.message_handler(commands=['eat'])
def eat(message):
    pokemon = Pokemon.pokemons[message.from_user.username]
    bot.send_message(message.chat.id, pokemon.feed()) 




@bot.message_handler(commands=['fights'])
def fights(message):
    if message.reply_to_message:
        pokemon = Pokemon.pokemons[message.from_user.username]
        pokemonenemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
        bot.send_message(message.chat.id, pokemon.fight(pokemonenemy))





bot.infinity_polling(none_stop=True)

