# 老师傅类
class Master(object):
    # object 顶级父类

    def __init__(self):
        self.skill = '古法煎饼果子配方'

    def make_jbgz(self):
        print('老师傅做的煎饼果子...')

# 徒弟类
class BigCat(Master):
    pass

# 创建子类对象
dalong = BigCat()
dalong.make_jbgz()
print(dalong.skill)