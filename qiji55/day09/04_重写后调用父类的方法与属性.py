class Master(object):

    def __init__(self):
        self.skill = '古法煎饼果子配方'

    def make_jbgz(self):
        print('老师傅做的煎饼果子...')

class BigCat(Master):

    def __init__(self):
        # 在类中 父类类名.__init__(self)
        Master.__init__(self)
        self.skill1 = '徒弟的煎饼果子配方'

    def make_jbgz(self):
        # 在类中:父类类名.同名方法名(self)
        Master.make_jbgz(self)
        print('徒弟做的煎饼果子...')

dalong = BigCat()
# 在类外
# 调用重写后父类中的方法:父类类名.同名方法名(子类对象)
# print(Master.make_jbgz(dalong))
# dalong.make_jbgz()

# 调用重写后父类中的属性:父类类名.__init__(子类对象)
Master.__init__(dalong)
print(dalong.skill)
# print(dalong.skill)
# print(dalong.skill1)