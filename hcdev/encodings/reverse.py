#Author: noize


class Reverse:
    def __init__(self):
        pass

    def encode(self, text):
        return text[::-1]

    def decode(self, text):
        return self.encode(text)

reverse = Reverse()