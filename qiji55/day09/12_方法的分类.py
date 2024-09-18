# 实例方法 小括号为self的方法,需要有对象名进行调用
# 类方法 小括号中为cls的方法,需要在定义方法的上一行@classmethod
# 静态方法 小括号中什么都没有,需要在定义方法上一行添加@staticmeyhod
class Person(object):

    # 实例方法
    def sing(self):
        print('我是实例方法....')

    # 类方法
    @classmethod
    def dance(cls):
        print('我是类方法...')

    # 静态方法
    @staticmethod
    def sleep():
        print('我是静态方法...')
p = Person()

# 调用实例方法 对象名.方法名()
# p.sing()
# 调用类方法 类名.方法名()
# Person.dance()
# 调用静态方法 静态.方法名()
p.sleep()
Person.sleep()