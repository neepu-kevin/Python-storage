stu={"张琳":58,"孙治平":70,"徐小伟":89,"徐丽萍":69,"童万丽":90,"钱志敏":84,"赵虚余":64}
print("原有字典：")
print(stu)
stu["晋宇浩"]="缺考" # type: ignore 
stu["张琳"]=60
del stu["徐小伟"]
print("现有字典:")
print(stu)
print("现有人数:")
print(len(stu))

name=input("输入同学的姓名：")
if(name in stu):
    print(stu[name])
else:
    print("没找到该同学")