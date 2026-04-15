for i in range(100,301):
    for j in range(2, i):
        if i % j == 0:
            break
    if j == i-1:
        print(i, end=' ')