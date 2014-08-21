from fractions import gcd
from random import choice

class affine:

    global vals, chars

    vals = []

    chars = 'abcdefghijklmnopqrstuvwxyz'

    def gencoprime(text):

        for char in text:

            mod = chars.index(char)

            if gcd(mod, len(chars)) == 1:

                vals.append(mod)

    def encode(self, text):

        enc = ''

        affine.gencoprime(text)

        a,b = vals[0],choice(vals)

        for char in text:

            get = chars.index(char)

            form = ((a * get + 8) % 26)

            enc += chars[form]

        return '%s %d' % (enc, a)

    def decode(self, text, a):

        dec = ''

        for i in range(26):

            if ((i * a) % 26) == 1:
                val = i

        for char in text:

            get = chars.index(char)

            stp1 = (val * (get - 8)) % 26

            dec += chars[stp1]

        return dec