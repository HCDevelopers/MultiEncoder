#Coded by Ex094

class vigenere:

    global alpha
    
    alpha = '''ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'''

    def adjust_key(self, key, l):
        okey = key
        while len(key) < l:
            key += okey
        return key

    def encode(self, plain, key):
        plain = plain.upper()
        key = key.upper()
        enc = ''
        key = self.adjust_key(key, len(plain))    

        for x in range(len(plain)):
            ch = plain[x]
            if ch.isalpha():
                a,b = ch, key[x]
                get = alpha.index(a) + alpha.index(b)
                enc += alpha[get]
            else: enc += ch
        return enc

    def decode(self, msg, key):
        msg = msg.upper()
        key = key.upper()
        dec = ''
        key = self.adjust_key(key, len(msg))

        for x in range(len(msg)):
            ch = msg[x]
            if ch.isalpha():
                a,b = ch, key[x]
                get = alpha.index(a) - alpha.index(b)
                dec += alpha[get]
            else: dec += ch
        return dec

    def description(self):

        return '''
Coded By Ex094 in Python

In this cipher, 2 things are required for encoding
1) A Plain text
2) A key

Suppose the text is ATTACKBEFOREDAWN
And the key is      ORANGEORANGEORAN

In order to encode this, the formulae involved is:
              Char = (plaintext alphabet + key alphabet)

To encode T with R, We get: char = (20 + 18) = 38 which is K

So the new letter for T and R will be K

For decoding, Simply we preform the subtraction of the key index with that of the encrypted cipher.'''
