#Author: Ex094

class ex094morse:
    morse_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    morse_encode = ['.-', '-...', '-.-.', '-.', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.','...' ,'-' ,'..-' ,'...-' ,'.--' ,'-..-' ,'-.--' ,'--..' ,'-----' ,'.----','..---','...--','....-','.....','-....','--...','---..','----.']
    def encode(self, text):
        store = ''
        for item in text.upper():
            store += self.morse_encode[self.morse_alpha.find(item)] + ' '
        return store

    def decode(self, text):
        store = ''
        for item in text.split():
            store += self.morse_alpha[self.morse_encode.index(item)]
        return store

morse = ex094morse()
