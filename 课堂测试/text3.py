import random
arr = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]
print("排序前：")
for row in arr:
    print(row)
arr.sort(key=lambda x: x[2])
print("排序后：")
for row in arr:
    print(row)