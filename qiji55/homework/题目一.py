# 题目一
# 需求:
name = "张三"
age = 25
height = 180.66
# 1. 提示用户输入用户姓名，并保存到变量中
name = input("请输入您的姓名：")
# # 2. 提示用户输入用户年龄，保存到变量中，并转换成整数
name = int(input("请输入您的姓名："))
# # 3. 提示用户输入用户身高，保存到变量中，并转换成浮点数
height = float(input("请输入您的身高："))
# 4. 在控制台输出用户姓名、年龄、身高对应变量的数据类型
print(type(name))
print(type(height))
print(type(age))
# 5. 按照以下格式输出用户信息:“姓名:xxx 年龄:xxx 身高:xxx”
print("姓名：%s 年龄：%d height：%f" %(name,age,height))
# 6. 在控制台输出该用户5年之后的年龄，格式:“张三 5 年之后的年龄是 25”
print("张三5年之后的年龄是%d" % age)
# 7. 在控制台输出该用户现在是否成年，格式:“张三是否成年:True”
print("张三是否成年：True")