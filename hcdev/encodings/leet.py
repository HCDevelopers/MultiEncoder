class leet:
    def encode(self,string):
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','|','<','>','G']
        leet = ['4','8','<','>','3','f','9','h','1','j','k','|','m','n','0','p','q','r','5','7','v','v','w','x','y','2','o','i','z','e','a','s','G','t','b','g','l','c','d','6']

        encoded = ""

        for c in string:
            for i in range(0,len(alphabet)):
                if c == alphabet[i]:
                    encoded = encoded + c.replace(alphabet[i],leet[i])
                    continue

        return(encoded)

    def decode(self,string):
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','|','<','>','G']
        leet = ['4','8','<','>','3','f','9','h','1','j','k','|','m','n','0','p','q','r','5','7','v','v','w','x','y','2','o','i','z','e','a','s','G','t','b','g','l','c','d','6']
        
        decoded = ""

        for c in string:
            for i in range(0,len(alphabet)):
                if c == leet[i]:
                    decoded = decoded + c.replace(leet[i],alphabet[i])
                    continue

        return(decoded)

    def description(self):
        return '''
            The leet encoding algorithm is based upon the 1337 speak well-known in the hackers' underground.
            Characters are replaced with numbers or groups of different characters resembling them.

            Example input string:

             Hello from LEET speak!

            Encoded string:

             |-|3||0 fr0|\/| |337 5p34|<!

            To avoid messing up cases and to allow this algorithm to be used combined with other case-sensitive encodings, only lowercase characters, numbers and the |, <, > and G characters are translated (G is the only uppercase character that is translated).
        '''
