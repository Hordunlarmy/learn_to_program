"""
a program to get the area of a square
"""


class Square:

    def __init__(self, height=0, width=0):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__width = value

    def getArea(self):
        if self.height.isdigit() and self.width.isdigit():
            return (int(self.height) * int(self.width))
        else:
            print("pls, enter a digit")


def main():
    a_square = Square()

    s_height = input("Enter the height of your square: ")
    s_width = input("Enter the width of your square: ")

    a_square.height = s_height
    a_square.width = s_width

    print(a_square.getArea())


main()
