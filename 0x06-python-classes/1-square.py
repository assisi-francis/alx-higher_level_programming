#!/usr/bin/python3
"""Defines a square """


class Square:
    """Represents a square"""

    def __init__(self, size):
        """Initializing this square class
        Args: size - represnets the size of the square defined
        """

        self.__size = size


if __name__ == '__main__':
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
