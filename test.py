# encoding: utf-8

# score = 55
# if score >= 90:
#     print 'Excellent'
# else:
#     if score < 60:
#         print 'Fail'
#     else:
#         print 'Good Job'


# # name = raw_input("What's your name?")
# sum = 100 + 100
# # print('hello,%s' % name)
# print('sum = %d' % sum)


# sum = 0
# for number in range(1, 12, 2):
#     sum = sum + number
# print sum


# for number in range(1, 12, 2):
#     print('sum = %d' % number)

# sum = 0
# number = 1
# while number < 11:
#     sum = sum + number
#     number = number + 1
# print sum


# lists = ['a', 'b', 'c']
# lists.append('d')
# print lists
# print len(lists)
# lists.insert(0, 'mm')
# lists.pop()
# print lists


# tuples = ('tupleA', 'tupleB')
# print tuples[0]


# -*- coding: utf-8 -*
# # 定义一个 dictionary
# score = {'guanyu': 95, 'zhangfei': 96}
# # 添加一个元素
# score['zhaoyun'] = 98
# print score
# # 删除一个元素
# score.pop('zhangfei')
# # 查看 key 是否存在
# print 'guanyu' in score
# # 查看一个 key 对应的值
# print score.get('guanyu')
# print score.get('yase', 99)


s = set(['a', 'b', 'c'])
s.add('d')
s.remove('b')
print s
print 'c' in s
