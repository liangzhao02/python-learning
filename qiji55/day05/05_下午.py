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
a = 10

def demo1():
    global a
    a = 20
    print(a)

def demo2():
    print(a)

print(a)
demo1()
print(a)
demo2()

























