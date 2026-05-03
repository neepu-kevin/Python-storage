def master_func(a, b, c=10, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

# 调用：
master_func(1, 2, 3, 4, 5, 6, name="Tom", age=18)