import string
import random

s = string.ascii_letters + string.digits + string.punctuation
res = "".join(random.choices(s, k=1000))
d = {}
for i in res:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(res)
print(d)