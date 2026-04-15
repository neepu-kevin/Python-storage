import random
import string

chars = string.ascii_letters + string.digits + string.punctuation
s = ''.join(random.choice(chars) for _ in range(1000))
print("字符串s:", s)
counts = {}
for char in s:
    counts[char] = counts.get(char, 0) + 1
sorted_counts = sorted(counts.items(), key=lambda x: x[1])
for char, count in sorted_counts:
    print(f"'{char}': {count}")