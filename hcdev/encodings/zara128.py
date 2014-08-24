#!/usr/bin/env python2.7
#
# ZARA-128 Encoding Algorithm implementation.
#
# Author: Animesh Shaw


class HCPyEncoder:
    __PAD = 0

    def __init__(self):
        self.__PAD = 312

    def encode(self, plaintext):

        enctext = []
        for c in plaintext:
            enctext.append(str(ord(c) + self.__PAD))

        return " ".join(enctext)

    def decode(self, ciphertext):

        dectext = []
        for c in ciphertext.split():
            dectext.append(chr(int(c) - self.__PAD))

        return "".join(dectext)

    @staticmethod
    def description():

        return '''
    Description :-
    ---------------
    ZARA-128 is a very simple example of String encoding where each character in the string is converted
    to ASCII value and then 312 is add to it along with a space to distinguish between the characters.

    Example:
    Plaintext  : Psycho_Coder
    Ciphertext: 392 427 433 411 416 423 407 379 423 412 413 426
            '''

zara128 = HCPyEncoder()