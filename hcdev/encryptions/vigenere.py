# Coded by Ex094


class vigenere:
    __alpha = ""

    def __init__(self):
        self.__alpha = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""

    @staticmethod
    def adjust_key(key, l):
        okey = key
        while len(key) <= l:
            key += okey
        return key

    def encode(self, plain, key):
        plain = plain.upper()
        key_plain = plain.replace(" ", "")
        key = self.adjust_key(key, len(key_plain))
        enc = ""

        for x in range(len(plain)):
            ch = str(plain[x])

            if (ch not in self.__alpha) or (ch == " "):
                enc += ch
            else:
                a, b = ch, key[x]
                get = ((self.__alpha.index(a) + self.__alpha.index(b)) % 26)
                enc += self.__alpha[get]     
            
        return enc

    def decode(self, msg, key):
        msg = msg.upper()
        key = key.upper()
        dec = ""
        key = self.adjust_key(key, len(msg))

        for x in range(len(msg)):
            ch = str(msg[x])
            if ch.isalpha():
                a, b = ch, key[x]
                get = ((self.__alpha.index(a) - self.__alpha.index(b)) % 26)
                dec += self.__alpha[get]

            else:
                dec += ch
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
  
For decoding, Simply we preform the subtraction of the key index with that of the encrypted cipher."""