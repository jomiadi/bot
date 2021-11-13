# -*- coding: utf-8 -*-
#импорт всего
import telebot
import pandas as pd
import numpy as np
import random
from telebot import types
bot = telebot.TeleBot('2100731217:AAFYneIp8lKq7h9xnkdckqnmvG09URwEdF4')
herokukey = 'https://git.heroku.com/kosmetichkabot.git'

# In[2]:


#Летуаль
def letoulie():
    df = pd.read_csv('letu/main.csv', sep = ';', engine='python')
    #чистим данные
    del df['param']
    del df['type']
    df['oldprice'].replace('', np.nan, inplace=True)
    df.dropna(subset=['oldprice'], inplace=True)
    #добавляем столбец со скидкой
    df['skidka'] = (1 - (df['price'] / df['oldprice'])) * 100
    df['skidka'] = df['skidka'].round()
    df = df.astype({'skidka': "Int64"})
    #фильтруем данные
    df = df.loc[df['available'] == True]
    df = df.loc[df['price'] < 3500]
    df = df.loc[df['price'] > 450]
    df = df.loc[df['skidka'] > 29]
    #извлекаем случайную позицию
    i = random.randint(1, len(df))
    oldprice = df.iloc[i]['oldprice']
    newprice = df.iloc[i]['price']
    skidka = df.iloc[i]['skidka']
    vendor = df.iloc[i]['vendor']
    vendor1 = vendor.replace(' ', '_')
    name = df.iloc[i]['name']
    image = df.iloc[i]['picture']
    link = df.iloc[i]['url']
    #формируем и отправляем сообщение
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Перейти к скидке', url=link)
    markup.add(btn_my_site)
    message = name + "\n\nСтарая цена: " + str(int(oldprice)) + " рублей\nНовая цена: " + str(int(newprice)) + " рублей" + "\nРазмер скидки: " + str(skidka) + "%" + "\n\n#" + vendor1 + "\n\n#Летуаль"
    bot.send_photo('@mamakusah', image, caption = message, reply_markup = markup)


# In[3]:


def zolotoe():
    df = pd.read_csv('gold/main.csv', sep = ';', engine='python')
    #чистим данные
    del df['type']
    df['oldprice'].replace('', np.nan, inplace=True)
    df.dropna(subset=['oldprice'], inplace=True)
    #добавляем столбец со скидкой
    df['skidka'] = (1 - (df['price'] / df['oldprice'])) * 100
    df['skidka'] = df['skidka'].round()
    df = df.astype({'skidka': "Int64"})
    #фильтруем данные
    df = df.loc[df['price'] < 3500]
    df = df.loc[df['price'] > 450]
    df = df.loc[df['skidka'] > 29]
    #извлекаем случайную позицию
    i = random.randint(1, len(df))
    oldprice = df.iloc[i]['oldprice']
    newprice = df.iloc[i]['price']
    skidka = df.iloc[i]['skidka']
    vendor = df.iloc[i]['vendor']
    vendor1 = vendor.replace(' ', '_')
    name = df.iloc[i]['name']
    image = df.iloc[i]['picture']
    link = df.iloc[i]['url']
    #формируем и отправляем сообщение
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Перейти к скидке', url=link)
    markup.add(btn_my_site)
    message = name + " " + vendor + "\n\nСтарая цена: " + str(int(oldprice)) + " рублей\nНовая цена: " + str(int(newprice)) + " рублей" + "\nРазмер скидки: " + str(skidka) + "%" + "\n\n#" + vendor1 + "\n\n#ЗолотоеЯблоко"
    bot.send_photo('@mamakusah', image, caption = message, reply_markup = markup)


# In[4]:


randomka = [1,1,1,1,1,1, 0, 0, 0, 0]
a = random.randint(0, len(randomka) - 1)
if randomka[a] == 1:
    letoulie()
else:
    zolotoe()


# In[ ]:




