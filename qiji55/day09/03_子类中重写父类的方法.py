class Master(object):

    def __init__(self):
        self.skill = '古法煎饼果子配方'

    def make_jbgz(self):
        print('老师傅做的煎饼果子...')

class BigCat(Master):

    def __init__(self):
        self.skill1 = '徒弟的煎饼果子配方'

    def make_jbgz(self):
        print('徒弟做的煎饼果子...')

dalong = BigCat()
# dalong.make_jbgz()
print(dalong.skill1)