from vigenere import vigenere

class gronsfeld(vigenere):

    global chars

    chars = '''ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'''

    def encode(self, text, key):
        text = text.upper()
        enc = ''
        key = self.adjust_key(key, len(text))

        for x in range(len(text)):
            ch = text[x]
            if ch.isalpha():
                a,b = ch, key[x]
                get = chars.index(a) + int(b)
                enc += chars[get]
            else: enc += ch
        return enc

    def decode(self, text, key):
        text.upper()    
        dec = ''
        key = self.adjust_key(key, len(text))

        for x in range(len(text)):
            ch = text[x]    
            if ch.isalpha():
                a,b = ch, key[x]
                get = chars.index(a) - int(b)   
                dec += chars[get]
            else: dec += ch
        return dec

    def description(self):

        return '''
This cipher is similar in working to the Vigenere Cipher but the difference
lies in the usage of the characters it uses. Vigenere Cipher used alphabets
where as in Gronsfeld Cipher we use a fixed numeric Key to encode the plain
text. The general forumla for encoding is:
                     
          Encode Char = (Key + Index of the each char in Plain text)

For example:

Plain text = 'Hackcommnity'
Cipher Key = '4'

Now what it does is simply take the index of the chars and add it to the cipher
key resulting in a new number which is the index of the new encoded char

So for encoding H with the key cipher 4, We first take the index of H which is
7. Apply the formula:

                 Encode Char = (4 + 7) = 11

11 is the index number of L so the new word for H will be L

Decoding is heck easy too, You just need to know the key that's all and then
instead of adding, subtract it from the char index and you'll get the actual
char.
''' 
