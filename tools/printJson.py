# encoding: utf-8
# print 1
# print("222")
import json

with open('foo', 'r') as f:
    data = json.load(f)

for province in data:
    for city in province['child']:
        if (type(city.get('child', '')) == str):
            print province['id'], province['name'], city['id'], city['name'],
        else:
            for distinct in city['child']:
                print province['id'], province['name'], city['id'], city['name'], distinct['id'], distinct['name']


# for province in data:
#     for city in province['child']:
#         for distinct in city['child']:
# print province['id'], province['name'], city['id'], city['name'],
# distinct['id'], distinct['name']


# for x in data:
#     print x['id'], x['name']
# print(type(data))
# print(len(data))

# print(data.length)
# print data


# encoding: utf-8
# [
#   {
#     "id": 2,
#     "name": "北京",
#     "child": [
#       {
#         "id": 36,
#         "name": "北京市",
#         "child": [
#           {
#             "id": 377,
#             "name": "东城区",
#             "zipcode": "100011"
#           },
#           {
#             "id": 378,
#             "name": "西城区",
#             "zipcode": "100032"
#           },
#           {
#             "id": 381,
#             "name": "朝阳区",
#             "zipcode": "100020"
#           },
#           {
#             "id": 382,
#             "name": "丰台区",
#             "zipcode": "100071"
#           },
#           {
#             "id": 383,
#             "name": "石景山区",
#             "zipcode": "100043"
#           },
#           {
#             "id": 384,
#             "name": "海淀区",
#             "zipcode": "100089"
#           },
#           {
#             "id": 385,
#             "name": "门头沟区",
#             "zipcode": "102300"
#           },
#           {
#             "id": 386,
#             "name": "房山区",
#             "zipcode": "102488"
#           },
#           {
#             "id": 387,
#             "name": "通州区",
#             "zipcode": "101100"
#           },
#           {
#             "id": 388,
#             "name": "顺义区",
#             "zipcode": "101300"
#           },
#           {
#             "id": 389,
#             "name": "昌平区",
#             "zipcode": "102200"
#           },
#           {
#             "id": 390,
#             "name": "大兴区",
#             "zipcode": "102600"
#           },
#           {
#             "id": 391,
#             "name": "怀柔区",
#             "zipcode": "101400"
#           },
#           {
#             "id": 392,
#             "name": "平谷区",
#             "zipcode": "101200"
#           },
#           {
#             "id": 393,
#             "name": "密云县",
#             "zipcode": "101500"
#           },
#           {
#             "id": 394,
#             "name": "延庆县",
#             "zipcode": "102100"
#           }
#         ]


#     ]
#   }
# ]
