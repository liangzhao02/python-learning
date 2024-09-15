# class Person(object):
#
#     def __init__(self, name, age):
#         # self.属性名 = 属性值
#         self.name = name
#         self.age = 18
#
#     def sing(self):
#         print('%s在唱歌...' % self.name)
#
# p = Person('张三',18)
# p1 = Person('李四',20)
# print(p.name)
# print(p1.name)
# p1.sing()
#
# 创建一个汽车类（Car），包含三个属性，分别是颜色（coLor）、型号（modeL）、马力（horsepower）
# 分别创建宝马（Bmw）奔驰（Benz）的对象，打印对象身上所有属性值
class Car(object):
    def __init__(self,color,model,horsepower):
        self.color = color
        self.model = model
        self.horsepower = horsepower

    def __str__(self):
        return '颜色是:%s,型号是:%s,马力是:%s' % (self.color, self.model, self.horsepower)

Bmw = Car('black',8,4000)
print(Bmw.color)
print(Bmw.model)
print(Bmw.horsepower)
print(Bmw)
print('宝马的颜色是：%s，型号是：%s，马力是：%s' %(Bmw.color,Bmw.model,Bmw.horsepower))
Benz =Car('black','s',5000)
print(Benz.color)
print(Benz.model)
print(Benz.horsepower)
print('奔驰的颜色是：%s，型号是：%s，马力是：%s' %(Benz.color,Benz.model,Benz.horsepower))
print(Benz)