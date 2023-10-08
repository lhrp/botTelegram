import telebot, requests, os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


CHAVE_API = os.environ.get("CHAVE_API")
bot = telebot.TeleBot(CHAVE_API)


###########################################################################
@bot.message_handler(commands=["1"])
def func01(mensagem):
  bot.reply_to(mensagem, "Opção 01")
###########################################################################
###########################################################################
@bot.message_handler(commands=["3"])
def func02(mensagem):
  bot.reply_to(mensagem, "Opção 03")
###########################################################################

def verificar(mensagem):
  return True

@bot.message_handler(func=verificar)
def responder(mensagem):
  texto = """
    Escolha uma opção para continuar (Clique no item):
     /1 Consulta Usuário
     /2 Consultar CEP
     /3 Consultar CNPJ
Qualquer outro comando diferente dos mencionados acima não irá funcionar!!!"""
  bot.reply_to(mensagem, texto)

bot.polling()