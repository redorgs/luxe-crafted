class StatusHandler:
    def __init__(self):
        self.payload = {
            'error': False,
            'code': 0,
            'message': 'Success',
            'data': None
        }

    def setStatusErrDB(self, e):
        '''
        Set status as error due to database-related exception (e)
        Update payload values based on the database exception
        '''

        self.payload['error'] = True
        self.payload['code'] = e.errno
        self.payload['message'] = e.msg

    def setStatusErrIndex(self, e):
        '''
        Set status indicating an IndexError occurred.
        '''

        self.payload['error'] = True
        self.payload['code'] = 1
        self.payload['message'] = e.__str__()
