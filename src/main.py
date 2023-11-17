import datetime
import os
from re import match
import bcrypt
from colorama import Fore, Style
import ulid
import pytz

from user import User
from utils.db import DB

utc = pytz.UTC


class Main:
    def __init__(self) -> None:
        self.__current_menu = 1
        self.__format = {
            'green': '\033[92m',
            'blue': '\033[94m',
            'bold': '\033[1m',
            'reset': '\033[00m'
        }

        self.__menu()
        self.__navigation()

        while True:
            if self.__current_menu == 2:
                path = '/shop'
            else:
                path = '/'

            user_choice = input(
                f'\n{self.__format["bold"] + self.__format["green"]}you@e-commerce{self.__format["reset"]}:{self.__format["bold"] + self.__format["blue"] + path + self.__format["reset"]}$ ')

            os.system('clear')

            if user_choice == '1':
                self.__current_menu = 2
                self.__listShop()
            else:
                self.__current_menu = 1
                self.__menu()

            self.__navigation()

    def __navigation(self):
        print()
        print('_1) Cart')
        print('_2) Shop History')
        print('_3) Home')

    def __extendSession(self):
        new_session_id = ulid.new().str

        f = open("../storage/session", "r")
        user_session = DB('sessions').where('id', f.read()).get()[0]
        f.close()

        f = open("../storage/session", "w")
        f.write(new_session_id)
        f.close()

        DB('sessions').where('user_id', user_session[1]).delete()
        DB('sessions').create({
            'id': new_session_id,
            'user_id': user_session[1]
        })

    def __checkSession(self):
        if not os.path.isfile('../storage/session'):
            self.__login()
            exit()

        f = open("../storage/session", "r")
        session_id = f.read()
        f.close()

        user_session = DB('sessions').where('id', session_id).get()
        session_date = ulid.from_str(session_id).timestamp().datetime + \
            datetime.timedelta(seconds=10)
        now = utc.localize(datetime.datetime.now())

        if session_date > now and len(user_session) > 0:
            self.__extendSession()
            self.__menu()
        else:
            self.__login()

        exit()

    def __listShop(self):
        for shop in DB('shop').get():
            print(shop)

    def __menu(self):
        os.system('clear')
        print('1) Shop')

    def __login(self):
        os.system('clear')

        email = input('Email: ')
        password = str.encode(input('Password: '))

        try:
            user = User().get(email=email)['data'][0]
            hashed_password = str.encode(user[2])
        except:
            self.__login()
            exit()

        if bcrypt.checkpw(password, hashed_password):
            the_id = ulid.new().str

            f = open("../storage/session", "w")
            f.write(the_id)
            f.close()

            DB('sessions').where('user_id', user[0]).delete()
            DB('sessions').create({
                'id': the_id,
                'user_id': user[0]
            })

            self.__menu()
        else:
            self.__login()

        exit()


if __name__ == '__main__':
    try:
        Main()
    except KeyboardInterrupt as e:
        os.system('clear')
        print('Selamat Jalan')
