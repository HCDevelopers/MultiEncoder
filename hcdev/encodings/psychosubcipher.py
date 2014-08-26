class HCPyEncoder:
    """
    Here we create a constructor and initialise the alphabets and substitution dictionary.
    This dictionary remains same for all types of plaintext given.
    """

    def __init__(self):
        self.alphabets = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_+|:"<>-=[];,.?'
        self.dictionary = '7D#+[~Zg%u<K8@]Jr Q4-j>dO^:aU,&!AC2xVy(Y;Gzp|LbSMqB*WT0fEls$PXi)cN6RoF3mHn9e_.1"vt=?wI5hk'

    """
    We pass the plaintext and the corresponding alphabets are replaced with the alphabets
    in the dictionary to create the ciphertext.
    """

    def encode(self, plaintext):
        cipher = ""
        for c in plaintext:
            cipher += self.dictionary[self.alphabets.index(c)]
        return cipher

    # We do the Reverse here to get the plaintext.
    def decode(self, cipher):
        plain = ""
        for c in cipher:
            plain += self.alphabets[self.dictionary.index(c)]
        return plain


psychosub = HCPyEncoder()
