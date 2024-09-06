import random
#出拳设置
#人出拳input（）石头（0）／剪刀(1）／布（2)关于
person=int(input("石头（0）／剪刀（1）／布（2）"))
#电脑出拳random
computer = random.randint(0,2)
#print(computer)
#查看双方都出了什么print()
print("人出的是%d，电脑出的是%d" %(person,computer))
#比较
#1.平局人和电脑出的相同
if person == computer:
    print("平局")
#2.人赢
# 人出0电脑出1
# 人出1电脑出2
# 人出2电脑出8
elif(person ==0 and computer == 1) or(person ==1 and computer == 2)or(person == 2 and computer == 0):
    print("恭喜你，取得胜利。。")
#3.电脑赢
# 电脑出0人出1
# 电脑出1人出2
# 电脑出2人出0
elif(computer == 0 and person == 1) or (computer == 1 and person == 2) or (computer == 2 and person == 0):
    print("别灰心，再试试。。")
else:
    print("输入有误，请重新输入")