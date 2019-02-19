# encoding: utf-8
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
# data = {'语文': [66, 95, 95, 90, 80, 80], '英语': [
#     65, 85, 92, 88, 90, 90], '数学': [None, 98, 96, 77, 90, 90]}
# df = DataFrame(data, index=['张飞', '关羽', '赵云', '黄忠',
#                             '典韦', '典韦'], columns=['语文', '英语', '数学'])
# df = df.drop_duplicates()
# df = df.fillna(0)


# def total_score(df):
#     df['总分'] = df['语文'] + df['英语'] + df['数学']
#     return df
# df = df.apply(total_score, axis=1)
# print(df)


# scores = {'Chinese': [66, 95, 95, 90, 80, 80],
#           'English': [65, 85, 92, 80, 90, 90],
#           'Math': [None, 98, 96, 77, 90, 90],
#           'Total': [None, None, None, None, None, None]}
# df = DataFrame(scores, index=['Zhang Fei', 'Guan Yu',
#                               'Zhao Yun', 'Huang Zhong', 'Dian Wei', 'Dian Wei'],)

# # Data ckeaning.
# # remove the duplicated record.
# df = df.drop_duplicates()
# # print(df)

# # Calculate the total scores.
# df['Total'] = df.sum(axis=1)
# print(df.describe())


data = np.array([[66, 95, 95, 90, 80, 80], [65, 85, 92,
                                            88, 90, 90], [None, 98, 96, 77, 90, 90]])
df = DataFrame(data.T, index=["张飞", "关羽", "赵云",
                              "黄忠", "典韦", "典韦"], columns=["语文", "英语", "数学"])
print df
df["数学"].fillna(df["数学"].mean().astype(int), inplace=True)
df = df.drop_duplicates()
df["总分"] = df.sum(axis=1)
print df
# df.describe()
print df.loc["张飞"]
