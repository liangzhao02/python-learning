# 写一个函数打印一条横线

# def print_one_line():
#     print('-' * 30)
#
# print_one_line()

# 打印自定义行数的横线
# def print_lines(x):
#     for i in range(0,x):
#         print_one_line()
#
# print_lines(30)

# 全局变量
# a = 10
#
# def demo1():
#     # 局部变量
#     a = 20
#     print(a)
#
# def demo2():
#     print(a)
#
# print(a)
# demo1()
# demo2()
# a = 30
# demo2()
# a = 10
#
# def demo1():
#     global a
#     a = 20
#     print(a)
#
# def demo2():
#     print(a)
#
# print(a)
# demo1()
# print(a)
# demo2()
# t = (3,1,5)
# # 方式1
# a,b,c = t
# print(a)
# print(b)
# print(c)
# # 方式2
# print(*t)

# a = 1
# b = 2
# # 方式1
# # c = a
# # a = b
# # b = c
#
# # 方式2
# # a,b = b,a
#
# # 方式3 只适用于都为数字的情况,两数相减法
# a = a + b #3
# b = a - b #1
# a = a - b #2
#
# print(a)
# print(b)
# 九九乘法表
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         result = i * j
#         print("%d * %d = %d\t" % (j, i, result), end="")
#         j += 1
#     print()
#     i += 1

for i in range(1,10):
    for j in range(1,i+1):
        result = i * j
        print("%d * %d = %d\t" % (j, i, result), end="")
    print()















