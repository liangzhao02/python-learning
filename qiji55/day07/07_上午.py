# 无参数无返回值
# def demo1():
#     print(1)

# demo1 = lambda: print(1)
# demo1()
# 无参数有返回值
# def demo2():
#     return 1

# demo2 = lambda:1
# res = demo2()
# print(res)
# 有参数无返回值
# def demo3(a,b):
#     print(a + b)

# demo3 = lambda a,b:print(a + b)
# demo3(1,2)
# 有参数有返回值
# def demo4(a,b):
#     return a + b

#
# demo4 = lambda a,b:a + b
# result = demo4(1,2)
# print(result)

# 需求:以列表的形式输出1-100之间的所有数
# 方式1
# li = []
# for i in range(1,101):
#     li.append(i)

# 方式2
# li = [i for i in range(1,101)]
# print(li)

# 需求:以列表的形式输出1-100之间的所有的偶数
# li = [i for i in range(2,101,2)]
# li = [i for i in range(1,101) if i % 2 == 0]
# print(li)
# 需求:以列表的形式输出以下两字名字的各种组合
# a = ['赵','王','孙','李']
# b = ['一','二','三','四']
# li = [x + y for x in a for y in b]
# print(li)

# map:是一个函数,可以将列表按照指定规则输出
# 输出列表['1','2','3','4']
# li =[1,2,3,4]
# 方式1
# li1 = []
# for i in li:
#     li1.append(str(i))
# print(li1)

# 方式2
# li1 =[str(i) for i in li]
# print(li1)

# def demo(x):
#     return str(x)
#
# res = list(map(demo,li))
# print(res)

#输出列表['Hello','Hi','Itfeat']
# my_list =['hello','hi','itfeat']
#
# def demo(s):
#     s_ =str(s.capitalize())
#     return s_
# res = list(map(demo,my_list))
# print(res)

# my_list = ['hello', 'hi', 'itfeat']
# new_list = list(map(str.capitalize, my_list))
# print(new_list)

# my_list = ['hello', 'hi', 'itfeat']
# new_list = [word.capitalize() for word in my_list]
# print(new_list)

# res = list(map(lambda x:x.capitalize(), my_list))
# print(res)

# filter:是一个函数,将列表按照某种规则进行过滤
# 以列表的形式输出[2,8]
li = [1,2,5,8]
# 方式1
# li1 = []
# for i in li:
#     if i % 2 == 0:
#         li1.append(i)
# print(li1)

# def demo(x):
#     if x % 2 == 0:
#         return x
# def demo(x):
#         return x ** 2    map实现输出[1,4,25,64]
# res = list(map(demo,li))
# res = list(filter(demo,li))
# res = filter(lambda x: x % 2 == 0, li)
# print(list(res))

#输出列表['HeLLo','Itfeat']
li = ['Hello','hi','Itfeat']
# def demo(x):
#     if x == x.capitalize():
#         return x
# def demo(x):
#     if x[0].isupper():
#         return x
demo = lambda x: x[0].isupper()
res =list(filter(demo,li))
# res =list(filter(lambda x:x[0].isupper(),li)
# res = list(filter(lambda x:x == x.capitalize(),li))
print(res)












