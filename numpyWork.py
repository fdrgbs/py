# encoding: utf-8

import numpy as np

'''
平均成绩、最小成绩、最大成绩、方差、标准差

'''
persontype = np.dtype({
    'names': ['name', 'chinese', 'math', 'english', 'total'],
    'formats': ['S32', 'i', 'i', 'i', 'i']})
peoples = np.array([("ZhangFei", 66, 65, 30, 0), ("GuanYu", 95, 85, 98, 0),
                    ("ZhaoYun", 93, 92, 96, 0), ("HuangZhong", 90, 88, 77, 0),
                    ("dianwei", 80, 90, 90, 0)], dtype=persontype)
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']
peoples[:]['total'] = peoples[:]['chinese'] + \
    peoples[:]['math'] + peoples[:]['english']

print("chinese ave", np.mean(chineses))
print("chinese max", np.amax(chineses))
print("chinese min", np.amin(chineses))
print("chinese std", np.std(chineses))
print("chinese var", np.var(chineses))

print peoples
print np.sort(peoples, order='total')
