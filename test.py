import random

arr = [[random.randint(1,100) for i in range(5)] for j in range(5)]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=' ')
    print()

arr.sort(key=lambda x: x[1])
print('Sorted by second element:')
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=' ')
    print()