class IncorrectFieldValue(BaseException):
    """Field value is empty or incorrect"""
    def __init__(self, msg):
        super().__init__(msg)