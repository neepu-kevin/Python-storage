class Complex:
    def __init__(self, shi, xu):
        self.shi = shi
        self.xu = xu

    def add(self, other):
        new_shi = self.shi + other.shi
        new_xu = self.xu + other.xu
        return Complex(new_shi, new_xu)

    def sub(self, other):
        new_shi = self.shi - other.shi
        new_xu = self.xu - other.xu
        return Complex(new_shi, new_xu)

    def mul(self, other):
        new_shi = self.shi * other.shi - self.xu * other.xu
        new_xu = self.shi * other.xu + self.xu * other.shi
        return Complex(new_shi, new_xu)

    def div(self, other):
        m = other.shi**2 + other.xu**2
        new_shi = (self.shi * other.shi + self.xu * other.xu) / m
        new_xu = (self.xu * other.shi - self.shi * other.xu) / m
        return Complex(new_shi, new_xu)

    def show(self):
        print(str(self.shi) + " + " + str(self.xu) + "i")

c1 = Complex(4, 2)
c2 = Complex(2, 1)
c3 = Complex(1, 1)

res_add = c1.add(c2)
res_sub = c1.sub(c2)
res_mul = c1.mul(c3)
res_div = c1.div(c2)

res_add.show()
res_sub.show()
res_mul.show()
res_div.show()