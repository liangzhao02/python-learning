# 要求：打印如下图形：
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# print("*" , end ='')
# 外层循环控制的是行数
# i = 1
# while i <= 5:
#     #内层循环，控制的是每行的个数
#     j = 1
#     while j <= 5:
#         print("* " , end ='')
#         # end是为了不换行
#         j = j + 1
#     print()
#     # print不是为了输出，为了换行
#     i = i + 1
# 打印三角形
# *
# * *
# * * *
# * * * *
# * * * * *
# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print("* ", end='')
#         j += 1
#     print()
#     i += 1
#九九乘法表
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         result = j * i
#         print("%d * %d = %d" % (i, j, result), end="  ")
#         j += 1
#     print()
#     i += 1
# range:可以生成指定范围内的数,是一个可迭代对象
# range：可以生成指定范围内的数,是一个可迭代对象
# range(起始值,结束值,步长)
# 起始值：要生成范围的开始的数值,默认是0
# 结束值：要生成范围内结束位置的值,应该取结束位置下一位的值
# 步长：默认为1,可以不写
# for i in range(2,101,2):
#     print(i , end = '  ')
# 需求1 for循环生成1-100之间所有数的和
# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum , end= '')
# 需求2 for循环生成1-100之间所有偶数的和
# sum = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         sum += i
# print(sum)

# n = 5
# while n > 0:
#     i = n
#     while i > 0:
#         print('* ', end='')
#         i -= 1
#     print()
#     n -= 1
#break：终止循环，结束循环，不再进行循环
#continue：结束本次循环，立即进入下一次循环
#需求打印1-5之间所有的数，遇到3就不打印1245
# i = 0
# while i < 5:
#     i = i + 1
#     print('----')
#     if i== 3:
#         continue  #break
#     print(i)
# else:
#     print("==while循环过程中，如果没有执行break退出，则执行本语句==")
# 索引：可以取出字符串中的某一个字符
# 分类
# 正向索引：从左往右数，默认从0开始
# 反向索引：从右往左数，默认从-1开始
# 用法：
# 变量名[索引值]


















