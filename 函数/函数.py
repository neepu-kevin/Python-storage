def fun1(a,b):
    c=a+b if a<b else a-b
    def sum(a,c):
        return a+c
    d=sum(a,c)+b
    return d
z=fun1(100,200)
print(z)


def fun2(b,a=[]):
    a.append(b)
aa=[1,2,3,4,5]
fun2(6,aa)
print(aa)
c=[]
fun2(1,c)
print(c)
fun2(2,c)
print(c)

def demo(*para):
    avg=sum(para)/len(para)
    g=[i for i in para if i>avg]
    return (avg,)+tuple(g)
print(demo(1,2,3,4))

