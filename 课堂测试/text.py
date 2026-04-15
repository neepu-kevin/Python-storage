stu = {"张琳": 58, "孙治平": 70, "徐小伟": 89, "徐丽萍": 69, "童万丽": 90, "钱志敏": 84, "赵虚余": 64}
print("原有字典：", stu)
stu["晋宇浩"] = "缺考" 
stu["张琳"] = 60
del stu["徐小伟"]
print("现有字典：", stu)
num = len(stu)
print("当前总人数：", num)
name = input("请输入同学姓名：")
if name in stu:
    print(name, "的成绩是：", stu[name])
else:
    print("没找到该同学")