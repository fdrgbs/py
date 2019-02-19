# encoding: utf-8

import pandas as pd
import numpy as np

from pandas import Series, DataFrame
# score = DataFrame(pd.read_excel('data.xlsx'))
# score.to_excel('data1.xlsx')
# print score

data = {'Chinese': [66, 95, 93, 90, 44], 'English': [
    65, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun',
                             'HuangZhong', 'DianWei'], columns=['English', 'Math', 'Chinese'])

# df2 = df2.drop(columns=['Chinese'])
# print df2
# df2 = df2.drop(columns=['Math'])
# print df2


# df2.rename(columns={'Chinese': 'YuWen', 'English': 'Yingyu'}, inplace=True)
# print df2

# 去除重复行
# df2 = df2.drop_duplicates()
# print df2

# df2['Chinese'].astype('str')
# df2['Chinese'].astype(np.int64)
# print df2

# # 删除左右两边空格
# # df2['Chinese'].astype(np.str)
# df2['Chinese'].astype('str')

# print df2
# df2['Chinese'] = df2['Chinese'].map(str.strip)
# # 删除左边空格
# df2['Chinese'] = df2['Chinese'].map(str.lstrip)
# # 删除右边空格
# df2['Chinese'] = df2['Chinese'].map(str.rstrip)


# df2['Chinese'] = df2['Chinese'].str.strip('$')

# # 全部大写
# df2.columns = df2.columns.str.upper()
# print df2
# # 全部小写
# df2.columns = df2.columns.str.lower()
# print df2
# # 首字母大写
# df2.columns = df2.columns.str.title()
# print df2

# df2['Chinese'].astype('str')
# print df2.isnull()
# print df2

# print df2.isnull().any()

# print df2
# df2['Chinese'].astype('str')
# print df2['Chinese'].dtypes

# df2['Chinese'] = df2['Chinese'].apply(str.upper)

# def double_df(x):
#     return 100 * x
# df2[u'Chinese'] = df2[u'Chinese'].apply(double_df)
# print df2

# print df2


# def plus(df, n, m):
#     df['new1'] = (df[u'Chinese'] + df[u'English']) * m
#     df['new2'] = (df[u'Chinese'] + df[u'English']) * n
#     return df
# df2 = df2.apply(plus, axis=1, args=(2, 3,))
# print '\n'

# print df2


# df1 = DataFrame(
#     {'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
# print df1

# print df1.describe()

# df1 = DataFrame(
#     {'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
# df2 = DataFrame(
#     {'name': ['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data2': range(5)})

# df3 = pd.merge(df1, df2, on='name')
# print df1
# print df2
# print df3
# df3 = pd.merge(df1, df2, how='inner')
# print df3

# df3 = pd.merge(df1, df2, how='left')
# print df3
# df3 = pd.merge(df1, df2, how='right')
# print df3
# df3 = pd.merge(df1, df2, how='outer')
# print df3
