class Error(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

    # try:
    #     raise Error(2*2)
    # except Error as e:
    #     print('My exception occurred, value:', e.value)

    # raise Error('oops!')