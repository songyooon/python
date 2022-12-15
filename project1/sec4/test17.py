def fnc1():
    print("함수")

class test:
    x = y = 0

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def plus(self):
        return self.x + self.y

    def __del__(self):
        print("객체가 소멸됩니다")

fnc1()
obj1 = test(20, 40)
