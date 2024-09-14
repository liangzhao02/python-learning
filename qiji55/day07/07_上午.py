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

demo4 = lambda a,b:a + b
result = demo4(1,2)
print(result)