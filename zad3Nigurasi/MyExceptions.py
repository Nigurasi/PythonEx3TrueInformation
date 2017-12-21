class WrongArgumentException(Exception):
    def __init__(self):
        super(Exception, self).\
            __init__("<WrongArgumentException> One of "
                     "arguments is wrong.")
