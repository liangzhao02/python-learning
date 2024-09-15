# __del__:是一个魔法方法,不需要手动调用,在对象被销毁时会自动调用该方法
# 对象被销毁
# 1.系统回收
# 2.人为删除 del
class Person(object):
    def sing(self):
        print('在唱歌...')
    def __del__(self):
        print('啊 我被销毁了...')

p = Person()
print('好好学习')
print('好好学习')
del p
print('好好学习')
print('好好学习')