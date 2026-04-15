data = [
    ["同学三", 85, 90, 78, 88],
    ["同学四", 70, 65, 80, 72],
    ["同学五", 92, 88, 95, 90],
    ["同学六", 60, 55, 70, 68],
    ["同学七", 80, 82, 85, 79]
]
stats = []
for i in range(len(data)):
    name = data[i][0]
    scores = data[i][1:]
    total = sum(scores)
    avg = total / len(scores)
    stats.append([name, total, avg])

name_input = input("请输入学生姓名: ")
found = False

for i in range(len(data)):
    if data[i][0] == name_input:
        print("姓名:", data[i][0])
        print("成绩:", data[i][1:])
        print("平均成绩:", stats[i][2])
        found = True
        break

if not found:
    print("查无此人！")

print("\n统计结果：")
for row in stats:
    print(row)