import types

class Car:
    def __init__(self, xinghao, mali, yanse):
        self.xinghao = xinghao
        self.mali = mali
        self.yanse = yanse

    def update(self, m, y):
        self.mali = m
        self.yanse = y

class ECar(Car):
    def __init__(self, xinghao, mali, yanse, rongliang, licheng):
        super().__init__(xinghao, mali, yanse)
        self.rongliang = rongliang
        self.licheng = licheng

    def display(self):
        print(self.xinghao, self.mali, self.yanse, self.rongliang, self.licheng)

byd_s7 = Car("S7", 205, "红色")
byd_s7.zuowei = 7
byd_s7.fadongji = "2.0T"
byd_s7.gaodu = 1720

def s7_info(self):
    print(self.xinghao, self.mali, self.yanse, self.zuowei, self.fadongji, self.gaodu)

byd_s7.show = types.MethodType(s7_info, byd_s7)
byd_s7.show()

byd_tang = ECar("唐", 500, "白色", 80, 600)
byd_tang.display()