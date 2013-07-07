#Binary Converter
#By Ex094

class txt2bin:

    def encode(self, text):
        
        enc = ''

        for char in text: enc += bin(ord(char))[2:].zfill(8)
        return enc

    def decode(self, text):

        dec = ''
        txt = []

        for x in range(int(len(text) / 8)): txt.append(text[x * 8 : (x * 8) + 8])

        for item in txt: dec += chr((int(item, 2)))

        return dec

binary = txt2bin()
