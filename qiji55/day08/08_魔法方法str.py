# __str__:是一个魔法方法,不需要手动调用,会在对象被打印时自动调用
class Person(object):
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def __str__(self):
        return '名字为:%s,年龄为:%s' %(self.name,self.age)

p = Person('张三',18)
print(p)





