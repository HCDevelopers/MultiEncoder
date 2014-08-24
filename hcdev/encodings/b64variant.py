# Authors: Deque, Ex094
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

        This Base-64 variant has the alphabet: """ + self.alphabet + "\n\nDeque, Ex094\n"

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

gila7 = B64VariantEncoder("7ZSTJK+W=cVtBCasyf0gzA8uvwDEq3XH/1RMNOILPQU4klm65YbdeFrx2hij9nopG")
tripo5 = B64VariantEncoder("ghijopE+G78lmnIJQRXY=abcS/UVWdefABCs456tDqruvNOPwx2KLyz01M3Hk9ZFT")
feron74 = B64VariantEncoder("75XYTabcS/UVWdefADqr6RuvN8PBCsQtwx2KLyz+OM3Hk9ghi01ZFlmnjopE=GIJ4")
tigo3 = B64VariantEncoder("FrsxyzA8VtuvwDEqWZ/1+4klm67=cBCa5Ybdef0g2hij9nopMNO3GHIRSTJKLPQUX")
esab46 = B64VariantEncoder("ABCDqrs456tuvNOPwxyz012KLM3789=+QRSTUVWXYZabcdefghijklmnopEFGHIJ/")
atom128 = B64VariantEncoder("3GHIJKLMNOPQRSTUb=cdefghijklmnopWXYZ/12+406789VaqrstuvwxyzABCDEF5")
megan35 = B64VariantEncoder("/128GhIoPQROSTeUbADfgHijKLM+n0pFWXY456xyzB7=39VaqrstJklmNuZvwcdEC")
zong22 = B64VariantEncoder("ZKj9n+yf0wDVX1s/5YbdxSo=ILaUpPBCHg8uvNO4klm6iJGhQ7eFrWczAMEq3RTt2")
hazz15 = B64VariantEncoder("HNO4klm6ij9n+J2hyf0gzA8uvwDEq3X1Q7ZKeFrWcVTts/MRGYbdxSo=ILaUpPBC5")
base = B64VariantEncoder("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=")
