# __all__:是一种约束,当使用from 模块名 import * 可以使用哪些
__all__ = ['age','demo']

# 全局变量
age = 18
# 函数
def demo(x, y):
    print(x, y)
# 类
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
# 测试代码
# 在本模块中应该执行,当被其他模块调用时不应该执行
# __name__ :是在当前模块下运行,值为__main__;但被其他模块调用时,值为对应模块的模块名
if __name__ == '__main__':
    print(age)
    demo(1,2)
    p = Person('zhangsan',18)
    print(p)
