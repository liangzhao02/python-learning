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

#find：用来查找某个字符在大的字符串在的位置，返回索引值，如果不存在，则返回-1
# rfind:
#index：用来查找某个字符在大的字符串在的位置，返回索引值，如果不存在，则报错
#rindex
#count：用来统计某个字符在大的字符串中出现的次数
#split：切割，分割，按照指定分隔符进行分割，返回的是列表的数据类型
#repLace：替换，将字符串中某一部分字符进行替换
#capitalize：将字符串中第一个字符大写
#title：将字符串中每个单词的首字母大写
#startswith：用来判断该字符串是否以某个子符开头
#endswith：用来判断该字符串字符以某个字符结尾
#Lower：将大写转小写
#upper:将小写转大写
#ljsut：左对齐，如果字符串长度不够填写长度，则以空格填充至最右边
#rjust：右对齐，如果字符串长度不够填写长度，则以空格填充至最左边
#center:居中显示
#lstrip:去除字符串左边的空格
#rstrip:去除字符串右边的空格
#strip:去掉字符串左右两边的空格
#partition:分割,分割完永远只返回三部分,分隔符,分隔符之前,分隔符之后,返回的是一个元组的数据类型
#rpartition:从右往左找分割,分割完永远只返回三部分,分隔符,分隔符之前,分隔符之后,返回的是一个元组的数据类型
#splitlines:按照换行符进行分割,返回的是列表的数据类型
# isalpha:判断字符串是否全用字母组成
# isdigit:判断字符串是否全部由数字组成
# isalnum:判断字符串是否由数字或字母组成
# isspace:判断字符串是否全部由空格组成
mstr = "  hello world  "
# res = mstr.find('w')
# res = mstr.find('o')
# res = mstr.rfind('o')
# res = mstr.find('l',3,5)
# mstr.find('x')
# res = mstr.index('l',3,5)
# res = mstr.index('x')
# res = mstr.count('l')
# res = mstr.split(" ")
# res = mstr.ljust(10)
# res = mstr.strip()
# res = mstr.center()
# res = mstr.count()
# res = mstr.capitalize()
# res = mstr.partition("o")
res = mstr.isalpha()

print(res)