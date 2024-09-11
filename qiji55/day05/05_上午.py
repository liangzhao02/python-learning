# li = ['a','b','c']
# # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
# # 同时列出数据和数据下标，一般用在 for 循环当中。
# for i in enumerate(li):
#     # print(i)
#     print('索引为%s,值为%s' %(i[0],i[1]))
# ## 集合 ##
# 无序
# 不重复
# mset = {'a',1,180.1,1}
# print(mset)
# print(type(mset))

# 列表的去重
# li = [1,2,1]
# 方式1
# li1 = []
# for i in li:
#     if i not in li1:
#         li1.append(i)
# print(li1)
# 方式2
# 将列表转为集合 ---去重
# 将集合转为列表 ---输出列表
# print(list(set(li)))

# 定义一个空集合
# mset = set()
# print(mset)
# print(type(mset))

# mset = {'a','b','c'}
# 添加操作
# add:将元素整体添加进去
# update:将元素拆分开来添加进去

# mset.add('x')
# mset.update('早上好')
#
# print(mset)

# 删除操作
# remove:删除指定元素,元素不存在则报错
# pop:随机删除一个元素
# discard:删除指定元素,元素不存在则什么也不做
# mset.remove('a')
# mset.remove('x')
# mset.remove('a')
# mset.discard('a')
# mset.discard('x')
# mset.pop()
# print(mset)
# mset = {'a','b','c'}
# mset1 = {'a','b','x'}
# # 交集 &
# # 并集 |
# # res = mset & mset1
# res = mset | mset1
# print(res)

# 公共方法
# data = {'name':'张三' , 'age': 18}
# # res = '张三' in data.values()
# # res = 'name' in data
# # res = ('name','张三') in data.items()
# # print(res)
#
# print(len(data))
#
# li = [1,5,8]
# print(max(li))
# print(min(li))
# print(sum(li))

# 函数
# def
# 定义
def demo():
    a = 1
    b = 2
    print(a + b)
# 调用
demo()
# print(demo())












