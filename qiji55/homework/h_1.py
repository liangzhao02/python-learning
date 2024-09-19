# # 1.编写程序，求 1 - 3 + 5 - 7 + 9 -11 + 13 - 15 ... - 99 + 101 的值    答案51
# # range(start, stop[, step])
# # start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
# # stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
# # step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
result = 0
sign = 1
for i in range(1, 102, 2):
    result += sign * i
    sign *= -1
print(result)

# i = 1
# sum = 0
# a = 1
# while i <= 101:
#     if i % 2 != 0:
#         sum += i * a
#         a *= -1
#     i += 1
# print(sum)
#
# # result = result + sign * i
# # sign = sign * -1
# # 1-3+5-7+9-11
#
# # sum_value = 0
# # i = 1
# # sign = 1
# # while i <= 101:
# #     sum_value += i * sign
# #     sign *= -1
# #     i += 2
# # print(sum_value)