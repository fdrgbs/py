# encoding: utf-8
# print 1
# print("222")

# fo = open("foo", "r")


# asd = '''
# select order_uid,count(1)  from t_order where order_uid ='AAA' and order_status !=-1 and order_status =5
# union all select order_uid,count(1)  from t_order where order_uid ='AAA'
# and order_status !=-1;


# 个护健康
# 五金工具
# 厨房电器
# 大家电

# '''

# asd = '''
# mysql -h 10.162.19.53 -P 3306 -u yptuishou_r -p0UEUuucRie8RWHktBckrOBCSOdLag4uY --default-character-set=utf8 yptuishou  -e "select b.new_cname2,b.gid,b.name, sum(fee)/100 fee ,sum(case when a.status=5 then fee else 0 end)/100 from t_order_pid a ,t_goods b where a.gid=b.gid and a.status >1 and b.new_cname2 in ('AAA') group by b.new_cname2,b.gid order by fee desc limit 100; " >>    'zzz_good_AAA.txt'
# '''

# for line in fo.readlines():
#     line = line.strip()
#     print asd.replace('AAA', line)

# # 关闭文件
# fo.close()
