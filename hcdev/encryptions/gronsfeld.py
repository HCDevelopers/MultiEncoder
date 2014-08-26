# Coded by Ex094


class gronsfeld:
    __alpha = ""

    def __init__(self):
        self.__alpha = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""

    def encode(self, plain, key):
        plain = plain.upper()
        enc = ""

        for ch in plain:
            if (ch not in self.__alpha) or (ch == " "):
                enc += ch
            else:
                get = ((self.__alpha.index(ch) + int(key)) % 26)
                enc += self.__alpha[get]     
            
        return enc

    def decode(self, msg, key):
        msg = msg.upper()
        dec = ""

        for ch in msg:
            if (ch not in self.__alpha) or (ch == " "):
                dec += ch
            else:
                get = self.__alpha.index(ch) - int(key)
                dec += self.__alpha[get]

        return dec.lower()

    @staticmethod
    def description():

        return """
Coded By Ex094 in Python
  
In this cipher, 2 things are required for encoding
1) A Plain text
2) A key
  
Suppose the text is ATTACKBEFOREDAWN
And the key is      ORANGEORANGEORAN
  
In order to encode this, the formulae involved is:
              Char = (plaintext self.__alphabet + key self.__alphabet)
  
To encode T with R, We get: char = (20 + 18) = 38 which is K
  
So the new letter for T and R will be K
  
For decoding, Simply we preform the subtraction of the key index with that of the encrypted cipher.
"""
