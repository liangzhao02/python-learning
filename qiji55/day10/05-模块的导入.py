# 1.import 模块名
# 用法:模块名.全局变量/函数/类
# 2.from 模块名 import 全局变量/函数/类
# 用法:全局变量/函数/类
# 3.from 模块名 import *
# 用法:全局变量/函数/类

# import itfeat
# print(itfeat.age)

# from itfeat import demo
# demo(1,2)

from itfeat import *
print(age)
demo(1,2)
p = Person('张三',18)
print(p)