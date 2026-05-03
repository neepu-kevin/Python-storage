scores = {"Zhang San": 45, "Li Si": 78, "Wang Wu": 40, "Zhou Liu": 96, "Zhao Qi": 65, "Sun Ba": 90, "Zheng Jiu": 78, "Wu Shi": 99, "Dong Shiyi": 60}

def solve(d):
    v = list(d.values())
    hi = max(v)
    lo = min(v)
    avg = sum(v) / len(v)
    names = []
    for k in d:
        if d[k] == hi:
            names.append(k)    
    return hi, lo, avg, names

high, low, avg, top_stu = solve(scores)
print(high, low, avg, top_stu)