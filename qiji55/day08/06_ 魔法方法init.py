# __init__ :魔法方法,不需要手动调用,在对象创建的那一刻自动调用方法

class Person(object):
    def __init__(self):
        # self是一个万能词,哪个对象调用该方法,self就是那个对象名
        self.name = '张三'
        self.age = 18
        print('我被调用了')

    def sing(self):
        # 在类中获取属性
        print('%s在唱歌' % self.name)

# 类外获取属性
# 对象名.属性名
p = Person()
p1 = Person()
# p.sing()
print(p.name)
print(p.age)
print(p1.name)
print(p1.age)