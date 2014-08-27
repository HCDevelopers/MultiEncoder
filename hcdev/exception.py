class HCDevError(Exception):
    """Base class for exceptions in the hcdev module"""
    pass

class EncodeInputError(HCDevError):
    """Raised if input for an encoding was wrong."""

    def __init__(self, msg):
        self.msg = msg
