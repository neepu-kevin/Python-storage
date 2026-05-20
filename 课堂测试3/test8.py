class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def print_info(self):
        print(self.name, self.age, self.city)

class Teacher(Person):
    def __init__(self, name, age, city, id, dept):
        super().__init__(name, age, city)
        self.id = id
        self.dept = dept

    def print_info(self):
        print(self.name, self.age, self.city, self.id, self.dept)

class University:
    def __init__(self, school, addr, teacher_list):
        self.school = school
        self.addr = addr
        self.teachers = []
        for i in range(5):
            t = Teacher(teacher_list[i][0], teacher_list[i][1], teacher_list[i][2], teacher_list[i][3], teacher_list[i][4])
            self.teachers.append(t)

    def display(self):
        print(self.school, self.addr)
        for t in self.teachers:
            t.print_info()

data = [
    ["张一", 30, "北京", "T01", "电气学院"],
    ["李二", 35, "上海", "T02", "能动学院"],
    ["王三", 40, "吉林", "T03", "计科学院"],
    ["赵四", 45, "长春", "T04", "自动化院"],
    ["孙五", 50, "大连", "T05", "经管学院"]
]

neepu = University("东北电力大学", "吉林市船营区", data)
neepu.display()