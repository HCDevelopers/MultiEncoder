#By Ex094 for Deque's Project
class rot13:

    def encode(self, text):

        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        rotate = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijkl'

        enc = ''

        for char in text:

            if char == ' ':
                enc += ' '

            else:
                get = alpha.index(char)
                enc += rotate[get]

        return enc

    def decode(self, text):

        rotate = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijkl'
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

        dec = ''

        for char in text:

            if char == ' ':
                dec += ' '

            else:
                get = rotate.index(char)
                dec += alpha[get]
        return dec
