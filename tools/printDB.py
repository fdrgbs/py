# encoding: utf-8
# encoding: utf-8
# print 1
# print("222")
# import MySQLdb
fo = open("foo", "r")

asd = '''
<if test="AAA != null"> and BBB = #{AAA} </if>
'''

for line in fo.readlines():
    test = line.strip().split(',')
    print asd.replace('AAA', test[0]).replace('BBB', test[1])

# 关闭文件
fo.close()


# fo = open("foo.txt", "r")

# asd = '''
# select order_uid,count(1)  from t_order where order_uid ='AAA' and order_status !=-1 and order_status =5
# union all select order_uid,count(1)  from t_order where order_uid ='AAA' and order_status !=-1;
# '''

# asd = '''
# select count(1)  from t_order where order_uid in (select uid from t_user where parent_uid='AAA') and order_status !=-1 and order_status =5
# union all select count(1)  from t_order where order_uid in (select uid from t_user where parent_uid='AAA') and order_status !=-1;
# '''

# for line in fo.readlines():
#     test = line.strip().split(',')
#     print asd.replace('AAA', test[0]).replace('BBB', test[1])

# # 关闭文件
# fo.close()


# for line in fo.readlines():
#     line = line.strip()
#     print asd.replace('AAA', line)

# # 关闭文件
# fo.close()


# asd = '''
# select AAA,count(1)  from t_order where order_uid in (select uid from t_user where parent_uid='AAA') and order_status !=-1 and order_status =5
# union all select AAA,count(1)  from t_order where order_uid in (select uid from t_user where parent_uid='AAA') and order_status !=-1;
# '''


# select * from t_user_test where parent_uid in (select uid from t_user_test where invite_code in ('MITUI002'));
# select * from t_user_test where parent_uid in (select uid from t_user_test where parent_uid in (select uid from t_user_test where invite_code in ('MITUI002')));
# select * from t_user_test where parent_uid in (select uid from t_user_test where parent_uid in (select uid from t_user_test where parent_uid in (select uid from t_user_test where invite_code in ('MITUI002')))
# );
# select * from t_user_test where parent_uid in (select uid from t_user_test where parent_uid in (select uid from t_user_test where parent_uid in (select uid from t_user_test where parent_uid in (select uid from t_user_test where invite_code in ('MITUI002')))
# ));
# select * from t_user_test where parent_uid in (select uid from t_user_test where parent_uid in (select uid from t_user_test where parent_uid in (select uid from t_user_test where parent_uid in (select uid from t_user_test where parent_uid in (select uid from t_user_test where invite_code in ('MITUI002')))
# )));

# select * from t_user_test where parent_uid in (select uid from t_user_test where parent_uid in (select uid from t_user_test where parent_uid in (select uid from t_user_test where parent_uid in (select uid from t_user_test where parent_uid in (select uid from t_user_test where parent_uid in (select uid from t_user_test where invite_code in ('MITUI002')))
# ))));
