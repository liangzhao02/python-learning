# #面试题：列表和元组的区别
# #1.列表是用中括号定义的,元组是用小括号定义的
# #2.列表支持增删改查等一系列操作,元组只支持查看操作
# t = ('张三',18,180.1,18)
# # t = ('张三',)
# #print（t)
# #print(type(t))
# #18
# #print(t[1])
# #print(t[θ])
# #print（t[::-1])
#
# # in
# # not in
# # index
# # count
#
# # res = 18 in t
# # res = 1 not in t
# # res = t.index(18)
# res = t.count(18)
# print(res)
# data = {'name':'张三',"age":18}
# 取值
# 字典名[键名]
# print(data['age'])
# 字典名.get(键名)
# print(data.get('age'))

# print(type(data))
# 添加
# 字典名[键名] = 新值   键不存在
# data['height'] = 180

# 修改
# 字典名[键名] = 新值   键存在
# data['age'] = 20
# print(data)

# 删除
# pop:删除指定键值对
# data.pop('age')
# del:del关键删除法
# del data['age']
# clear:清空字典
# data.clear()
# print(data)
# data = {'name':'张三',"age":18}
#遍历所有的键
# 方式1
# for i in data:
#     print(i)
# 方式2
# for i in data.keys():
#     print(i)
#遍历所有的值
# 方式1
# for i in data:
#     print(data[i])
# 方式2
# for i in data.values():
#     print(i)
#遍历所有的键值对
# 方式1
# for i in data:
#     print('键为%s,值为%s' %(i,data[i]))
# 方式2
# for i in data.items():
#     print('键为%s,值为%s' % (i[0],i[1]))

# join:拼接,将列表中的元素按照指定拼接符
li = ['a','b','c']
mstr = '*'
res = mstr.join(li)
print(res)














