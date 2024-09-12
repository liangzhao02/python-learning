# 定义一个字典，用于保存所有的学生信息
all_dict = {}

def show_menu():
    """显示菜单"""
    print('---------------------------')
    print('      学生管理系统 V1.0')
    print(' 1:添加学生信息')
    print(' 2:删除学生信息')
    print(' 3:修改学生信息')
    print(' 4:查询学生信息')
    print(' 5:显示所有学生')
    print(' 6:退出系统')
    print('---------------------------')
    ret = input('请选择：')
    return int(ret) if ret in list("123456") else 0


def save_info():
    """添加学生信息"""
    my_no = input('请输入添加学生的学号：')

    if my_no in all_dict:
        print('该学号已经存在...')
        return

    my_name = input('请输入添加学生的名字：')
    my_score = input('请输入添加学生的分数：')
    # 构造一个小字典
    my_dict = {'no': my_no, 'name': my_name, 'score': my_score}
    # 保存到all_dict中
    all_dict[my_no] = my_dict
    print('保存学生信息成功...')


def del_info():
    """删除学生信息"""

    my_no = input('请输入要删除的学生的学号：')
    if my_no not in all_dict:
        print('该学号不存在...')
        return

    del all_dict[my_no]
    print('删除学生信息成功...')


def update_info():
    """更新学生信息"""
    my_no = input('请输入要修改的学生的学号：')

    if my_no not in all_dict:
        print('该学号不存在...')
        return

    new_name = input('请输入学生新的名字：')
    new_score = input('请输入学生新的分数：')
    # 构造学生信息字典
    my_dict = {'no': my_no, 'name': new_name, 'score': new_score}
    all_dict[my_no] = my_dict
    print('修改学生信息成功...')


def find_info():
    """查询学生信息"""
    my_no = input('请输入要查询的学生的学号：')

    if my_no not in all_dict:
        print('该学号不存在...')
        return

    my_dict = all_dict[my_no]
    print('----该名学生信息如下:----')
    print('学号:%s' % my_dict['no'])
    print('名字:%s' % my_dict['name'])
    print('分数:%s' % my_dict['score'])
    print('------------------------')
    print('查询学生信息成功...')

def show_all_info():
    """显示所有的学生信息"""
    print('-----xx班级所有学生信息-----')
    for value in all_dict.values():
        print('----该名学生信息如下:----')
        print('学号:%s' % value['no'])
        print('名字:%s' % value['name'])
        print('分数:%s' % value['score'])
        print('------------------------')


def main():
    while True:
        index = show_menu()
        if index == 1:
            # 1:添加学生信息
            save_info()
        elif index == 2:
            # 2: 删除学生信息
            del_info()
        elif index == 3:
            # 3:修改学生信息
            update_info()
        elif index == 4:
            # 4:查询学生信息
            find_info()
        elif index == 5:
            # 5:显示所有学生
            show_all_info()
        elif index == 6:
            # 6:退出系统
            break
        else:
            print('输入有误，请重新输入...')
main()