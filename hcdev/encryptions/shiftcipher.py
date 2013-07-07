class HCPyEncoder:
  
      def __init__(self):
        self.alphabets = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_+|:"<>-=[];,.?'
                        
      def encode(self, plaintext, shiftVal):
        length=len(self.alphabets)
        ciphertext=''
        shiftVal=int(shiftVal)
        for char in plaintext:
            n = self.alphabets.find(char)
            if n > -1:
                ciphertext += self.alphabets[(n + shiftVal) % length]
        return ciphertext
      
      def decode(self, ciphertext, shiftVal):
        plaintext=''
        shiftVal=int(shiftVal)
        length=len(self.alphabets)        
        for char in ciphertext:
            n = self.alphabets.find(char) + length
            if n >= length:
                plaintext += self.alphabets[(n - shiftVal) % length]
        return plaintext
shiftcipher = HCPyEncoder()
