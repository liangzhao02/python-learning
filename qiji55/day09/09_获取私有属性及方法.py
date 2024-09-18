class Master(object):

    def __init__(self):
        # 私有属性
        self.__money = 1000
        self.skill = '古法煎饼果子配方'
    # 定义一个共有方法
    def get_money(self):
        print('钱数为%s ' % self.__money)


class Bigcat(Master):
    pass

dalong = Bigcat()
dalong.get_money()