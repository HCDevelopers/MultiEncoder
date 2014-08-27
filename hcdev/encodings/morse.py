# Author: Ex094
from hcdev.exception import EncodeInputError

class ex094morse:
    def __init__(self):
        pass

    morse_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    morse_encode = ['.-', '-...', '-.-.', '-.', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.',
                    '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----',
                    '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

    def encode(self, text):
        store = ''
        for item in text.upper():
            if not item in self.morse_alpha:
                raise EncodeInputError("Allowed alphabet: " + self.morse_alpha)
            store += self.morse_encode[self.morse_alpha.find(item)] + ' '
        return store

    def decode(self, text):
        store = ''
        for item in text.split():
            if not item in self.morse_encode:
                raise EncodeInputError("Allowed alphabet: " + ', '.join(self.morse_encode))
            store += self.morse_alpha[self.morse_encode.index(item)]
        return store


morse = ex094morse()
