class leet:
    def back(l,w):
        return(replace(w,l))
    def encode(self,text):
        string = text.lower()
        string = string.replace("a","4").replace("b","8").replace("c","<").replace("e","3").replace("g","9").replace("h","|-|")
        string = string.replace("i","1").replace("k","|<").replace("l","|").replace("m","|\/|").replace("n","|\|").replace("o","0")
        string = string.replace("q","0_").replace("s","5").replace("t","7").replace("u","|_|").replace("v","\/").replace("w","\/\/").replace("x","><").replace("z","2")
        return(string)
    def decode(self,text):
        string = text.lower()
        string = string.replace("4","a").replace("8","b").replace("<","c").replace("3","e").replace("9","g").replace("|-|","h")
        string = string.replace("1","i").replace("|<","k").replace("|\/|","m").replace("|\|","n").replace("|","l").replace("0","o")
        string = string.replace("0_","q").replace("5","s").replace("7","t").replace("|_|","u").replace("\/\/","w").replace("\/","v").replace("><","x").replace("2","z")
        return(string)