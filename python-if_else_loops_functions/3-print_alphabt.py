#!/usr/bin/python3
for letter in list(
                range(97, 101)) + list(
                                    range(102, 113)) + list(
                                                        range(114, 123)):
    print("{}".format(chr(letter)), end="")
