# 提示用户在控制台输入一个天数，然后把天数折算成秒数，并在控制台输出。
# 要求输出内容格式：xx天等于xx秒

day = int(input("请输入一个天数："))
second = day * 24 * 60 * 60
print("%d天等于%d秒" % (day, second))