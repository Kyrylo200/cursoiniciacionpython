import os
os.system('cls')

class Square:
    def __init__(self, width, height):
        self.__height = height
        self.__width = width

        @property
        def height(self):
            return self.__height
        
        @height.setter
        def height(self, num_value):
            self.__height = num_value
try:
    square = Square(2,2)
    square.height = 3
    print(square.isSquare())
    print(square.height)
except Exception as err:
    print(err)