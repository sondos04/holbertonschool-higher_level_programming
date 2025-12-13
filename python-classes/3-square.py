#!/usr/bin/python3
"""Defines a class Square with size validation and area method."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a square.
        Args:
            size (int): size of the square (default 0)
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size
