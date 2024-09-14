# 1.有列表li = ["1", "13", "11", "6", "8"]，请将列表进行排序，生成：["1", "6", "8", "11", "13"]
# li = ["1", "13", "11", "6", "8"]
# sorted_li = sorted(li, key=int)
# print(sorted_li)
# li1 = []
# for i in li:
#     if i not in li1:
#         li1.append(int(i))
# li1.sort()
# li2 = []
# for i in li1:
#     if i not in li2:
#         li2.append(str(i))
# print(li2)
# 2.使用一行代码生成 [1,4,9,16,25,36,49,64,81,100]
# print([x**2 for x in range(1,11)])

# 3.使用一行代码生成 ["1", "4", "7", "10", "13", "16", "19"]
# print([str(x) for x in range(1, 20, 3)])

# 4.有列表li = [1,2,3,4,5]，使用两种方式完成生成目标列表 [1,4,9,16,25] (注：列表推导式和高阶函数)
# li = [1,2,3,4,5]
# print([x**2 for x in li])
# print(list(map(lambda x: x**2, li)))
# 5.有列表li = [1,4,9,16,25]， 使用两种方式提取出大于10的数，提取结果为 [16,25] (注：列表推导式和高阶函数)
# li = [1,4,9,16,25]
# print([x for x in li if x > 10])
# print(list(filter(lambda x: x > 10, li)))
# 6.使用两种方式将列表 li = [1, 2, 3, 4, 5] 变成 ["1", "2", "3", "4", "5"] (注：列表推导式和高阶函数)
# li = [1, 2, 3, 4, 5]
# print([str(s) for s in li])
# print(list(map(lambda s:str(s), li)))
# print(list(map(str, li)))
# 7. 有列表li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]，求编写代码求出值中出现1的元素的个数
# 注：上述题中值中出现1的元素有 [1, 10, 11, 12, 13, 14] 共6个
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# def has_one_in_list(lst):
#     for num in lst:
#         num_str = str(num)
#         if '1' in num_str:
#             return True
#     return False
# if has_one_in_list(li):
#     print("列表中包含数字1")
# else:
#     print("列表中不包含数字1")

# count = 0
# for num in li:
#     if '1' in str(num):
#         count += 1
# print("列表中包含数字1的元素个数为%d" %count)

# 8. 将以下函数转成匿名函数
"""
def fun_A(x,y=3):
    return x*y
"""
# lambda x , y = 3: x*y


# 9. 将以下匿名函数转成标准函数
"""
lambda x:x if x%2 else None
"""
# def fun(x):
#     if x%2:
#         return x
#     else:
#         return None

# 10. 用 filter() 函数和 lambda 表达式快速求出100以内所有4的倍数
# li = list(range(1,101))
# print(list(filter(lambda x:x%4==0,li)))