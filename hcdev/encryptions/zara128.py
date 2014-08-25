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
    ZARA-128 is a very simple example of String encryption where the user
    either generates a key or uses the default key len of 312. The Key given
    by the user is changed to integer by summation of ASCII value of each character
    in the key. If no Key is Supplied we use a default key of length 312.

    Example Run :-

    Encodings/encryptions (type "-i name" to get a description): zara
    Encode (e) or decode (d)? e
    Text: Hello

    Key for zara128 (type "-gen" to generate): -gen
    Generated key: oFlS3muQnX
    > zara128: 1000 1029 1036 1036 1039

    Result: 1000 1029 1036 1036 1039
            """


zara128 = HCPyEncoder()