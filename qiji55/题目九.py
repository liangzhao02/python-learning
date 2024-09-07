# 设计简易计算器，可以进行基本的加减乘除运算, 参考如下
# 请输入第一个数字:
# 请输入第二个数字:
# 请输入要进行的操作(+ - * /):
# 计算的结果为:
# 举例如下:
# 请输出第一个数字: 10
# 请输入第二个数字: 20
# 请输入要进行的操作(+ - * /): +
# 计算的结果为: 10 + 20 = 30
# calculator
"""简易的计算器，暂时不考虑输入数字为浮点数的时候"""
m = int(input("请输入第一个数字："))
n = int(input("请输入第二个数字："))
operate = input("请输入要进行的操作：+ - * /：")
if operate == "+":
    result = m + n
    print("计算的结果是：%d + %d = %d " % (m,n,result))
elif operate == "-":
    result = m - n
    print("计算的结果是：%d - %d = %d" % (m, n, result))
elif operate == "*":
    result = m * n
    print("计算的结果是：%d * %d = %d" % (m, n, result))
elif operate == "/":
    result = float(m / n)
    print("计算的结果是：%d / %d = %.2f" % (m, n, result))
else:
    print("输入有误，请重新输入！")