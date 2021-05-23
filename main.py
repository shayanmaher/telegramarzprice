import telebot
import json
import requests
import flag
from persiantools.jdatetime import JalaliDateTime
import datetime ,pytz
from extract import extract_element_from_json
tz = pytz.timezone('Asia/Tehran')
fa=JalaliDateTime.now(tz).strftime('%c')
bot = telebot.TeleBot("1871250002:AAH6wKLiOJJ_QHNEdFvLR1qAB-o2iDOaSWY",parse_mode="MARKDOWN")
from extract import extract_element_from_json
endpoints='https://call17.tgju.org:443/ajax.json'
response= requests.get(endpoints)
dollar=extract_element_from_json(response.json(),['current','price_dollar_rl','p'])
euro=extract_element_from_json(response.json(),['current','price_eur','p'])
gb=extract_element_from_json(response.json(),['current','price_gbp','p'])
aed=extract_element_from_json(response.json(),['current','price_aed','p'])
kwd=extract_element_from_json(response.json(),['current','price_kwd','p'])
rub=extract_element_from_json(response.json(),['current','price_rub','p'])
tr=extract_element_from_json(response.json(),['current','price_try','p'])
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message,"قیمت دلار:{}ریال".format(dollar)+flag.flag('US')+"\n"+"قیمت یورو:{} ریال".format(euro)+flag.flag('EU')+"\n"+"قیمت پوند:{}ریال".format(gb)+flag.flag('GB')+"\n"+"قیمت درهم:{}ریال".format(aed)+flag.flag('AE')+"\n"+"قیمت دینار کویت: {}ریال".format(kwd)+flag.flag('KW')+"\n"+"قیمت روبل روسیه: {}ریال".format(rub)+flag.flag('RU')+"\n"+"قیمت لیر ترکیه: {}ریال".format(tr)+flag.flag('TR')+"\n"+"*آخرین بروز رسانی:{}*".format(fa))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()