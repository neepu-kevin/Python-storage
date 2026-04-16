import types  # 建议导入放在代码最开头，规范写法

class Car:
    price = 100000
    def __init__(self, c):
        self.color = c

car1 = Car("red")
car2 = Car("blue")
print(car1.color, Car.price)  # red 100000

Car.price = 120000
Car.name = "QQ"
car1.color = "yellow"
print(car2.color, Car.price, Car.name)  # blue 120000 QQ
print(car1.color, Car.price, Car.name)  # yellow 120000 QQ

# 定义方法
def setSpeed(self, s):
    self.speed = s

# ✅ 修正：绑定到实例 car1（第二个参数是实例）
car1.setSpeed = types.MethodType(setSpeed, car1)
car1.setSpeed(50)

print(car1.speed)  # 50（正确输出）
# print(car2.speed)  # 直接删掉/注释：car2没有speed属性，会报错