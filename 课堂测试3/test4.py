def fun(day):
    if day == 7:
        return 1
    else:
        return (fun(day + 1) + 1) * 2

print(fun(1))