class Student:
    num = 0
    t1_sum = 0
    w1_sum = 0
    t2_sum = 0
    exam_sum = 0
    score_sum = 0
    pass_num = 0

    def __init__(self, t1, w1, t2, exam):
        self.t1 = t1
        self.w1 = w1
        self.t2 = t2
        self.exam = exam
        self.score = 0
        Student.num += 1
        Student.t1_sum += t1
        Student.w1_sum += w1
        Student.t2_sum += t2
        Student.exam_sum += exam

    def change(self, t1, w1, t2, exam):
        self.t1 = t1
        self.w1 = w1
        self.t2 = t2
        self.exam = exam

    def count(self):
        self.score = 0.1 * self.t1 + 0.1 * self.w1 + 0.1 * self.t2 + 0.7 * self.exam
        Student.score_sum += self.score
        if self.score >= 60:
            Student.pass_num += 1

    @classmethod
    def avg(cls):
        print("课堂测验1平均分：", cls.t1_sum / cls.num)
        print("作业1平均分：", cls.w1_sum / cls.num)
        print("课堂测验2平均分：", cls.t2_sum / cls.num)
        print("期末考试平均分：", cls.exam_sum / cls.num)
        print("课程成绩平均分：", cls.score_sum / cls.num)

    @staticmethod
    def show():
        print("总人数：", Student.num)
        print("及格人数：", Student.pass_num)
        print("及格率：", Student.pass_num / Student.num)


s1 = Student(80, 90, 85, 88)
s2 = Student(70, 75, 80, 78)
s3 = Student(60, 65, 70, 72)
s4 = Student(50, 55, 58, 60)
s5 = Student(90, 92, 95, 96)

s1.count()
s2.count()
s3.count()
s4.count()
s5.count()

Student.show()
Student.avg()