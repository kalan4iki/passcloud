# -*- coding: utf-8 -*-
from termcolor import colored, cprint
#from default import config_name, default_system, default_db, default_name_db, default_command
from commands import default_command
from Cryptodome.Cipher import ChaCha20
from base64 import b64encode, b64decode
import hashlib
import colorama
import configparser
import os.path

#Постоянные перемменые
config_name = "setting.ini"
default_system = ["ЕЦУР", "МСЭД", "Почта mosreg.ru", "VPN"]
default_db = 'local'
default_name_db = 'db.pass'

def decry(text, passw):
    #text - защифрованный текст
    #passw - пароль в md5
    config = readconfig()
    nonce = config['Programm']['nonce']
    nonce = b64decode(nonce)
    cipher = ChaCha20.new(key=passw.encode(), nonce=nonce)
    ret = b64decode(text)
    ret = cipher.decrypt(ret)
    return ret.decode('utf-8')
    

def newconfig():
    cprint('Создание файла конфигурации.', 'red')
    config = configparser.ConfigParser()
    password = input('Введите мастер пароль: ').encode()
    mdkh = hashlib.md5(password)
    mdk = mdkh.hexdigest()
    cipher = ChaCha20.new(key=mdk.encode())
    nonce = b64encode(cipher.nonce).decode('utf-8')
    config['Programm'] = {"system": default_system, 'db': default_db,
                          'defcommand': ['help', 'add', 'edit'], 'nonce': nonce}    
    with open(config_name, 'w') as configfile:
        config.write(configfile)

def readconfig():
    cprint('Чтение файла конфигурации.', 'red')
    if os.path.exists(config_name): #Проверка существования конфига
        config = configparser.ConfigParser()
        config.read(config_name)
        return config

def newdb():
    cprint('Создание базы данных.', 'red')
    db = configparser.ConfigParser()
    config = readconfig()
    system = eval(config['Programm']['system'])
    for i in system:
        db[i] = {}
    with open(default_name_db, 'w') as dbfile:
        db.write(dbfile)
    

def main():
    colorama.init()
    if os.path.exists(config_name) == False: #Проверка существования конфига
        newconfig()
    if os.path.exists(default_name_db) == False: #Проверка базы паролей
        newdb()
    config = readconfig()
    cprint('###Учет учетный записей и паролей###', 'green')
    cprint('###В данный момент есть следующие системы в базе###', 'green')
    a = ''
    for i in eval(config['Programm']['system']):
        a += '"'+ i + '" '
    cprint('###' + a + '###', 'blue')
    cprint('###Для помощи по командам введите help', 'green')
    command = config['Programm']['defcommand']
    while True:
        a = input('>> ')
        obr = a.split()
        print(obr)
        try:
            com = default_command[obr[0]]
            print(len(obr))
            if len(obr) == 1:
                com()
            else:
                arg = ''
                for i in obr[1:len(obr)]:
                    arg += i + ' '
                com(arg)
        except KeyError:
            cprint('Данной команды не существует, введите help', 'red')

if __name__ == "__main__":
    main()