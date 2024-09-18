class Master(object):

    def __init__(self):
        # 私有属性
        self.__money = 1000
        self.skill = '古法煎饼果子配方'
    # 定义一个共有方法
    def get_money(self):
        print('钱数为%s ' % self.__money)

    # 修改私有属性的值
    def set_money(self, x):
        self.__money = x
class Bigcat(Master):
    pass

dalong = Bigcat()
# 方式1 在类中新建一个公共方法,在该方法内获取私有属性值,在类外进行调用即可
# dalong.get_money()
# dalong.set_money(20000)
# dalong.get_money()

# 方式2
# dir 可以查看某个对象可以调用的所有的属性和方法
print(dir(dalong))
print(dalong._Master__money)