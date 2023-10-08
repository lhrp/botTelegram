import telebot, requests, os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


CHAVE_API = os.environ.get("CHAVE_API")
bot = telebot.TeleBot(CHAVE_API)


###########################################################################
@bot.message_handler(commands=["1"])
@bot.message_handler(commands=["linkedin"])
def func01(mensagem):
  bot.reply_to(mensagem, "https://www.linkedin.com/in/leonardo-henrique-rangon-paulino")
###########################################################################
###########################################################################
@bot.message_handler(commands=["2"])
@bot.message_handler(commands=["twitch"])
def func01(mensagem):
  bot.reply_to(mensagem, "https://www.twitch.tv/lhrpp")
###########################################################################
###########################################################################
@bot.message_handler(commands=["3"])
@bot.message_handler(commands=["youtube"])
def func02(mensagem):
  bot.reply_to(mensagem, "https://www.youtube.com/@lhrpp")
###########################################################################
###########################################################################
@bot.message_handler(commands=["4"])
@bot.message_handler(commands=["github"])
def func02(mensagem):
  bot.reply_to(mensagem, "https://github.com/lhrp")
###########################################################################


def verificar(mensagem):
  return True

@bot.message_handler(func=verificar)
def responder(mensagem):
  texto = """
    Escolha uma opção para continuar (Clique no item):
     Linkedin (/1 ou /linkedin)
     Twitch (/2 ou /twitch)
     YouTube (/3 ou /youtube)
     Github (/4 ou /githun)
Qualquer outro comando diferente dos mencionados acima não irá funcionar!!!"""
  bot.reply_to(mensagem, texto)

bot.polling()