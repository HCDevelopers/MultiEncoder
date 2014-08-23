#Author: Psycho_Coder

from string import digits, ascii_letters
from random import Random


class HCPyEncoder:

    def __init__(self):
        pass

    @staticmethod
    def xor_encrypt(plaintext, key):

        cipher = ""
        for chars in plaintext:
            for char in key:
                chars = chr(ord(chars) ^ ord(char))
            cipher = cipher+chars
        return cipher

    def encode(self, plaintext, key):
        cipher = self.xor_encrypt(plaintext, key)
        return repr(cipher)
    
    def decode(self, ciphertext, key):
        plain = self.xor_encrypt(eval(ciphertext), key)
        return plain

    @staticmethod
    def generate_key(keyLen=10):
        pad = ascii_letters + digits
        return ''.join(Random().sample(pad, keyLen))

xor = HCPyEncoder()