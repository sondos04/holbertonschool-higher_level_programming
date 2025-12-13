#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initialize a square with a private size attribute.
        Args:
            size (int): size of the square
        """
        self.__size = size
