#Author: Psycho_Coder
#

import string,random

class HCPyEncoder:

    def XORencrypt(self,plaintext,key):
        cipher=""
        for chars in plaintext:
            for char in key:
                chars=chr(ord(chars) ^ ord(char))
            cipher=cipher+chars
        return cipher

    def encode(self,plaintext,key):
        cipher= self.XORencrypt(plaintext,key)      
        return cipher
    
    def decode(self,ciphertext,key):
        plain= self.XORencrypt(ciphertext,key)
        return plain

    def generateKey(self,keyLen=10):
        pad = string.letters + string.digits
        return ''.join(random.Random().sample(pad, keyLen))

xor = HCPyEncoder()
