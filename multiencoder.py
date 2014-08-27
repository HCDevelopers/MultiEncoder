#!/usr/bin/env python2.7
#
# UI for the MultiEncoder
#
# Author: Deque
# Co-author : Psycho_Coder
# URL: https://github.com/HCDevelopers/MultiEncoder
# For license information, see LICENSE

import hcdev

encrypters = hcdev.get_encryptors()
encoders = hcdev.get_encoders()
abbreviations = hcdev.get_abbrevs()

title = """
  __  __       _ _   _ ______                     _
 |  \/  |     | | | (_)  ____|                   | |
 | \  / |_   _| | |_ _| |__   _ __   ___ ___   __| | ___ _ __
 | |\/| | | | | | __| |  __| | '_ \ / __/ _ \ / _` |/ _ \ '__|
 | |  | | |_| | | |_| | |____| | | | (_| (_) | (_| |  __/ |
 |_|  |_|\__,_|_|\__|_|______|_| |_|\___\___/ \__,_|\___|_|


                Version 0.4 at Hackcommunity.com
            Authors: Ex094, noize, Psycho_Coder, Deque
"""


def get_algorithms():
    """Asks the user for the encoding and encryption algorithms that shall be
       used to encode or decode some text.
       Returns a list of the encoders and encrypters the user wants to apply.
    """
    userargs = []
    while True:
        userin = raw_input("Encodings/encryptions (type '-i algo-name' to get a description): ")
        userargs = userin.split()
        if len(userargs) >= 2 and userargs[0] == "-i":
            print_description(userargs[1])
        else:
            break
    return clean_list(userargs)


def print_description(algorithm):
    """Prints a description of the given algorithm
       The algorithm instance must have the attribute description, otherwise
       it prints that no description is available.
    """
    enc = None
    alglist = clean_list([algorithm])
    if len(alglist) == 1:
        alg = alglist[0]
        if alg in encoders:
            enc = encoders[alg]
        elif alg in encrypters:
            enc = encrypters[alg]
        if hasattr(enc, "description"):
            print("\n-----------------------------------------------------------------")
            print(enc.description())
            print("-----------------------------------------------------------------")
        else:
            print("No description available for " + alg)
        print("\n")


def print_algorithms():
    """Prints a list of all available encoders and encrypters, including a (-i)
       if a description is available
    """
    print("Available encodings:\n"),
    for algo in encoders.keys():
        print(algo),
        if hasattr(encoders[algo], "description"):
            print "(-i)",
    print("\n\nAvailable encryptions:\n"),
    for algo in encrypters.keys():
        print(algo),
        if hasattr(encrypters[algo], "description"):
            print("(-i)"),
    print("\n")


def en_de_code(is_decode, text, algorithms):
    """Takes a list of algorithms and performs encoding or decoding on the given
       text, depending on the is_decode argument.
       The encoding or decoding is performed in the order the algorithms are given.
       Intermediate results and end result are printed.
    """
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
        print(" > " + alg + " : " + text)
    print("\nResult: " + text)


def ask_for_key(algorithm, gen):
    """Asks the user to input or generate a key.

       Returns the key.
    """
    if hasattr(gen, "generate_key"):
        print "Key for", algorithm, "(type '-gen' to generate):",
        key = raw_input()
        if key == "-gen":
            key = gen.generate_key()
            print("\nGenerated key: %s \n" % key)
    else:
        print("Key for " + algorithm + " : "),
        key = raw_input()
    return key


def clean_list(dirtylist):
    """Takes a list of algorithm names as the user put them in.
       Turns abbreviations in to their non-abbreviated form.

       Returns a list of the corresponding encoders or encrypters in the same
       order as given in the input list.
       Returns an empty list if any of the input elements is invalid (not found).
    """
    cleanlist = []
    for element in dirtylist:

        if element in abbreviations:
            element = abbreviations[element]

        if element in encoders or element in encrypters:
            cleanlist.append(element)
        # one element couldn't be found, so return empty list
        else:
            print("\ncouldn't find " + element)
            return []
    return cleanlist


def ask_is_decode():
    """Ask user if he/she wants to decode or encode until appropriate answer
       was given
    """
    while True:
        user_input = raw_input("Encode (e) or decode (d)?")
        if user_input == "d" or user_input == "D":
            return True
        if user_input == "e" or user_input == "E":
            return False
        print("\nCan not recognize your input " + user_input)


def main():
    print title
    print_algorithms()
    algorithms = get_algorithms()
    while not algorithms:
        algorithms = get_algorithms()
    is_decode = ask_is_decode()
    text = raw_input("Text: ")
    en_de_code(is_decode, text, algorithms)

if __name__ == "__main__":
    main()
