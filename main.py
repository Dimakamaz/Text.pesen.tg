import lyricsgenius 
import telebot 
import flask
import os
from telebot import types

server = flask.Flask(__name__)
app_name = 'textpesentg'

token_bot = '5764000123:AAE9g6Xdrg_iPf2vESpSJ_Hlwp6sNtXxDlA' 
bot = telebot.TeleBot(token_bot) 
 
token = 'EnCFUWr6Gt190uRmIRezRf8ymCfMaQah1UZ9DwiunbvX0iXYqpt3YJFsV7FEG8oN' 
genius = lyricsgenius.Genius(token) 
 
@bot.message_handler(commands = ['start']) 
def start(msg): 
    bot.send_message(msg.chat.id, 'Введи название своего артиста/групы и трек через тире.') 
 
@bot.message_handler(content_types=['text']) 
def lyrics (msg): 
    result = msg.text.split('-') 
 
    song = genius.search_song(result[1], result[0]) 
    bot.send_message(msg.chat.id, song.lyrics) 
 
 
@server.route('/' + token_bot, methods=['POST'])
def get_message():
      bot.process_new_updates([types.Update.de_json(flask.request.stream.read().decode("utf-8"))])
      return "!", 200

@server.route('/', methods=["GET"])
def index():
    print("hello webhook!")
    bot.remove_webhook()
    bot.set_webhook(url=f"https://{app_name}.herokuapp.com/{token_bot}")
    return "Hello from Heroku!", 200


if __name__ == '__main__':
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

