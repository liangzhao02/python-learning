# 算法 两两进行对比 大的放在后面

li = [9,5,4,6,1]
# 轮数:元素数-1
# 外层循环控制的是轮数
for j in range(0,len(li)-1):
    # 内层循环控制的是每轮比较的次数
    for i in range(0,len(li)-1-j):
        if li[i] > li[i+1]:
            li[i],li[i+1] = li[i+1],li[i]

print(li)
# 第一轮5-1 n-j
# 第一次[5,9,4,6,1]
# 第二次[5,4,9,6,1]
# 第三次[5,4,6,9,1]
# 第四次[5,4,6,1,9]

# 第二轮5-2
# 第一次[4,5,6,1,9]
# 第二次[4,5,6,1,9]
# 第三次[4,5,1,6,9]

# 第三轮5-3
# 第一次[4,5,1,6,9]
# 第二次[4,1,5,6,9]
#
# 第四轮5-4
# 第一次[1,4,5,6,9]

# def bubble_sort(arr):
#     n = len(arr)
#     # 遍历所有元素
#     for i in range(n):
#         # 标记是否有交换发生
#         swapped = False
#         # 最后的i个元素已经有序，不需要再比较
#         for j in range(0, n-i-1):
#             # 如果前一个元素大于后一个元素，则交换它们
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#         # 如果没有发生交换，说明已经有序，可以提前结束
#         if not swapped:
#             break
#     return arr
#
# # 测试
# arr = [64, 34, 25, 12, 22, 11, 90]
# sorted_arr = bubble_sort(arr)
# print("排序后的数组:", sorted_arr)
