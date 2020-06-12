list = [1,3,4,6,8,10,1,8]
list_1 = set(list) #变成集合，集合是无序的
print(set(list_1))  #去重
list_2 = set([2, 6, 0, 66, 22, 8, 4])

print(list_1,list_2)
print( list_1.intersection(list_2) )  #交集
print(list_1.union(list_2)) #并集
print(list_1.difference(list_2)) #差集，取list_1里不在list_2里的
print(list_1.issubset(list_2)) #子集，判断1是否是2的子集
print(list_1.issuperset(list_2)) #父集 判断1是否是2的父集
print(list_1.symmetric_difference(list_2)) #去掉2个都有的
print('------------')
print(list_1 & list_2) #交集
print(list_1 | list_2) #并集
print(list_1 - list_2) #in list_1,but not in list_2
print(list_1 ^ list_2) #对称差集
list_1.add(999) #添加一个
print(list_1)
list_1.update([10,11,12]) #添加多项
print(list_1)
list_1.pop()