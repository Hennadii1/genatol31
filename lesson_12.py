# 1.
# a = 'dfgfdg12f45fdgfd456fdgfdg45dfg798dfgf55fgfdfdg2'
# b = ''
# for i in a:
#     if i >= '0' and i <= '9':
#         b = b + i
# print(b)


# dict1 = {
#   "type": "FeatureCollection",
#   "features": [
#     {
#       "type": "Feature",
#       "properties": {},
#       "geometry": {
#         "type": "Polygon",
#         "coordinates": [
#           [
#             [
#               42.1875,
#               52.696361078274485
#             ],
#             [
#               54.84375,
#               52.696361078274485
#             ],
#             [
#               54.84375,
#               59.5343180010956
#             ],
#             [
#               42.1875,
#               59.5343180010956
#             ],
#             [
#               42.1875,
#               52.696361078274485
#             ]
#           ]
#         ]
#       }
#     },
#     {
#       "type": "Feature",
#       "properties": {},
#       "geometry": {
#         "type": "Polygon",
#         "coordinates": [
#           [
#             [
#               2.4609375,
#               14.26438308756265
#             ],
#             [
#               10.8984375,
#               2.8113711933311403
#             ],
#             [
#               28.828124999999996,
#               -0.7031073524364783
#             ],
#             [
#               30.585937499999996,
#               13.923403897723347
#             ],
#             [
#               18.984375,
#               26.745610382199022
#             ],
#             [
#               2.4609375,
#               14.26438308756265
#             ]
#           ]
#         ]
#       }
#     },
#     {
#       "type": "Feature",
#       "properties": {},
#       "geometry": {
#         "type": "Point",
#         "coordinates": [
#           81.9140625,
#           58.26328705248601
#         ]
#       }
#     }
#   ]
# }
# list1 = []
#
# a = dict1.get("features")
# for i in a:
#     dict2 = {}
#     b = i.get("geometry")
#     c = {b.get("type") : b.get("coordinates")}
#     dict2.update(c)
#     list1.append(dict2)
#
# print(list1)


a = [{1:1}, {2:1}, {3:1}, {4:1}, {'a':1}, {5: 'fdgf'}]

b = {}
for i in a:
    b.update(i)

print(b)
