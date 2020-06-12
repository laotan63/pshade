'''
f = open('yesterday2','a',encoding='utf-8') #文件句柄
f.write('我爱你，我的祖国\n')
print(f)
f.close()
'''
f = open('yesterday','r',encoding='utf-8')
count = 0
for line in f:
    if count ==9:
        print('------分割线------')
        continue
        count +=1
    print(line)
    count +=1

# for index,line in enumerate(f.readlines()):  #f.readlines()把文件按行变成列表
#     if index == 9:
#         print('-------分割线------')
#         continue
#     print(line.strip())

# for i in range(5):
#     print(f.readline())