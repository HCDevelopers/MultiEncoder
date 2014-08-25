#!/usr/bin/env python2.7
# coding=utf-8
#
# ZARA-128 Encoding Algorithm implementation.
#
# Author: Animesh Shaw


from random import Random
from string import ascii_letters, digits


class HCPyEncoder:
    def __init__(self):
        self.__DEFAULT_KEY_VAL = 312
        self.__PAD = 0
        self.__key_val = lambda key: sum([ord(c) for c in key]) \
            if key.strip() != "" else self.__DEFAULT_KEY_VAL

    def encode(self, plaintext, key=""):
        self.__PAD = self.__key_val(key)
        return " ".join(str(ord(c) + self.__PAD) for c in plaintext)

    def decode(self, ciphertext, key=""):
        self.__PAD = self.__key_val(key)
        return "".join(chr(int(c) - self.__PAD) for c in ciphertext.split())

    @staticmethod
    def generate_key(keylen=10):
        pad = ascii_letters + digits
        return ''.join(Random().sample(pad, keylen))

    @staticmethod
    def description():
        return """
    Description :-
    ---------------
    ZARA-128 is a very simple example of String encoding where each character in the string is converted
    to ASCII value and then 312 is add to it along with a space to distinguish between the characters.

    Example:
    Plaintext  : Psycho_Coder
    Ciphertext: 392 427 433 411 416 423 407 379 423 412 413 426
            """


zara128 = HCPyEncoder()