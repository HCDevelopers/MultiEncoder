from hcdev.exception import EncodeInputError

from hcdev.encryptions.zara128 import zara128
from hcdev.encryptions.vigenere import vigenere
from hcdev.encryptions.xor import xor
from hcdev.encryptions.shiftcipher import shiftcipher
from hcdev.encryptions.gronsfeld import gronsfeld

from hcdev.encodings.atbash import atbash
from hcdev.encodings.psychosubcipher import psychosub
from hcdev.encodings.hex import hex
from hcdev.encodings.leet import leet
from hcdev.encodings.reverse import reverse
from hcdev.encodings.binary import binary
from hcdev.encodings.morse import morse
from hcdev.encodings.b64variant import *
from hcdev.encodings.rot import *


encrypters = {
    "gronsfeld": gronsfeld,
    "shiftcipher": shiftcipher,
    "vigenere": vigenere(),
    "xor": xor,
    "zara128": zara128
}

encoders = {
    "atbash": atbash,
    "psychosubcipher": psychosub,
    "hex": hex,
    "leet": leet,
    "reverse": reverse,
    "rot13": rot13,
    "binary": binary,
    "morse": morse,
    "megan35": megan35,
    "atom128": atom128,
    "zong22": zong22,
    "gila7": gila7,
    "tripo5": tripo5,
    "feron74": feron74,
    "tigo3": tigo3,
    "esab46": esab46,
    "base64": base,
    "hazz15": hazz15,
    "rot18": rot18,
    "rot47": rot47,
    "rot5": rot5
}

abbreviations = {
    "grons": "gronsfeld",
    "shift": "shiftcipher",
    "psycho": "psychosubcipher",
    "psy": "psychosubcipher",
    "vig": "vigenere",
    "rev": "reverse",
    "rot": "rot13",
    "bin": "binary",
    "megan": "megan35",
    "atom": "atom128",
    "zara": "zara128",
    "zong": "zong22",
    "base": "base64",
    "hazz": "hazz15",
    "gila": "gila7",
    "tripo": "tripo5",
    "feron": "feron74",
    "tigo": "tigo3",
    "esab": "esab46"
}


def get_encryptors():
    return encrypters


def get_encoders():
    return encoders


def get_abbrevs():
    return abbreviations
