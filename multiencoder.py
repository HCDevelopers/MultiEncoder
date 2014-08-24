#!/usr/bin/env python2.7
#
# UI for the multi encoder
#
# Author: Deque
# URL: https://github.com/HCDevelopers/MultiEncoder
# For license information, see LICENSE


# Encryptions
from hcdev.encryptions.vigenere import vigenere
from hcdev.encryptions.xor import xor
from hcdev.encryptions.shiftcipher import shiftcipher
from hcdev.encryptions.gronsfeld import gronsfeld

# Encodings
from hcdev.encodings.atbash import atbash
from hcdev.encodings.psychosubcipher import psychosub
from hcdev.encodings.hex import hex
from hcdev.encodings.leet import leet
from hcdev.encodings.reverse import reverse
from hcdev.encodings.binary import binary
from hcdev.encodings.morse import morse
from hcdev.encodings.b64variant import *
from hcdev.encodings.rot import *

encrypters = { 'gronsfeld': gronsfeld(), 'shiftcipher': shiftcipher, 'vigenere': vigenere(), 'xor': xor }

encoders = { 'atbash': atbash, 'psychosubcipher': psychosub, 'hex': hex, 'leet': leet(),
             'reverse': reverse, 'rot13': rot13, 'binary': binary,
             'morse': morse, 'megan35': megan35, 'atom128': atom128, 'zong22': zong22, 'gila7': gila7,
             'tripo5': tripo5, 'feron74': feron74, 'tigo3': tigo3, 'esab46': esab46,
             'base64': base, 'hazz15': hazz15, 'rot18': rot18, 'rot47': rot47, 'rot5': rot5 }

abbrevs = { 'grons': 'gronsfeld', 'shift': 'shiftcipher', 'psycho': 'psychosubcipher',
            'psy': 'psychosubcipher', 'vig': 'vigenere', 'rev': 'reverse',
            'rot': 'rot13', 'bin': 'binary', 'megan': 'megan35', 'atom': 'atom128',
            'zong': 'zong22', 'base': 'base64', 'hazz': 'hazz15', 'gila': 'gila7', 'tripo': 'tripo5',
            'feron': 'feron74', 'tigo': 'tigo3', 'esab': 'esab46'}

title = """
  __  __       _ _   _ ______                     _
 |  \/  |     | | | (_)  ____|                   | |
 | \  / |_   _| | |_ _| |__   _ __   ___ ___   __| | ___ _ __
 | |\/| | | | | | __| |  __| | "_ \ / __/ _ \ / _` |/ _ \ "__|
 | |  | | |_| | | |_| | |____| | | | (_| (_) | (_| |  __/ |
 |_|  |_|\__,_|_|\__|_|______|_| |_|\___\___/ \__,_|\___|_|


                Version 0.4 at Hackcommunity.com
            Authors: Ex094, noize, Psycho_Coder, Deque
"""


def get_algorithms():

    userargs = []
    while True:
        userin = raw_input('Encodings/encryptions (type "-i name" to get a description): ')
        userargs = userin.split()
        if len(userargs) >= 2 and userargs[0] == "-i":
            print_description(userargs[1])
        else:
            break
    return clean_list(userargs)


def print_description(algorithm):

    enc = None
    list = clean_list([algorithm])
    if len(list) == 1:
        alg = list[0]
        if alg in encoders:
            enc = encoders[alg]
        elif alg in encrypters:
            enc = encrypters[alg]
        if hasattr(enc, "description"):
            print
            print "-----------------------------------------------------------"
            print enc.description()
            print "-----------------------------------------------------------"
        else:
            print "No description available for", alg
        print("\n")


def print_algorithms():
    print "Available encodings:\n",
    for algo in encoders.keys():
        print algo,
        if hasattr(encoders[algo], "description"):
            print "(-i)",
    print "\n\nAvailable encryptions:\n",
    for algo in encrypters.keys():
        print algo,
        if hasattr(encrypters[algo], "description"):
            print "(-i)",
    print("\n")


def en_de_code(is_decode, text, algorithms):
    print

    for alg in algorithms:
        if alg in encoders:
            encoder = encoders[alg]
            function = encoder.decode if is_decode else encoder.encode
            text = function(text)
        if alg in encrypters:
            encrypter = encrypters[alg]
            key = ask_for_key(alg, encrypter)
            function = encrypter.decode if is_decode else encrypter.encode
            text = function(text, key)
        print '>', alg + ':', text
    print
    print "Result:", text


def ask_for_key(algorithm, gen):
    if hasattr(gen, "generate_key"):
        print "Key for", algorithm, '(type "-gen" to generate):',
        key = raw_input()
        if key == "-gen":
            key = gen.generate_key()
            print "Generated key:", key
    else:
        print "Key for", algorithm + ':',
        key = raw_input()
    return key


def clean_list(dirtylist):
    cleanlist = []
    for element in dirtylist:

        if element in abbrevs:
            element = abbrevs[element]

        if element in encoders or element in encrypters:
            cleanlist.append(element)
        else:
            print
            print "Couldn't find", element
    return cleanlist


def main():
    print title
    print_algorithms()
    algorithms = get_algorithms()
    is_decode = True if raw_input("Encode (e) or decode (d)? ") == "d" else False
    text = raw_input("Text: ")
    en_de_code(is_decode, text, algorithms)

if __name__ == "__main__":
    main()
