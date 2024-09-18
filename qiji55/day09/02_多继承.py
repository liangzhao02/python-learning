# 老师傅类
class Master(object):
    # object 顶级父类

    def __init__(self):
        self.skill = '古法煎饼果子配方'

    def make_jbgz(self):
        print('老师傅做的煎饼果子...')

# 学校类
class School(object):

    def __init__(self):
        self.skill1 = '学校的煎饼果子配方'

    def make_cxlm(self):
        print('学校做的朝鲜冷面...')

    def make_jbgz(self):
        print('学校做的煎饼果子...')

# 徒弟类
class BigCat(Master, School):
    pass

dalong = BigCat()
dalong.make_jbgz()
dalong.make_cxlm()
# 多个父类中有相同方法名,子类对象调用该方法,会先从自身调用,
# 如果没有,则会按照继承的先后顺序进行调用,子类括号中父类的顺序
# __mro__ 查看某个类调用的属性的先后顺序
# 类名.__mro__
print(BigCat.__mro__)

# 获取多个父类中的属性时,按照子类对象调用init方法的顺序来获取
print(dalong.skill)
print(dalong.skill1)