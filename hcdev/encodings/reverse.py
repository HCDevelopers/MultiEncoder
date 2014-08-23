#Author: noize


class Reverse:
    def __init__(self):
        pass

    @staticmethod
    def encode(text):
        return text[::-1]

    def decode(self, text):
        return self.encode(text)


reverse = Reverse()