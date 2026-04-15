s1 = input("请输入字符串s1: ")
s2 = input("请输入字符串s2: ")
alpha_count = 0
digit_count = 0
other_count = 0

for char in s1:
    if char.isalpha():
        alpha_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        other_count += 1
        
print(f"字母个数: {alpha_count}")
print(f"数字个数: {digit_count}")
print(f"符号个数: {other_count}")

new_s1 = ""
for char in s1:
    if not char.isalpha():
        new_s1 += char
print("删除字母后的s1:", new_s1)

flag = True
for char in s2:
    if char not in s1:
        flag = False
        break
        
if flag:
    print("yes")
else:
    print("No")