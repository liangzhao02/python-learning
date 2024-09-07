# 制作用户登录系统：已知A用户注册的用户名为 aaa，密码是 123456 。具体要求如下：
#
# 登录时需要验证用户名、密码、验证码(固定验证码为 qwer )。
#
# 提示：系统先验证验证码是否正确，正确后再验证用户名和密码。
"""
username = "aaa"
password = 123456
verification_code = "qwer"
"""
username = input("请输入您的用户名：")
password = int(input("请输入您的密码："))
verification_code = input("请输入验证码：")
if verification_code == "qwer":
    if username == "aaa" and password == 123456:
        print("登录成功")
    else:
        print("用户名或密码错误！")
else:
    print("验证码错误！")