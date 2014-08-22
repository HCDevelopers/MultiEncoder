class leet:

    def back(l,w):
        return(replace(w,l))

    def encode(self,text):
        string = text.lower()
        string = string.replace("a","4").replace("b","8").replace("c","<").replace("e","3").replace("g","9").replace("h","|-|")
        string = string.replace("i","1").replace("k","|<").replace("l","|").replace("m","|\/|").replace("n","|\|").replace("o","0").replace("0","o")
        string = string.replace("q","0_").replace("s","5").replace("t","7").replace("u","|_|").replace("v","\/").replace("w","\/\/").replace("x","><").replace("z","2")
        return(string)

    def decode(self,text):
        string = text.lower()
        string = string.replace("4","a").replace("8","b").replace("<","c").replace("3","e").replace("9","g").replace("|-|","h")
        string = string.replace("1","i").replace("|<","k").replace("|\/|","m").replace("|\|","n").replace("|","l").replace("0","o").replace("o","0")
        string = string.replace("0_","q").replace("5","s").replace("7","t").replace("|_|","u").replace("\/\/","w").replace("\/","v").replace("><","x").replace("2","z")
        return(string)

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
