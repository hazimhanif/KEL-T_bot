'''
Created on Aug 26, 2015

@author: hazimhanif
'''

import telebot
from telebot import *

import esquery
from esquery import *



API_TOKEN = '91095561:AAFfiJD9No-wpWkuBIZNYcp1FQlzyX2DAnQ'

bot = telebot.TeleBot(API_TOKEN)
#bot = telebot.AsyncTeleBot(API_TOKEN)

user_dict = {}



# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am PTM UM ES-PyBot.
I'm here to provide you with the insight of the elasticsearch cluster that currently contains DNS and Firewall Log.
Cheers!
:)\
""")

# Handle '/help'
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, """\
How to use the robot:-
Just simply type in /es and enjoy !.
\
""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(commands=['es'])
def es_message(message):
        try:           
                markup = types.ReplyKeyboardMarkup(row_width=3,one_time_keyboard=True)
                markup.row('Fortigate Firewall')
                markup.row('DNS')                                                               
                msg=bot.reply_to(message, "Please select the type of log to query",reply_markup=markup)
            
                bot.register_next_step_handler(msg, time_query_step)
        except Exception as e:
                print(e)

def time_query_step(message):
        try:
                markup = types.ReplyKeyboardMarkup(row_width=3,one_time_keyboard=True)
                markup.row('Last 15 mins')
                markup.row('Last 30 mins')          
                markup.row('Last 1 hour')   
                markup.row('Last 12 hours')   
                markup.row('Last 24 hours')                                                        
                msg=bot.reply_to(message, "Please select the time range",reply_markup=markup)
                bot.register_next_step_handler(msg, type_query_step)

        except Exception as e:
            print(e)


def type_query_step(message):
        try:
                markup = types.ReplyKeyboardMarkup(row_width=3,one_time_keyboard=True)
                markup.row('Top 10 Destination Country')
                markup.row('Top 10 Destination IP')
                markup.row('Top 10 Source Country')
                markup.row('Top 10 Source IP')
                markup.row('Top 10 Status')
                markup.row('Top 10 Level')
                markup.row('Top 10 Reason')
                markup.row('Top 10 Message')                                                                  
                msg=bot.reply_to(message, "Please select the query",reply_markup=markup)
                bot.register_next_step_handler(msg, all_query_step)
        except Exception as e:
            print(e)

def all_query_step(message):
        try:
            query=message.text
            if query=="Top 10 Destination Country":
                bot.reply_to(message,esquery.top_10_destination_country())
            elif query=="Top 10 Destination IP":
                bot.reply_to(message,esquery.top_10_destination_ip())
            elif query=="Top 10 Source Country":
                bot.reply_to(message,esquery.top_10_source_country())  
            elif query=="Top 10 Source IP":
                bot.reply_to(message,esquery.top_10_source_ip())  
            elif query=="Top 10 Status":
                bot.reply_to(message,esquery.top_10_status())  
            elif query=="Top 10 Level":
                bot.reply_to(message,esquery.top_10_level())  
            elif query=="Top 10 Reason":
                bot.reply_to(message,esquery.top_10_reason())   
            elif query=="Top 10 Message":
                bot.reply_to(message,esquery.top_10_message())     
            else:
                 bot.reply_to(message, 'Sorry, wrong parameters. Try again')   
        except Exception as e:
            print(e)


bot.polling()

while True:
    pass