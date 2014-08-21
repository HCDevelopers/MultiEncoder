#!/usr/bin/env python 2.7
#
# Author: Deque
# UI for the multi encoder
#

import sys
# encryptions
from hcdev.encryptions.vigenere import vigenere
from hcdev.encryptions.xor import xor
from hcdev.encryptions.shiftcipher import shiftcipher
from hcdev.encryptions.gronsfeld import gronsfeld
# encodings
from hcdev.encodings.atbash import atbash
from hcdev.encodings.psychosubcipher import psychosub
from hcdev.encodings.hex import hex
from hcdev.encodings.leet import leet
from hcdev.encodings.reverse import reverse
from hcdev.encodings.binary import binary
from hcdev.encodings.morse import morse
from hcdev.encodings.b64variant import *
from hcdev.encodings.rot import *

encrypters = {'gronsfeld' : gronsfeld(), 'shiftcipher': shiftcipher, 'vigenere' : vigenere(), 'xor' : xor}

encoders = {'atbash' : atbash, 'psychosubcipher' : psychosub, 'hex' : hex,  'leet' : leet(),
    'reverse' : reverse(), 'rot13' : rot13, 'binary' : binary,
    'morse' : morse, 'megan35': megan35, 'atom128' : atom128, 'zong22' : zong22,
    'base64' : base, 'hazz15' : hazz15, 'rot18' : rot18, 'rot47' : rot47, 'rot5' : rot5 }

abbrevs = {'grons' : 'gronsfeld', 'shift' : 'shiftcipher', 'psycho' : 'psychosubcipher',
    'psy' : 'psychosubcipher', 'vig' : 'vigenere', 'rev' : 'reverse',
    'rot' : 'rot13', 'bin' : 'binary', 'megan' : 'megan35', 'atom' : 'atom128',
    'zong' : 'zong22', 'base' : 'base64', 'hazz' : 'hazz15'}

title = '''
.88b  d88. db    db db      d888888b d888888b d88888b d8b   db  .o88b.  .d88b.  d8888b. d88888b d8888b.
88'YbdP`88 88    88 88      `~~88~~'   `88'   88'     888o  88 d8P  Y8 .8P  Y8. 88  `8D 88'     88  `8D
88  88  88 88    88 88         88       88    88ooooo 88V8o 88 8P      88    88 88   88 88ooooo 88oobY'
88  88  88 88    88 88         88       88    88~~~~~ 88 V8o88 8b      88    88 88   88 88~~~~~ 88`8b
88  88  88 88b  d88 88booo.    88      .88.   88.     88  V888 Y8b  d8 `8b  d8' 88  .8D 88.     88 `88.
YP  YP  YP ~Y8888P' Y88888P    YP    Y888888P Y88888P VP   V8P  `Y88P'  `Y88P'  Y8888D' Y88888P 88   YD

                        Version 0.3 at Hackcommunity.com
                    Authors: Ex094, noize, Psycho_Coder, Deque
'''

def main():

    print title
    print_algorithms()
    algorithms = get_algorithms()
    is_decode = True if raw_input("Encode (e) or decode (d)? ") == "d" else False
    text = raw_input("Text: ")
    en_de_code(is_decode, text, algorithms)

def get_algorithms():
    while(True):
        userin = raw_input('Encodings/encryptions (type "-i name" to get a description): ')
        userargs = userin.split()
        if len(userargs) >= 2 and userargs[0] == "-i":
            print_description(userargs[1])
        else: break
    return clean_list(userargs)

def print_description(algorithm):
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
        else: print "No description available for", alg
        print

def print_algorithms():
    print "Available encodings:",
    for algo in encoders.keys():
        print algo,
        if hasattr(encoders[algo], "description"): print "(-i)",
    print
    print "Available encryptions:",
    for algo in encrypters.keys():
        print algo,
        if hasattr(encrypters[algo], "description"): print "(-i)",
    print
    print

def en_de_code(is_decode, text, algorithms):
    print
  #  try:

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
#    except:
 #       print "Unexpected error:", sys.exc_info()[0]

def ask_for_key(algorithm, gen):
    if hasattr(gen, "generateKey"):
        print "Key for", algorithm, '(type "-gen" to generate):',
        key = raw_input()
        if key == "-gen":
            key = gen.generateKey()
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

main()
