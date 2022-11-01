import lyricsgenius 
import telebot 
 
token_bot = '5764000123:AAE9g6Xdrg_iPf2vESpSJ_Hlwp6sNtXxDlA' 
bot = telebot.TeleBot(token_bot) 
 
token = 'EnCFUWr6Gt190uRmIRezRf8ymCfMaQah1UZ9DwiunbvX0iXYqpt3YJFsV7FEG8oN' 
genius = lyricsgenius.Genius(token) 
 
@bot.message_handler(commands = ['start']) 
def start(msg): 
    bot.send_message(msg.chat.id, 'Введи название своей артиста/групы и трек через пробел.') 
 
@bot.message_handler(content_types=['text']) 
def lyrics (msg): 
    result = msg.text.split('-') 
 
    song = genius.search_song(result[1], result[0]) 
    bot.send_message(msg.chat.id, song.lyrics) 
 
 
bot.polling()

