# 批量创建文件
# for num in range(1,11):
#     f = open(r'D:\WorkProject\Python_qiji55\qiji55\AAA\abc%s.txt' % num,'w',encoding='utf-8')
#     f.write('hi')
#     f.close()
# 批量修改文件名
import os
# 1.切换目录 chdir
os.chdir(r'D:\WorkProject\Python_qiji55\qiji55\AAA')
# 2.获取目录列表 listdir
res = os.listdir()
# print(res)
# 3.遍历列表,进行批量修改名字 rename(旧名字,新名字)
for old_name in res:
    new_name = '[奇技课堂]' + old_name
    os.rename(old_name, new_name)