from time import sleep
all_data = {}

def add_stu_info():
    no = input('请输入要添加学生的学号:')
    if no in all_data:
        print('该学号已存在...')
        return
    name = input('请输入要添加学生的姓名:')
    score = input('请输入要添加学生的成绩:')
    # 人为构造嵌套的字典
    stu_info = {'name': name, 'no': no,  'score': score}
    # 字典的添加操作
    all_data[no] = stu_info
    print('学生信息添加成功...')

def delete_stu_info():
    no = input('请输入要删除学生的学号:')
    if no not in all_data:
        print('该学号不存在...')
        return
    # 字典的删除操作
    del all_data[no]
    print('学生信息删除成功...')

def update_stu_info():
    no = input('请输入要修改学生的学号:')
    if no not in all_data:
        print('该学号不存在...')
        return
    new_name = input('请输入修改后的学生姓名:')
    new_score = input('请输入修改后的学生成绩:')
    stu_info = {'name': new_name, 'score': new_score}
    # 字典的修改操作
    all_data[no] = stu_info
    print('学生信息修改成功...')

def query_stu_info():
    no = input('请输入要查询的学生的学号:')
    if no not in all_data:
        print('该学号不存在...')
        return
    query_info = all_data[no]
    print('该学生的学号为:%s' % query_info['no'])
    print('该学生的姓名为:%s' % query_info['name'])
    print('该学生的成绩为:%s' % query_info['score'])

def show_stu_info():
    if len(all_data) == 0:
        print('暂无学生信息...')
        return
    for value in all_data.values():
        print('----该名学生信息如下:----')
        print('学号:%s' % value['no'])
        print('名字:%s' % value['name'])
        print('分数:%s' % value['score'])
        print('------------------------')

while True:
    print('---------------------------')
    print('      学生管理系统 V1.0')
    print(' 1:添加学生信息')
    print(' 2:删除学生信息')
    print(' 3:修改学生信息')
    print(' 4:查询学生信息')
    print(' 5:显示所有学生')
    print(' 6:退出系统')
    print('---------------------------')

    ret = input('请选择您要进行的操作：')
    if ret == '1':
        add_stu_info()
    elif ret == '2':
        delete_stu_info()
    elif ret == '3':
        update_stu_info()
    elif ret == '4':
        query_stu_info()
    elif ret == '5':
        show_stu_info()
    elif ret == '6':
        print('正在退出系统,请稍候')
        sleep(3)
        break
    else:
        print('您输入的有误,请重新输入!')


