# vim: set fileencoding:utf-8
import numpy as np

'''
假设一个团队里有5名学员，成绩如下表所示。
1.用NumPy统计下这些人在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。
2.总成绩排序，得出名次进行成绩输出。
'''

scoretype = np.dtype({
    'names': ['name', 'chinese', 'english', 'math', 'total'],
    'formats': ['S32', 'i', 'i', 'i', 'i']})

peoples = np.array(
    [
        ("zhangfei", 66, 65, 30, 0),
        ("guanyu", 95, 85, 98, 0),
        ("zhaoyun", 93, 92, 96, 0),
        ("huangzhong", 90, 88, 77, 0),
        ("dianwei", 80, 90, 90, 0)
    ], dtype=scoretype)

# print(peoples)
peoples[:]['total'] = peoples[:]['chinese'] + \
    peoples[:]['math'] + peoples[:]['english']

name = peoples[:]['name']
wuli = peoples[:]['chinese']
zhili = peoples[:]['english']
tili = peoples[:]['math']


def show(name, cj):
    print name,
    print " |",
    print np.mean(cj),
    print " | ",
    print np.min(cj),
    print " | ",
    print np.max(cj),
    print " | ",
    print np.var(cj),
    print " | ",
    print np.std(cj)

print("科目 | 平均成绩 | 最小成绩 | 最大成绩 | 方差 | 标准差")
show("语文", wuli)
show("英语", zhili)
show("数学", tili)

print("排名:")
ranking = sorted(peoples, cmp=lambda x, y: cmp(
    x[4], y[4]), reverse=True)
print(ranking)
