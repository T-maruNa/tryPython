class Ant:
    __position = 0
    __vector = 0
    def __init__(self, position):
        self.__position = position

    def show(self):
        print(self.__position)
