# li = ['张三','李四','王五', 18 , 180.1, True]
# print(li)
# print(type(li))
# #18
# print(li[1])
# print(li[2])
# print(li[3])
# print(li[4])
#
# # True
# print(li[3])
# # 张三
# print(li[0])
# # 三
# print(li[0][1])
# 方式1
# for i in li:
#     print(i)
# 方式2
# i = 0
# while i < len(li):
#     print(li[i])
#     i += 1
# len:统计容器中元素的个数
# len(变量名)
# print(len(li))
# print(len('hello'))
# print(len(range(1,11)))

# li = ["张三",180]
# # append:将元素整体添加进去
# # extend:将元素拆分开来添加进去,元素必须是可迭代对象
# # insert:将元素添加到指定位置
# # li.append(18)
# # li.extend("李四")
# # li.extend(range(1,3))
# # for i in "李四"
# #     li.append(i)
# li.insert(1,"李四")
# print(li)
# 修改操作
# 列表名[索引值] = 新值

# print(li[1])
# li[1] = 20
# print(li[1])

# 查看操作
# in :查看某个元素是否在列表中
# not in:查看某个元素不在列表中
# index:查看列表中某个元素的位置,返回索引值
# # count:统计元素出现的次数
# res = '张三' in li
# res = '张三1' in li
# res = 18 not in li
# res = 180 not in li
# res = li.index(18)
# res = li.index(True)
# #li.count(1)
# # res= li.count(18)
# # print(res)
# # 去重
# li = ["张三",18,18]
# li1= []
# for i in li:
#     if i not in li1:
#         li1.append(i)
# print(li1)
#

# 删除操作
# remove:删除指定元素
# pop:默认删除最后一个元素,如果传参数的话,传要删除元素的索引值
# del:关键字删除法,del 列表名[索引值]
# li = ['张三',18]
# # li.remove(18)
# # li.pop(0)
# del li[0]
# del li
# print(li)
# li = [1,9,5,0]
# # 升序
# # li.sort()
# # print(li)
# # 降序
# li.sort(reverse=True)
# print(li)

# li = [1,2,3,4]
# # 方式1
# # print(li[::-1])
# # 方式2
# # li.reverse()
# # 方式3
# li1 = []
# for i in li:
#     li1.insert(0,i)
# print(li)
# print(li1)

cls = [["刘一", "陈二", "张三", "李四"], ["王五", "赵六", "孙七"], ["周八", "吴九", "郑十"]]

# 取出"赵六"
print(cls[1][1])
# 删除"赵六"
del cls[1][1]
print(cls)
# 删除"吴九"
cls[2].remove('吴九')
print(cls)














