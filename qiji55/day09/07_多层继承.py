# 老师傅类
class Master(object):
    def __init__(self):
        self.skill = "古法煎饼果子配方"

    def make_jbgz(self):
        print("老师傅做的煎饼果子...")

# 学校类
class School(Master):

    def make_cxlm(self):
        print("学校做的朝鲜冷面...")

# 徒弟类
class BigCat(School):
    pass

dalong = BigCat()
dalong.make_cxlm()
dalong.make_jbgz()
print(dalong.skill)