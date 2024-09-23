# No.27
# li = [8,3,1,2,5]
# for i in range(0, len(li)-1):
#     for j in range(0, len(li)-1-i):
#         if li[j] > li[j+1]:
#             li[j], li[j+1] = li[j+1], li[j]
# print(li)

# No.28
def reverse_number(num):
    if num < 0:
        sign = -1
        num = -num
    else:
        sign = 1

    reversed_num = int(str(num)[::-1]) * sign
    return reversed_num

# 测试
num1 = 567
num2 = -346
num3 = 19000

reversed_num1 = reverse_number(num1)
reversed_num2 = reverse_number(num2)
reversed_num3 = reverse_number(num3)

print(reversed_num1)  # 输出 765
print(reversed_num2)  # 输出 -643
print(reversed_num3)  # 输出 91
















