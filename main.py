class Test():
    def __init__(self):
        self.public = "публичный атрибут"
        self._proyected = "защищенный атрибут"
        self.__private = "приватный атрибут"
    def get_private(self):
        return self.__private
    def set_private(self, value):
        self.__private = value

test = Test()
print(test.public)

print(test._proyected)

print(test.get_private())

test.set_private("получили значение приватного атрибута")

print(test.get_private())
