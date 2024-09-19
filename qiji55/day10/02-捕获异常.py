# print(a)
# print(10)
#
# try:
    # 尝试捕获的代码
# except:
    # 如果出现问题后的补救代码

# 1.捕获指定类型的异常
# 2.多个异常分开处理
# 3.多个异常统一处理
# 4.捕获未知类型方法异常
li = [3,1,5]

def demo(x, y):
    return x / y

try:
    print(li[10])
    # demo(10,0)

# 捕获未知类型方法异常
except Exception as e:
    print(e)
#   当没有异常时输出的代码
else:
    print('没有异常')
#   无论是否有异常都会输出的代码
finally:
    print('我都会出现')
# 多个异常统一处理
# except (IndexError, ZeroDivisionError):
#     print('出现异常...')
# 多个异常分开处理
# except ZeroDivisionError:
#     print('两数相除,分母不能为0')
# except IndexError:
#     print('索引值超出边界')

print('hi')

