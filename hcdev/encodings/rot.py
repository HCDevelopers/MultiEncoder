#By Ex094 for Deque's Project
class rot:

    def __init__(self, alpha, rotate):

        self.alpha = str(alpha)
        self.rotate = str(rotate)

    def encode(self, text):

        enc = ''

        for char in text:

            if char in self.alpha:
                get = self.alpha.index(char)
                enc += self.rotate[get]
            else: enc += char

        return enc

    def decode(self, text):
        return self.encode(text)


rot13 = rot("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")
rot18 = rot("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz", "RSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQnopqrstuvwxyzabcdefghijklm")
rot47 = rot("!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~", "PQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO")
rot5 = rot("0123456789", "5678901234")
