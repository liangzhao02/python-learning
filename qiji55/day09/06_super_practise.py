# class Person(object):
#
#     def __init__(self, name, sex, age, country):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.country = country
#
#     def eat(self):
#         print('%s要吃饭' % self.name)
#
#     def sleep(self):
#         print('%s要睡觉' % self.name)
#
#     def work(self):
#         print('%s要工作' % self.name)
#
#     # def __str__(self):
#     #     attrs = vars(self) #返回字典
#     #     attr_list = [ "%s: %s" % (key, value) for key, value in attrs.items()]
#     #     return '\n'.join(attr_list)
#     def __str__(self):
#         return '姓名为%s,性别为%s,年龄为%s,国籍为%s' % (self.name,self.sex,self.age,self.country)

# p = Person('张三','男',18,'China')
# p.eat()
# p.sleep()
# p.work()
# print(p.name)
# print(p.sex)
# print(p.age)
# print(p.country)
# print(p)

class Person(object):

    def __init__(self, name, sex, age, country):
        self.name = name
        self.sex = sex
        self.age = age
        self.country = country

    def eat(self):
        print('%s要吃饭' % self.name)

    def sleep(self):
        print('%s要睡觉' % self.name)

    def work(self):
        print('%s要工作' % self.name)

class Student(Person):
    def __init__(self, name, sex, age, country, school_name, no):
        super(Student ,self).__init__(name, sex, age, country)
        self.school_name = school_name
        self.no = no

    def eat(self):
        print('%s要吃饭' % self.name)

    def sleep(self):
        print('%s要睡觉' % self.name)

    def work(self):
        print('%s要学习' % self.name)

    def __str__(self):
        attrs = vars(self) # 返回字典
        attr_list = [ "%s: %s" % (key, value) for key, value in attrs.items()]
        return '\n'.join(attr_list)
    # def __str__(self):
    #     res = super(Student ,self).__str__()
    #     return '%s,校名%s,学号为%s' % (res,self.school_name,self.no)
    # def __str__(self):
    #     return '姓名为%s,性别为%s,年龄为%s,国籍为%s,学校是%s,学号是%s' % (self.name, self.sex, self.age, self.country,self.school_name,self.no)

# # p = Student('张三','男',18,'China','qijiketang','001')
student = Student("张三", "男", 18, "中国", "奇技课堂", "001")
student.eat()
student.sleep()
student.work()
print(student)




















