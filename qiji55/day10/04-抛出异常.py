class AgeError(Exception):
    pass


class Person(object):

    def __init__(self, name, age):
        self.name = name
        if age < 0:
        # 抛出异常
        # 1.自定义一个异常类
        # 2.抛出异常
            e = AgeError('年龄不正确')
            raise e
        self.age = age

p = Person('张三',-22)