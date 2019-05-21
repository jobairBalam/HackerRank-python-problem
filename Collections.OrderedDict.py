from collections import OrderedDict

d = OrderedDict()
num_items = int(input())

for _ in range(num_items):
    item_name, _, item_price = input().rpartition(' ')
    d[item_name] = d.get(item_name, 0) + int(item_price)

for k, v in d.items():
    print(k,v)
