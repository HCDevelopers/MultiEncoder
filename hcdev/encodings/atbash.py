class HCPyEncoder:
    @staticmethod
    def description():
        print('''
    Description :-
    ---------------
    The Atbash cipher is a very specific case of a Monoalphabetic substitution cipher where the letters of the alphabet are reversed. In otherwords, all As are replaced with Zs, all Bs are replaced with Ys, and so on. I have added support for encrypting digits and special characters too to make it stronger

    Because reversing the alphabet twice will get you actual alphabet, you can encipher and decipher a message using the exact same algorithm.

    Example:
    Plaintext  : Ex094, You are a very Nice Guy!
    Ciphertext: [liZeB?~uo?8r4?8?n4rk?_064?-okX
    ''')

    def __init__(self):
        self.alphabets = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_+|:"<>-=[];,.?/`'

    def encode(self, plaintext):
        cipher = ""
        for i in plaintext:
            index = self.alphabets.index(i)
            cipher += self.alphabets[abs(len(self.alphabets) - index - 1) % len(self.alphabets)]
        return cipher

    def decode(self, ciphertext):
        return self.encode(ciphertext)


atbash = HCPyEncoder()
