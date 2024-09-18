class Master(object):

    def __init__(self):
        # 私有属性
        self.__money = 1000
        self.skill = '古法煎饼果子配方'

    def make_jbgz(self):
        print('老师傅做的煎饼果子')

    # 私有方法
    def __make_cxlm(self):
        print('老师傅做的朝鲜冷面')
class Bigcat(Master):
    pass

p = Bigcat()
# print(p.money)
print(p.skill)
p.make_cxlm()