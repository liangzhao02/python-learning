# 员工类
class Staff(object):

    def work(self):
        print('在工作...')

# it程序员
class Itboy(Staff):

    def work(self):
        print('在敲代码...')

# UI设计师
class Uiboy(Staff):

    def work(self):
        print('在画图...')

# 老板类
class Boss(object):

    def arrange_work(self,x):
        x.work()


i = Itboy()
u = Uiboy()
b = Boss()
b.arrange_work(i)
b.arrange_work(u)