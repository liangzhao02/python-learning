# 2.计算1000以内所有不能被7整除的整数之和

i = 1
sum = 0
while i < 1000:
    if i % 7 != 0:
        sum += i
    i += 1
print(sum)

# sum_value = 0
# for i in range(1000):
#     if i % 7!= 0:
#         sum_value += i
# print(sum_value)