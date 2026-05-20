class Car:
    def __init__(self, name, power, color):
        self.name = name
        self.power = power
        self.color = color

    def update(self, power, color):
        self.power = power
        self.color = color

class Ecar(Car):
    def __init__(self, name, power, color, battery, mile):
        Car.__init__(self, name, power, color)
        self.battery = battery
        self.mile = mile

    def display(self):
        print("型号：", self.name)
        print("马力：", self.power)
        print("颜色：", self.color)
        print("电池容量：", self.battery)
        print("最大行驶里程：", self.mile)


def show(self):
    print("型号：", self.name)
    print("马力：", self.power)
    print("颜色：", self.color)
    print("车座数：", self.seat)
    print("发动机型号：", self.engine)
    print("车身高度：", self.height)


c1 = Car("BYD-s7", 200, "黑色")

c1.seat = 5
c1.engine = "T100"
c1.height = 170

c1.show = show.__get__(c1)

c1.show()

c2 = Ecar("BYD唐", 300, "白色", 80, 600)

c2.display()