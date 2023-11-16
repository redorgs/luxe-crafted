import mysql.connector
from utils.db import DB
from utils.error_handler import StatusHandler


class User:
    def __init__(self):
        """
        Constructor to initialize a User object with an optional ID parameter.
        """

        self.__table = 'users'

    def create(self, **kwargs):
        """
        Create a new user with the provided attributes.
        """

        status = StatusHandler()

        try:
            DB(self.__table).create(kwargs)
        except mysql.connector.errors.DatabaseError as e:
            status.setStatusErrDB(e)

        return status.payload

    def get(self, *args, **kwargs):
        """
        Retrieve user data based on provided arguments (ID or specific columns).
        """

        status = StatusHandler()
        user = DB(self.__table)

        if len(args) > 0:
            user.where('id', args[0])
        elif len(kwargs) > 0:
            for column in kwargs:
                user.where(column, kwargs[column])

        try:
            status.payload['data'] = user.get()
        except mysql.connector.errors.DatabaseError as e:
            status.setStatusErrDB(e)

        return status.payload

    def search(self, value, column='email'):
        """
        Search for users based on a specific value in a column (default: email).
        """

        status = StatusHandler()

        try:
            status.payload['data'] = DB(self.__table).where(
                column, 'like', f'%{value}%'
            ).get()
        except mysql.connector.errors.DatabaseError as e:
            status.setStatusErrDB(e)

        return status.payload

    def update(self, id, **kwargs):
        """
        Update user information based on the provided attributes.
        """

        status = StatusHandler()

        try:
            DB(self.__table).where('id', id).update(kwargs)
        except mysql.connector.errors.DatabaseError as e:
            status.setStatusErrDB(e)

        return status.payload

    def delete(self, id):
        """
        Delete the user from the database.
        """

        status = StatusHandler()

        try:
            DB(self.__table).where('id', id).delete()
        except mysql.connector.errors.DatabaseError as e:
            status.setStatusErrDB(e)

        return status.payload

    def profile(self, id):
        '''
        Retrieves user profile data from the database using the provided 'id'.
        '''

        status = StatusHandler()

        try:
            status.payload['data'] = DB(
                'user_profile').where('user_id', id).get()[0]
        except mysql.connector.errors.DatabaseError as e:
            status.setStatusErrDB(e)
        except IndexError as e:
            status.setStatusErrIndex(e)

        return status.payload

    def isSeller(self, id):
        """
        Check if the user is a seller.
        """

        status = StatusHandler()

        try:
            shop = DB('shop').where('user_id', id).get()
            status.payload['data'] = True if len(shop) > 0 else False
        except mysql.connector.errors.DatabaseError as e:
            status.setStatusErrDB(e)

        return status.payload
