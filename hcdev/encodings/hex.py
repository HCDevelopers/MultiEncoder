# Author: Psycho_Coder

import binascii


class HCPyEncoder:
    def __init__(self):
        pass

    def encode(self, plaintext):
        return binascii.hexlify(plaintext)

    def decode(self, ciphertext):
        return binascii.unhexlify(ciphertext)


hex = HCPyEncoder()
