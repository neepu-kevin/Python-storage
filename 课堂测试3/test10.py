class A:
    def __init__(self, a=0):
        self.a = a

    def display(self):
        print(self.a)

class B(A):
    def __init__(self, b=0, a_for_b=0):
        super().__init__(a_for_b)
        self.b = b

class C(A):
    def __init__(self, c=0, a_for_c=0):
        super().__init__(a_for_c)
        self.c = c

class D(B, C):
    def __init__(self, b_val, a_b, c_val, a_c, d_val):
        super().__init__(b_val, a_b)
        C.__init__(self, c_val, a_c)
        self.d = d_val

d1 = D(1, 2, 3, 4, 5)

print(d1.a)
d1.display()