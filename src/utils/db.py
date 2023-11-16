from utils.connection import Connection


class DB:
    def __init__(self, table):
        # Initialize the database connection and cursor
        self.__connection = Connection().getConnection()
        self.__cursor = self.__connection.cursor()

        # Initialize variables for WHERE clause and table name
        self.__allowed_operator = ('<', '>', 'like')
        self.__where_query = ''
        self.__where_bind_data = ()
        self.__table = table

    def __setWhereQuery(self, column, operator):
        '''
        Set the WHERE clause for filtering data
        Example: WHERE column operator value

        e.g., WHERE name = 'John'
                OR
               WHERE age > 30
        operator can be '<', '>', or 'like'
        (assuming 'like' for pattern matching)
        This function is for internal use only
        '''

        if 'WHERE' in self.__where_query:
            self.__where_query += f' AND '
        else:
            self.__where_query += f' WHERE '

        self.__where_query += f'{column} {operator} %s'

    def __setWhereBindData(self, args):
        '''
        Set the data for binding parameters in WHERE clause

        Verify the operator and construct the binding data
        Example: ('John', '30') for WHERE name = 'John'
                  OR
                 ('30',) for WHERE age > 30
        This function is for internal use only
        '''

        operator = '='
        self.__where_bind_data = list(self.__where_bind_data)

        if len(args) > 1:
            self.__where_bind_data.append(args[1])

            if args[0] in self.__allowed_operator:
                operator = args[0]
            else:
                raise Exception(
                    f"invalid input. Only '<', '>', and 'like' operators are allowed")
        else:
            self.__where_bind_data.append(args[0])

        self.__where_bind_data = tuple(self.__where_bind_data)

        return operator

    def where(self, column, *args):
        '''
        Set the WHERE clause for filtering data
        Accepts arguments to specify conditions
        e.g., where('name', 'John') or where('age', '>', 30)
        '''

        if len(args) < 1:
            raise Exception('value parameter is missing')

        operator = self.__setWhereBindData(args)
        self.__setWhereQuery(column, operator)

        return self

    def create(self, payload):
        '''
        Create a new record in the database table
        Construct an INSERT query and execute it
        Return the last inserted ID
        '''

        columns = ' ,'.join(payload)
        binders = ', '.join(['%s'] * len(payload))
        values = tuple(payload.values())
        query = f'INSERT INTO {self.__table} ({columns}) VALUES ({binders})'

        self.__cursor.execute(query, values)
        self.__connection.commit()

        id = self.__cursor.lastrowid

        self.__cursor.close()
        self.__connection.close()

        return id

    def get(self):
        '''
        Retrieve records from the database table
        Construct a SELECT query with optional WHERE clause
        Execute the query and return the results
        '''

        query = f'SELECT * FROM {self.__table}{self.__where_query}'

        self.__cursor.execute(query, self.__where_bind_data)
        result = self.__cursor.fetchall()

        self.__cursor.close()
        self.__connection.close()

        return result

    def update(self, payload):
        '''
        Update records in the database table
        Construct an UPDATE query with SET and WHERE clauses
        Execute the query to update records
        '''

        update_query = ''

        for column in payload:
            update_query += f'{" SET" if "SET" not in update_query else ","} {column} = %s'

        query = f'UPDATE {self.__table}{update_query}{self.__where_query}'

        values = list(payload.values())
        values.extend(self.__where_bind_data)
        values = tuple(values)

        self.__cursor.execute(query, values)
        self.__connection.commit()

        self.__cursor.close()
        self.__connection.close()

    def delete(self):
        '''
        Delete records from the database table
        Construct a DELETE query with WHERE clause
        Execute the query to delete records
        '''

        query = f'DELETE FROM {self.__table}{self.__where_query}'

        self.__cursor.execute(query, self.__where_bind_data)
        self.__connection.commit()

        self.__cursor.close()
        self.__connection.close()
