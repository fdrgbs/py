# encoding: utf-8
# print 1
# print("222")

fo = open("foo", "r")


asd = '''
<if test="BBB != null">
    AAA = #{BBB},
</if>
'''


def printme(str):
    "打印任何传入的字符串"
    print str
    return


def formatter(src, firstUpper):
    """
    将下划线分隔的名字,转换为驼峰模式
    :param src: test_date
    :param firstUpper: 转换后的首字母是否指定大写(  testDate or  TestDate)
    :return:testDate
    """
    arr = src.split('_')
    res = ''
    for i in arr:
        res = res + i[0].upper() + i[1:]

    if not firstUpper:
        res = res[0].lower() + res[1:]
    return res

for line in fo.readlines():
    # test = line.strip().split(' ')
    # print asd.replace('AAA', test[0]).replace('BBB', test[1])
    test = formatter(line, False)
    # test = printme(line)
    print test
# 关闭文件
fo.close()


# def printme(str):
#     "打印任何传入的字符串"
#     print str
#     return
