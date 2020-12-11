# encoding: utf-8
# print 1
# print("222")

fo = open("foo", "r")


asd = '''
mysql -h 10.162.19.53 -P 3306 -u yptuishou_r -p0UEUuucRie8RWHktBckrOBCSOdLag4uY --default-character-set=utf8 yptuishou  -e "select 'AAA-BBB' ,count(uid),sum(cntPre),sum(fee) 'gmv',sum(pureFee) pureFee from ( select sum(fee) fee,sum(pureFee) pureFee,uid,count(distinct pre_oid1) cntPre from ( select sum(fee/100) fee,sum(case when op.status!=5 then fee/100 else 0 end) pureFee,op.uid,(case when pre_oid =0 then orderid else pre_oid end) pre_oid1  from t_order_pid op left join t_user u on op.uid=u.uid where op.uid=tuishou_uid and goods_type not in (1,4,5) and u.mtime< 1567094400 and op.status >1  and  ptime < u.mtime+31536000 group by op.uid,pre_oid1 ) a group by uid having fee>=AAA and fee<BBB) b " >>    'zzz_zzz_uid-preTime-12.txt'
'''

for line in fo.readlines():
    test = line.strip().split('-')
    print asd.replace('AAA', test[0]).replace('BBB', test[1])
# 关闭文件
fo.close()


# asd = '''
# select 'AAABBB' as 'day',3 'hours',count(distinct orderid) 'order',sum(fee/100) 'money' from t_order_pid where ctime >=UNIX_TIMESTAMP('2019-AAA-BBB 00:00:00') and ctime <UNIX_TIMESTAMP('2019-AAA-BBB 03:00:00') and status in (2,3,6,7)
# union all
# select 'AAABBB' as 'day',6 'hours',count(distinct orderid) 'order',sum(fee/100) 'money' from t_order_pid where ctime >=UNIX_TIMESTAMP('2019-AAA-BBB 03:00:00') and ctime <UNIX_TIMESTAMP('2019-AAA-BBB 06:00:00') and status in (2,3,6,7)
# union all
# select 'AAABBB' as 'day',9 'hours',count(distinct orderid) 'order',sum(fee/100) 'money' from t_order_pid where ctime >=UNIX_TIMESTAMP('2019-AAA-BBB 06:00:00') and ctime <UNIX_TIMESTAMP('2019-AAA-BBB 09:00:00') and status in (2,3,6,7)
# union all
# select 'AAABBB' as 'day',12 'hours',count(distinct orderid) 'order',sum(fee/100) 'money' from t_order_pid where ctime >=UNIX_TIMESTAMP('2019-AAA-BBB 09:00:00') and ctime <UNIX_TIMESTAMP('2019-AAA-BBB 12:00:00') and status in (2,3,6,7)
# union all
# select 'AAABBB' as 'day',15 'hours',count(distinct orderid) 'order',sum(fee/100) 'money' from t_order_pid where ctime >=UNIX_TIMESTAMP('2019-AAA-BBB 12:00:00') and ctime <UNIX_TIMESTAMP('2019-AAA-BBB 15:00:00') and status in (2,3,6,7)
# union all
# select 'AAABBB' as 'day',18 'hours',count(distinct orderid) 'order',sum(fee/100) 'money' from t_order_pid where ctime >=UNIX_TIMESTAMP('2019-AAA-BBB 15:00:00') and ctime <UNIX_TIMESTAMP('2019-AAA-BBB 18:00:00') and status in (2,3,6,7)
# union all
# select 'AAABBB' as 'day',21 'hours',count(distinct orderid) 'order',sum(fee/100) 'money' from t_order_pid where ctime >=UNIX_TIMESTAMP('2019-AAA-BBB 18:00:00') and ctime <UNIX_TIMESTAMP('2019-AAA-BBB 21:00:00') and status in (2,3,6,7)
# union all
# select 'AAABBB' as 'day',24 'hours',count(distinct orderid)
# 'order',sum(fee/100) 'money' from t_order_pid where ctime
# >=UNIX_TIMESTAMP('2019-AAA-BBB 21:00:00') and ctime
# <UNIX_TIMESTAMP('2019-AAA-CCC 00:00:00') and status in (2,3,6,7)

# '''

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
