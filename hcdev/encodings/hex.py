#Author: Psycho_Coder
#

import binascii

class HCPyEncoder:

    def encode(self,plaintext):        
        return binascii.hexlify(plaintext)
    
    def decode(self,ciphertext):
        return binascii.unhexlify(ciphertext)

hex = HCPyEncoder()
