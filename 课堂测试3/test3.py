def fun():
    data = [12.04,11.15,13.47,13.58,12.04,12.04,11.15,12.58,11.15]
    print("数据个数：")
    print(len(data))
    print("12.04出现次数：")
    print(data.count(12.04))
    m = min(data)
    print("最小值：")
    print(m)
    data.remove(m)
    print("删除后的列表：")
    print(data)

fun()