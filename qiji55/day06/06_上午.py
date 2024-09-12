# return返回值的作用
# 1.将函数的执行结果返回给调用者
# 2.结束函数的调用

# def demo1(a,b):
#     print(a)
#     return a + b
#
#
# res = demo1(1,2)
# print(res)

# # 返回多个值
# def demo2(a,b):
#     # return a, b
#     # return [a, b]
#     # return {'第一个元素为':a , '第二个元素为':b}
#     return {a,b}
#
# res = demo2(1,2)
# print(res)

# 位置参数:形参和实参的数量及位置都是一一对应的
# 关键字参数:在调用函数时,指定形参的名字来进行调用
# 缺省值参数:在定义函数时设置一个参数的默认值,如果传了新值,则走新值.如果没传新值,则走默认值
# 不定长参数
#     不定长位置参数:传入位置参数的个数不确定,一般用*args来表示,默认返回元组的数据类型
#     不定长关键字参数:调用函数时关键字参数的个数不确定,一般用**kwargs来表示,返回的是字典的数据类型

# 不定长位置参数
# def demo4(a,*args):
#     print(a)
#     print(args)
#
# demo4(1,2,3,4,5)
# # 不定长关键字参数
# def demo5(a,**kwargs):
#     print(a)
#     print(kwargs)
#
# demo5(a = 1 , b = 2 , c = 3 , d = 2 , e = 8)
#
#
#
# def demo3(a = 10,b = 20):
#     print(a)
#     print(b)
#
# # demo3(1,2)
# # demo3()
#
# def demo2(a,b):
#     print(a)
#     print(b)
#
# # demo2(a = 1,b = 2)
#
# def demo1(a,b):
#     print(a)
#     print(b)
#     print(a + b)
#
# # demo1(1,2)

# a = 1
# b = a
# a = 2
# print(a)
# print(id(a))
# print(b)
# print(id(b))

# a = [1]
# b = a
# a.append(2)
# print(a)
# print(id(a))
# print(b)
# print(id(b))

#id(变量名)：可以查看某个变量的内存地址值


# 不可变类型：字符串，数字，元组
# 可变类型：列表，字典，集合

# ==和is的区别:
# ==:表判断,判断左右两边的数值是否相等
# is:判断左右的内存地址值是否相等
#
# a = 1
# b = 1
# print(a == b)
# print(id(a))
# print(id(b))
# print(id(a) == id(b))
# print(a is b)

# a = [1]
# b = [1]
# print(a == b)
# print(id(a))
# print(id(b))
# print(id(a) == id(b))
# print(a is b)

# a =(1,2)
# b =(1,2)
# print(id(a))
# print(id(b))

import copy
# 拷贝:复制
# 深拷贝:完完全全拷贝,拷贝出来的数据和原数据没有任何关系
data = {'name':'张三','age':[18,19,20]}
# data1 = copy.deepcopy(data)
# 字典的添加操作
# data['height'] = 180
# 字典值的添加操作 列表的添加操作
# data['age'].append(30)
# print(data)
# print(data1)
# 浅拷贝:只拷贝表层数据,内部子对象不会被拷贝
# 表层数据发生变化,拷贝后的数据不会发生变化
# 内部子对象数据发生变化,拷贝后的数据会发生变化
data1 = copy.copy(data)
# 字典的修改操作
# data['age'] = [30,40,50]
# 字典的添加操作
# data['height'] = 180
#
# data['age'].append(20)
# data['age'].remove(20)

print(data)
print(data1)























