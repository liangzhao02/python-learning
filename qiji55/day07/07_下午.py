# from functools import reduce
#
# # reduce:可以将容器中的元素进行累计
# li = [1,2,3,4]
# # print(sum(li))
#
# def demo(x,y):
#     return x + y
#
# res = reduce(demo, li)
# print(res)
#  1.打开或者新建文件
# f = open('./aaa.txt',mode='w',encoding='utf-8')
# 2.写入内容
# f.write('Today is Good!')
# 3.关闭内容
# f.close()
from os import rename

# read:读取文件中全部内容
# readline:以行为单位进行读取
# readlines:读取全部的内容,以列表的形式输出
# 1.打开文件
# f = open('./aaa.txt','r',encoding='utf8')
# 2.读取内容
# content1 = f.read()
# print(content1)
# content2 = f.readline()
# content3 = f.readline()
# print(content2)
# print(content3)
# content4 = f.readlines()
# print(content4)
# 3.关闭文件
# f.close()


# 备份
# 1.打开原文件
# f = open('./aaa.txt','r',encoding='utf-8')
# 2.新建文件
# f1 = open('./aaa[备份].txt','w',encoding='utf-8')
# 3.读取原文件中的内容
# content = f.read()
# 4.将读取出来的内容写入新文件
# f1.write(content)
# 5.关闭原文件
# f.close()
# 6.关闭新文件
# f1.close()

import os
# 文件及文件夹的相关操作
# 文件的重命名 rename
# 删除文件 remove
# os.rename('./aaa.txt', './abc.txt')
# os.remove('./aaa[备份].txt')
# 新建文件夹 mkdir
# os.mkdir('AAA')
# 获取当前所在位置 getcwd
# print(os.getcwd())
# 切换目录位置 chdir
# os.chdir(r'D:\WorkProject\Python_qiji55\qiji55')
# print(os.getcwd())
# 获取目录列表 listdir
# print(os.listdir())
# 删除文件夹 rmdir
os.rmdir('AAA')



















