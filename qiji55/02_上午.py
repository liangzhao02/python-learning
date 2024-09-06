"""
age = "180.1"
print(int(float(age)))
print(type(int(float(age))))
print(type(age))
a = 10
b = 15
result = "a + b"
print(eval(result))
print(type(result))

print(a == b)
print(a <= b)
print(a != b)
print(a >= b)
"""

# a = 10
# b = 20
# c = 30
# # res = a == b and b == c
# res = not a == b or b == c
# print(res)
# age = int(input("请输入你的年龄："))
# if age >= 18:
#     print("你可以进网吧上网")
# else:
#     print("不允许进网吧")
# 需求：键盘录入一个分数，判断该分数
# 如果大于90小于等于100分输出优
# 如果大于80小于等于90分输出良
# 如果大于60小于等于80分输出中
# 如果大于等于0小于等于60分输出差
score = int(input("请输入你的分数："))
if 90 < score <= 100:
    print("优")
elif 80 < score <= 90:
    print("良")
elif 60 < score <= 80:
    print("中")
elif 0 < score <= 60:
    print("差")
else:
    print("输入错误，请重现输入！")
