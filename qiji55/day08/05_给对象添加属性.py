class Person(object):

    def sing(self):
        print('我在唱歌...')


p = Person()
# 给对象添加属性 : 对象名.属性名 = 属性值
p.name = '张三'
# 获取对象的属性 : 对象名.属性名
print(p.name)
# 修改对象的属性 : 对象名.属性名 = 新值
p.name = '李四'
print(p.name)

p1 = Person()
p1.age = 18
print(p1.age)