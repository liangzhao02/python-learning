def demo1(x, y):
    print(x / y)

def demo2(a, b):
    demo1(a, b)

try:
    demo2(2, 0)
except ZeroDivisionError:
    print('can not divide by zero')