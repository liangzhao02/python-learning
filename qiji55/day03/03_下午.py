#切片：可以取出字符串中某一部分字符
# 变量名[起始值:结束值:步长]
# 起始值：要截取数据开始位置的索引值
# 结束值：要截取数据结束位置的下一位的索引值
# 步长：将结果中相邻两位的下一位减去上一位的索引值，默认为1，可以不写
# name = 'abcdefg'
# print(name[::-1])
# # gda
# print(name[-1:-8:-3])
# """
# name[:]表示从序列name的开头一直到结尾进行切片,相当于复制了整个序列.
# name[::]也表示从序列name的开头一直到结尾进行切片,并且步长为 1（步长默认为 1 时可以省略不写）,
# 同样相当于复制了整个序列
# """
# print(name[:])
# print(name[::])
# print(name[::1])
# print(name[::-1])

# find：用来查找某个字符在大的字符串在的位置,返回索引值
# index：用来查找某个字符在大的字符串在的位置,返回索引值
# mstr = "hello world"
# res = mstr.find('w')
# res = mstr.find('o')
# res = mstr.rfind('o')
# res = mstr.find('l',3,5)
# mstr.find('x')
# res = mstr.index('l',3,5)
# res = mstr.index('x')
# res = mstr.count('l')
# res = mstr.split(" ")
# print(res)