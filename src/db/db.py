from db.connection import Connection

class DB(Connection):
    def __init__(self, table):
        super().__init__()
        self.__operators = ['=', '!=', '<', '>', '<=', '>=', 'like']
        self.__table = table
        self.__query = ''
        self.__where_params = ()
        self.__cursor = self._getCursor()

        if not table: raise Exception("MySQL Error: Table name not set.")

    def __endConnection(self):
        self._closeConnection()
        self.__query = ''
        self.__where_params = tuple()

    def __executeCommitQuery(self, query, params):
        self.__cursor.execute(query, params)
        self._commit()
        self.__endConnection()

    def _where(self, column, *props):
        values = list(self.__where_params)

        if len(props) == 2:
            value = str(props[1])

            if not self.__operators.count(props[0]):
                raise Exception("MySQL Error: The operator is invalid.")

            if not value.isalnum():
                raise Exception("MySQL Error: The value is invalid.")

            if props[0] == 'like':
                values.append(f'%{value}%')
            else:
                values.append(value)

            self.__query = f'WHERE {column} {props[0]} %s'
        else:
            value = str(props[0])

            if not value.isalnum():
               raise Exception("MySQL Error: The value is invalid.")

            self.__query = f'WHERE {column} = %s'
            values.append(value)

        self.__where_params = tuple(values)

        return self

    def _get(self):
        query = f"SELECT * FROM {self.__table} {self.__query}"
        self.__cursor.execute(query, self.__where_params)

        data = self.__cursor.fetchall()
        self.__endConnection()

        return data

    def _insert(self, data):
        columns = ', '.join(data.keys())
        values = tuple(data.values())
        binds = ', '.join(['%s'] * len(data))

        query = f"INSERT INTO {self.__table} ({columns}) VALUES ({binds})"
        self.__executeCommitQuery(query, values)

    def _update(self, data):
        columns = []
        values = []

        for column in data:
            columns.append(f'{column} = %s')
            values.append(data[column])

        columns = ', '.join(columns)
        values.extend(self.__where_params)

        query = f"UPDATE {self.__table} SET {columns} {self.__query}"
        self.__executeCommitQuery(query, values)

    def _delete(self):
        query = f"DELETE FROM {self.__table} {self.__query}"
        self.__executeCommitQuery(query, self.__where_params)