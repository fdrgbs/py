# -*- coding: utf-8 -*
import redis

# host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
# pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)

# print dir(redis)
# print redis.__file__

# r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

# r.set('name', 'junxi')
# print(r['name'])
# print(r.get('name'))
# print(type(r.get('name')))

r.delete('names')
r.lpush("names", "disen", "jack", "mack")
print r.lrange("names", 0, -1)

# r.geoadd("Guangdong", "113.2099647", "23.593675", "Qingyuan",
#          113.2278442, 23.1255978, "Guangzhou", 113.106308, 23.0088312, "Foshan")
# print r.geopos("Guangdong", "Qingyuan", "Guangzhou")
# print r.geodist("Guangdong", "Qingyuan", "Guangzhou")
# print r.geodist("Guangdong", "Qingyuan", "Guangzhou", unit="km")
# # 佛山和广州都在深圳的半径 120 公里之内
# print r.georadius("Guangdong", 114.0538788, 22.5551603, 120, unit="km",
# withdist=True)

# # 佛山在广州的半径 30 公里范围之内
# print r.georadiusbymember("Guangdong", "Guangzhou", 30, unit="km",
# withdist=True)
