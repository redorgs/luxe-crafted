import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

class Connection:
    def __init__(self):
        self.__db_host = os.environ.get('DB_HOST')
        self.__db_name = os.environ.get('DB_DATABASE')
        self.__db_user = os.environ.get('DB_USERNAME')
        self.__db_pass = os.environ.get('DB_PASSWORD')

        try:
            self.__connection = mysql.connector.connect(
                host=self.__db_host,
                user=self.__db_user,
                password=self.__db_pass,
                database=self.__db_name
            )
        except mysql.connector.Error as e:
            print(f"MySQL Error: {e}")

    def _commit(self):
        self.__connection.commit()

    def _closeConnection(self):
        self.__connection.close()

    def _getCursor(self):
        return self.__connection.cursor()