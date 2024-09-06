age = int(input("请输入你的年龄："))
if age >= 18:
    print("运行进入网吧")
    money = int(input("请输入现在余额："))
    if money >= 10:
        print("可以上网")
    else:
        print("不允许上网")
else:
    print("不允许进入网吧")