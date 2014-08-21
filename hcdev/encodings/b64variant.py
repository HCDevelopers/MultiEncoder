import base64

class B64VariantEncoder:

    def __init__(self, translation):
        base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
        self.alphabet = translation
        self.lookup = dict(zip(base, translation))
        self.revlookup = dict(zip(translation, base))

    def description(self):
        return """
        Crypo invented some fancy names for Base-64 encodings that simply use a different alphabet than the original Base-64 algorithm.
        We reverse engineered the site to find out the actual alphabets.

        This Base-64 variant has the alphabet: """ + self.alphabet + "\n\nDeque\n"

    def encode(self, text):
        global lookup
        b64 = base64.b64encode(text)
        result = "".join([self.lookup[x] for x in b64])
        return result

    def decode(self, code):
        global revlookup
        b64 = "".join([self.revlookup[x] for x in code])
        result = base64.b64decode(b64)
        return result

atom128 = B64VariantEncoder("3GHIJKLMNOPQRSTUb=cdefghijklmnopWXYZ/12+406789VaqrstuvwxyzABCDEF5")
megan35 = B64VariantEncoder("/128GhIoPQROSTeUbADfgHijKLM+n0pFWXY456xyzB7=39VaqrstJklmNuZvwcdEC")
zong22 = B64VariantEncoder("ZKj9n+yf0wDVX1s/5YbdxSo=ILaUpPBCHg8uvNO4klm6iJGhQ7eFrWczAMEq3RTt2")
hazz15 = B64VariantEncoder("HNO4klm6ij9n+J2hyf0gzA8uvwDEq3X1Q7ZKeFrWcVTts/MRGYbdxSo=ILaUpPBC5")
base = B64VariantEncoder("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=")
