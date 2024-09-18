# 实例属性 在init中定义的,需要用对象来调用
# 类属性 定义在类中,方法外的属性

class Master(object):
    # 类属性
    money = 100
    # 实例属性
    def __init__(self, name, age):
        self.name = name
        self.age = age


m = Master('张三',18)
# 获取实例属性 对象名.属性名
# print(m.name)
# print(m.age)
# 修改实例属性 对象名.属性名 = 新值
# m.age = 20
# print(m.age)
# print(m.money)
# print(Master.money)
Master.money = 200
print(Master.money)
















