class ContextDoesntExist(BaseException):
    """A contextual information does not exist"""
    def __init__(self, msg):
        super().__init__(msg)