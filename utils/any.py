from utils.variable import Variable


class Any(Variable):
    __value = None

    def set(self, value):
        self.__value = value

    def get(self):
        return self.__value
