#Author: Psycho_Coder

from string import digits, letters
from random import Random


class HCPyEncoder:

    def __init__(self):
        pass

    def XORencrypt(self, plaintext, key):

        cipher = ""
        for chars in plaintext:
            for char in key:
                chars = chr(ord(chars) ^ ord(char))
            cipher = cipher+chars
        return cipher

    def encode(self, plaintext, key):
        cipher = self.XORencrypt(plaintext, key)
        return repr(cipher)
    
    def decode(self, ciphertext, key):
        plain = self.XORencrypt(eval(ciphertext), key)
        return plain

    @staticmethod
    def generateKey(keyLen=10):
        pad = letters + digits
        return ''.join(Random().sample(pad, keyLen))

xor = HCPyEncoder()