from termcolor import colored, cprint
#from default import config_name, default_system, default_db, default_name_db

import colorama

def crypto():
    a = ''
    
def decrypto():
    a = ''

class Command():
    def helps(self, ):
        print(self.helps)
    
    
class wath(Command):
    helps = 'Test help' 
    def wath(self, *args):
        cprint('test wath', 'red')

class helps:
    def help():
        print('Команда помощи по всем командам')
    def __init__(self, *args):
        cprint('test','green')
        if len(args) > 0:
            try:
                for i in args: #BUG Не видит команду
                    a = default_command[i]
                    print(a.helps)
            except KeyError:
                cprint('Данной команды не существует, введите help')
                    

default_command = {'help': helps, 'wath': wath}    
